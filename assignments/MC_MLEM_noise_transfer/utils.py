""" utilities for OS-MLEM notebook """
import abc
import math
import numpy as np

import scipy.ndimage as ndi


def test_images(num_pix: int,
                bg_activity: float = 2.,
                insert_activity: float = 2.,
                d_0: float = 0.4,
                d_1: float = 0.7,
                d_insert: float = 0.05,
                d_arm: float = 0.12,
                offset_arm: float = 0.43) -> tuple[np.ndarray, np.ndarray]:
    """
    create emission and attenuation image for 2D "human ellipsoid phantom"
    """

    image_shape = (num_pix, num_pix)
    em_image = np.zeros(image_shape)
    att_image = np.zeros(image_shape)

    x = np.linspace(-0.5, 0.5, num_pix)
    x_0, x_1 = np.meshgrid(x, x, indexing='ij')

    r_ell = np.sqrt((2 * x_0 / d_0)**2 + (2 * x_1 / d_1)**2)
    em_image[r_ell <= 1] = bg_activity

    att_image[r_ell <= 1] = 0.01

    # add insert
    R = np.sqrt(x_0**2 + x_1**2)
    em_image[R <= 0.5 * d_insert] = insert_activity

    # add arms
    r_left_arm = np.sqrt(x_0**2 + (x_1 - offset_arm)**2)
    em_image[r_left_arm <= 0.5 * d_arm] = bg_activity
    att_image[r_left_arm <= 0.5 * d_arm] = 0.01

    r_right_arm = np.sqrt(x_0**2 + (x_1 + offset_arm)**2)
    em_image[r_right_arm <= 0.5 * d_arm] = bg_activity
    att_image[r_right_arm <= 0.5 * d_arm] = 0.01

    return em_image, att_image


#-------------------------------------------------------------------------


class SubsetSlicer(abc.ABC):
    """ abstract base class for defines subset slices """
    @property
    @abc.abstractmethod
    def complete_shape(self) -> tuple[int, ...]:
        """ shape of complete data set """

    @property
    @abc.abstractmethod
    def subset_axis(self) -> int:
        """ subset axis """

    @property
    @abc.abstractmethod
    def num_subsets(self) -> int:
        """ number of subsets """

    @abc.abstractmethod
    def get_subset_slice(self, subset: int) -> tuple[slice, ...]:
        """ get the slice of a subset """

    @abc.abstractmethod
    def get_subset_shape(self, subset: int) -> tuple[int, ...]:
        """ get the shape of a subset """


#-------------------------------------------------------------------------


class InterleavedSubsetSlicer(SubsetSlicer):
    """ class for interleaved subsets along a given axix """
    def __init__(self, complete_shape: tuple[int, ...], num_subsets: int,
                 subset_axis: int):

        self._complete_shape = complete_shape
        self._num_subsets = num_subsets
        self._ndim = len(self._complete_shape)
        self._subset_axis = subset_axis

        self.init_subsets()

    @property
    def complete_shape(self) -> tuple[int, ...]:
        """ shape of complete data set """
        return self._complete_shape

    @property
    def subset_axis(self) -> int:
        """ subset axis """
        return self._subset_axis

    @property
    def num_subsets(self) -> int:
        """ number of subsets """
        return self._num_subsets

    def init_subsets(self) -> None:
        """ initialize the subset set slices and shapes """
        self._subset_slices = []
        self._subset_shapes = []

        all_views = np.zeros(self._num_subsets, dtype=np.int16)

        # interleave the views to maximize the distance between the subsets
        if self._num_subsets > 1:
            all_views[0::2] = np.arange(0, math.ceil(self._num_subsets / 2))
            all_views[1::2] = np.arange(math.ceil(self._num_subsets / 2),
                                        self._num_subsets)
        empty_slice = self._ndim * [slice(None, None, None)]

        for view in all_views:
            sl = empty_slice.copy()
            sl[self._subset_axis] = slice(view, None, self._num_subsets)

            self._subset_slices.append(tuple(sl))

            sh = list(self._complete_shape)
            sh[self._subset_axis] = math.ceil(
                (self._complete_shape[self._subset_axis] - view) /
                self._num_subsets)
            self._subset_shapes.append(tuple(sh))

    def get_subset_slice(self, subset: int) -> tuple[slice, ...]:
        """ get the slice of a subset """
        return self._subset_slices[subset]

    def get_subset_shape(self, subset: int) -> tuple[int, ...]:
        """ get the shape of a subset """
        return self._subset_shapes[subset]


#-------------------------------------------------------------------------


class AffineSubsetMap(abc.ABC):
    """ abstract base class for linear map y = Ax + b supporting subsets """
    @property
    @abc.abstractmethod
    def x_shape(self) -> tuple[int, ...]:
        """ shape of array x """

    @property
    @abc.abstractmethod
    def y_shape(self) -> tuple[int, ...]:
        """ shape of array y """

    @property
    @abc.abstractmethod
    def num_subsets(self) -> int:
        """ number of subsets """

    @abc.abstractmethod
    def get_subset_slice(self, subset: int) -> tuple[slice, ...]:
        """ return slice for subset """

    @abc.abstractmethod
    def get_subset_shape(self, subset: int) -> tuple[int, ...]:
        """ return shape for subset """

    @abc.abstractmethod
    def forward(self, x: np.ndarray) -> np.ndarray:
        """ forward step Ax + b """

    @abc.abstractmethod
    def forward_subset(self, x: np.ndarray, subset: int) -> np.ndarray:
        """ subset forward step A_i x + b_i """

    @abc.abstractmethod
    def adjoint(self, y: np.ndarray) -> np.ndarray:
        """ adjoint of linear part of forward step A^T x """

    @abc.abstractmethod
    def adjoint_subset(self, y: np.ndarray, subset: int) -> np.ndarray:
        """ adjoint of linear part of subset forward step A_i^T x """

    def test_adjoint(self, subset: int = None, rtol: float = 1e-3) -> None:
        """ test wheter adjoint is really the adjoint of forward """

        if subset is not None:
            x = np.random.rand(*self.x_shape)
            x_fwd = self.forward_subset(x, subset)
            y = np.random.rand(*x_fwd.shape)
            y_back = self.adjoint_subset(y, subset)
        else:
            x = np.random.rand(*self.x_shape)
            y = np.random.rand(*self.y_shape)
            x_fwd = self.forward(x)
            y_back = self.adjoint(y)

        return np.isclose((x_fwd * y).sum(), (y_back * x).sum(), rtol=rtol)


#-------------------------------------------------------------------------


class Projector(AffineSubsetMap):
    """ abstract base class for line / volume integral projectors """
    @property
    @abc.abstractmethod
    def voxel_size_mm(self) -> tuple[float, ...]:
        """ shape of array x """


#-------------------------------------------------------------------------


class RotationBased2DProjector(Projector):
    """ base class for line / volume integral projectors """
    def __init__(self,
                 num_pixel: int,
                 pixel_size_mm: float,
                 num_subsets: int = 1,
                 projection_angles: np.ndarray = None):

        if projection_angles is None:
            self._projection_angles = np.linspace(0, 180, 180, endpoint=False)
        else:
            self._projection_angles = projection_angles

        self._image_shape = (num_pixel, num_pixel)
        self._sinogram_shape = (self._projection_angles.shape[0], num_pixel)
        self._voxel_size_mm = (pixel_size_mm, pixel_size_mm)

        self._subset_slicer = InterleavedSubsetSlicer(self._sinogram_shape,
                                                      num_subsets, 0)

        self.rotation_kwargs = dict(reshape=False, order=1, prefilter=False)

        # setup the a mask for the FOV that can be reconstructed (inner circle)
        x = np.linspace(-num_pixel / 2 + 0.5, num_pixel / 2 - 0.5, num_pixel)
        x_0, x_1 = np.meshgrid(x, x, indexing='ij')
        r = np.sqrt(x_0**2 + x_1**2)
        self._mask = (r <= x.max()).astype(float)

    @property
    def x_shape(self) -> tuple[int, ...]:
        """ shape of array x """
        return self._image_shape

    @property
    def y_shape(self) -> tuple[int, ...]:
        """ shape of array y """
        return self._sinogram_shape

    @property
    def num_subsets(self) -> int:
        """ number of subsets """
        return self._subset_slicer.num_subsets

    @property
    def voxel_size_mm(self) -> tuple[float, ...]:
        """ shape of array x """
        return self._voxel_size_mm

    @property
    def mask(self) -> np.ndarray:
        """ FOV mask """
        return self._mask

    def get_subset_slice(self, subset: int) -> tuple[slice, ...]:
        """ return slice for subset """
        return self._subset_slicer.get_subset_slice(subset)

    def get_subset_shape(self, subset: int) -> tuple[int, ...]:
        """ return shape for subset """
        return self._subset_slicer.get_subset_shape(subset)

    def forward(self, image: np.ndarray) -> np.ndarray:
        """ forward step """

        sino = np.zeros(self.y_shape)
        for subset in range(self.num_subsets):
            subset_slice = self.get_subset_slice(subset)
            sino[subset_slice] = self.forward_subset(image, subset)

        return sino

    def forward_subset(self, image: np.ndarray, subset: int) -> np.ndarray:
        """ subset forward step """

        subset_shape = self.get_subset_shape(subset)
        sino = np.zeros(subset_shape)

        subset_slice = self.get_subset_slice(subset)

        masked_image = self._mask * image

        for i, angle in enumerate(self._projection_angles[subset_slice[0]]):
            sino[i, ...] = ndi.rotate(masked_image, angle,
                                      **self.rotation_kwargs).sum(axis=0)

        return sino * self.voxel_size_mm[0]

    def adjoint(self, sinogram: np.ndarray) -> np.ndarray:
        """ adjoint of forward step """
        image = np.zeros(self.x_shape)

        for subset in range(self.num_subsets):
            subset_slice = self.get_subset_slice(subset)
            image += self.adjoint_subset(sinogram[subset_slice], subset)

        return image

    def adjoint_subset(self, sinogram: np.ndarray, subset: int) -> np.ndarray:
        image = np.zeros(self.x_shape)

        subset_slice = self.get_subset_slice(subset)

        for i, angle in enumerate(self._projection_angles[subset_slice[0]]):
            tmp_image = np.tile(sinogram[i, :],
                                self.x_shape[0]).reshape(self.x_shape)
            image += ndi.rotate(tmp_image, -angle, **self.rotation_kwargs)

        return image * self._mask * self.voxel_size_mm[0]


#-------------------------------------------------------------------------


class ImageBasedResolutionModel:
    """ class for image-based resolution modeling """
    def __init__(self, res_fwhm: tuple[float, ...],
                 voxel_size: tuple[float, ...]) -> None:

        self.sigmas = np.array(res_fwhm) / (2.35 * np.array(voxel_size))

    def forward(self, x):
        """ forward step of resolution model """
        return ndi.gaussian_filter(x, self.sigmas)

    def adjoint(self, y):
        """ adjoint step of resolution model """
        return ndi.gaussian_filter(y, self.sigmas)


#-------------------------------------------------------------------------


class PETAcquisitionModel(AffineSubsetMap):
    """ PET acquisition model """
    def __init__(self,
                 proj: Projector,
                 attenuation_image: np.ndarray,
                 contamination_sinogram: np.ndarray,
                 sensitivity_sinogram: np.ndarray,
                 resolution_model: ImageBasedResolutionModel = None) -> None:

        self.proj = proj
        self.attenuation_image = attenuation_image

        # calculate the attenuation sinogram
        self.attenuation_sinogram = np.exp(
            -self.proj.forward(self.attenuation_image))

        # expectatation of flat contamination
        self.contamination_sinogram = contamination_sinogram

        # sensitivity
        self.sensitivity_sinogram = sensitivity_sinogram

        # resolution model
        self.resolution_model = resolution_model

    @property
    def x_shape(self) -> tuple[int, ...]:
        """ shape of array x """
        return self.proj.x_shape

    @property
    def y_shape(self) -> tuple[int, ...]:
        """ shape of array y """
        return self.proj.y_shape

    @property
    def num_subsets(self) -> int:
        """ number of subsets """
        return self.proj.num_subsets

    def get_subset_slice(self, subset: int) -> tuple[slice, ...]:
        """ return slice for subset """
        return self.proj.get_subset_slice(subset)

    def get_subset_shape(self, subset: int) -> tuple[int, ...]:
        """ return shape for subset """
        return self.proj.get_subset_shape(subset)

    def forward_subset(self, image: np.ndarray, subset: int) -> np.ndarray:

        if self.resolution_model is not None:
            image = self.resolution_model.forward(image)

        subset_slice = self.get_subset_slice(subset)

        return self.sensitivity_sinogram[
            subset_slice] * self.attenuation_sinogram[
                subset_slice] * self.proj.forward_subset(
                    image, subset) + self.contamination_sinogram[subset_slice]

    def forward(self, image: np.ndarray) -> np.ndarray:
        sino = np.zeros(self.y_shape)

        for subset in range(self.num_subsets):
            subset_slice = self.get_subset_slice(subset)
            sino[subset_slice] = self.forward_subset(image, subset)

        return sino

    def adjoint_subset(self, sino: np.ndarray, subset: int) -> np.ndarray:
        subset_slice = self.get_subset_slice(subset)

        back_image = self.proj.adjoint_subset(
            self.sensitivity_sinogram[subset_slice] *
            self.attenuation_sinogram[subset_slice] * sino, subset)

        if self.resolution_model is not None:
            back_image = self.resolution_model.adjoint(back_image)

        return back_image

    def adjoint(self, sino: np.ndarray) -> np.ndarray:
        image = np.zeros(self.x_shape)

        for subset in range(self.num_subsets):
            subset_slice = self.get_subset_slice(subset)
            image += self.adjoint_subset(sino[subset_slice], subset)

        return image


#-------------------------------------------------------------------------


class OSMLEM:
    """ class for MLEM with ordered subsets """
    def __init__(self, data: np.ndarray, aff_map: AffineSubsetMap) -> None:

        self.data = data
        self.aff_map = aff_map

        # calculate the sensivity images
        self.sensitivity_imgs = np.zeros((self.aff_map.num_subsets, ) +
                                         self.aff_map.x_shape)

        for subset in range(self.aff_map.num_subsets):
            ones = np.ones(self.aff_map.get_subset_shape(subset))
            self.sensitivity_imgs[subset, ...] = self.aff_map.adjoint_subset(
                ones, subset)

        # indices where all subset have sensitivity > 0
        self.update_inds = np.where(self.sensitivity_imgs.min(axis=0) > 0)

        self.init_image()

    def init_image(self) -> None:
        """ initialize image and reset iteration counter """
        self.image = np.zeros(self.aff_map.x_shape)
        self.image[self.update_inds] = 1
        self.iteration = 0

    def run_update(self, subset: int) -> None:
        """ run OS-MLEM update on a given subset """
        expectation = self.aff_map.forward_subset(self.image, subset)

        subset_slice = self.aff_map.get_subset_slice(subset)

        ratio = self.data[subset_slice] / expectation

        self.image[self.update_inds] *= self.aff_map.adjoint_subset(
            ratio, subset)[self.update_inds]
        self.image[self.update_inds] /= self.sensitivity_imgs[subset, ...][
            self.update_inds]

    def run(self,
            num_iter: int,
            initialize_image: bool = True,
            verbose: bool = False) -> np.ndarray:
        """ run a number of OS-MLEM iterations """

        if initialize_image:
            self.init_image()

        for _ in range(num_iter):
            for subset in range(self.aff_map.num_subsets):
                self.run_update(subset)
                if verbose:
                    print(
                        f'iteration {(self.iteration+1):03} subset {subset:03}',
                        end='\r')

            self.iteration += 1

        return self.image
