import parallelproj
import numpy as np
import pymirc.viewer as pv
from pathlib import Path

from utils_data import bw_pet_phantom

ofile = Path("..") / "data" / "brainweb_parallel_projection.npz"

if not ofile.exists():
    # Load the data
    x_true, x_att = bw_pet_phantom(
        num_downsample=2, sl=(slice(None), slice(None), slice(None))
    )

    n = x_true.shape[0]
    radial_pos = np.arange(n) - n // 2 + 0.5
    view_angles = np.linspace(0, np.pi, 180, endpoint=False)

    proj = parallelproj.ParallelViewProjector3D(
        image_shape=x_true.shape,
        radial_positions=radial_pos,
        view_angles=view_angles,
        image_origin=3 * (radial_pos[0],),
        voxel_size=3 * (1.0,),
        radius=1.2 * radial_pos.max() * np.sqrt(2),
        ring_positions=radial_pos,
        max_ring_diff=0,
    )

    y = proj(x_true)

    np.savez_compressed(
        ofile,
        x_true=x_true,
        y=y,
        view_angles=view_angles,
    )
else:
    data = np.load(ofile)
    x_true = data["x_true"]
    y = data["y"]
    view_angles = data["view_angles"]

vi = pv.ThreeAxisViewer(y)
