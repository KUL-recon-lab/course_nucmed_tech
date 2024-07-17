nrdet  = 200
nrproj = 240
img = fltarr(nrdet, nrdet)
daar = niellipse(nrdet/50, nrdet/50, size=size(img), /pix)
img(daar) = 1.0

niwin,0,nrdet
niimage,img

if n_elements(pcoeff) eq 0 then pcoeff = 0L
if pcoeff eq 0L then NIkul_free, pcoeff
pcoeff = NIkul_coeff(nrdet, nrproj)
sino = fltarr(nrdet, nrproj)
NIproj, img, sino, pcoeff=pcoeff

niwin, 1, nrdet, nrproj
niimage,sino

backp = img*0
NIproj, backp, sino, pcoeff=pcoeff, /back
niwin, 2, nrdet, nrdet
niimage,alog(backp > 0.001)
end
