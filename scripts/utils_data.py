import numpy as np
import nibabel as nib
from typing import Callable


def bw_map_1(x: int) -> float:
    y = 0.5

    if x == 0:  # outside of brain
        y = 0.0
    elif x == 1:  # CSF
        y = 0.0
    elif x == 2:  # GM
        y = 3.0
    elif x == 3:  # WM
        y = 1.0
    elif x == 4:  # FAT
        y = 0.3
    elif x == 7:  # skull
        y = 0.2
    elif x == 11:  # bone marrow
        y = 0.3

    return y


def bw_pet_phantom(
    sl: tuple[slice, slice, slice] = (slice(None), slice(None), slice(159, 160, None)),
    orientation: str = "LPS",
    num_downsample: int = 2,
    brainweb_subject_num: int = 4,
    map_func: Callable[
        [
            int,
        ],
        float,
    ] = bw_map_1,
) -> tuple[np.ndarray, np.ndarray]:
    """Generate 2D PET brain phantom based on brainweb

    Parameters
    ----------
    sl : tuple[slice, slice, slice], optional
        slices to extract 2D from 3D volume, by default (slice(None), slice(None), slice(159, 160, None))
    orientation : str, optional
        return image in LPS or RAS, by default "LPS"
    num_downsample : int, optional
        number of downsampling steps,
        in every step all dimensions are reduced by a factor of 2,
        final dimension is 512 / (2**num_downsample), by default 2
    brainweb_subject_num : int, optional
        ID of brainweb subject to use, by default 4
    map_func : Callable[ [ int, ], float, ], optional
        function mapping the segmentation int to the PET update float,
        by default bw_map_1

    Returns
    -------
    np.ndarray, nd.ndarray
        2D PET array
    """

    hdr = nib.as_closest_canonical(
        nib.load(f"../data/subject{brainweb_subject_num:02}_crisp_v.mnc.gz")
    )
    brain_seg = hdr.get_fdata()

    if orientation == "LPS":
        brain_seg = np.flip(brain_seg, (0, 1))

    brain_seg = brain_seg[sl]

    brain_seg = np.squeeze(brain_seg)

    if brain_seg.ndim == 2:
        pw0 = (512 - brain_seg.shape[0]) // 2
        pw1 = (512 - brain_seg.shape[1]) // 2
        pad_width = ((pw0, pw0), (pw1, pw1))
    else:
        pw0 = (512 - brain_seg.shape[0]) // 2
        pw1 = (512 - brain_seg.shape[1]) // 2
        pw2 = (512 - brain_seg.shape[2]) // 2
        pad_width = ((pw0, pw0), (pw1, pw1), (pw2, pw2))

    brain_seg = np.pad(
        brain_seg, pad_width=pad_width, mode="constant", constant_values=0
    )

    att_img = 0.01 * (brain_seg > 0).astype(float)
    att_img[brain_seg == 7] = 0.015

    pet_img = np.vectorize(map_func)(brain_seg)

    for _ in range(num_downsample):
        if pet_img.ndim == 2:
            pet_img = pet_img[::2, :] + pet_img[1::2, :]
            pet_img = pet_img[:, ::2] + pet_img[:, 1::2]
            pet_img /= 4
            att_img = att_img[::2, :] + att_img[1::2, :]
            att_img = att_img[:, ::2] + att_img[:, 1::2]
            att_img /= 4
        else:
            pet_img = pet_img[::2, :, :] + pet_img[1::2, :, :]
            pet_img = pet_img[:, ::2, :] + pet_img[:, 1::2, :]
            pet_img = pet_img[:, :, ::2] + pet_img[:, :, 1::2]
            pet_img /= 8
            att_img = att_img[::2, :, :] + att_img[1::2, :, :]
            att_img = att_img[:, ::2, :] + att_img[:, 1::2, :]
            att_img = att_img[:, :, ::2] + att_img[:, :, 1::2]
            att_img /= 8

    return pet_img, att_img
