nrdet  = 100
nrproj = 140

img = fltarr(nrdet, nrdet)
daar = niellipse(3, 3, size=size(img), /pix)
img[daar] = 1.

if n_elements(pcoeff) eq 0 then pcoeff = 0L
NIkul_free, pcoeff
pcoeff = NIkul_coeff(nrdet, nrproj)

sino = fltarr(nrdet, nrproj)
NIproj, img, sino, pcoeff=pcoeff

sinos = shift(sino, 3)
cbp = fltarr(nrdet, nrdet)
NIcbp, cbp, sinos, pcoeff=pcoeff

niwin, 0, nrdet*2
niimage,img
niwin, 1, nrdet*2, nrproj*2
niimage,sino
niwin,2,nrdet*2
niimage,cbp
niwin,3, nrdet*2, nrproj*2
niimage,sinos
