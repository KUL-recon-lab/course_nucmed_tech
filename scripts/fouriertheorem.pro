nrdet  = 200
nrproj = 120
img = nishepp2d(nrdet,nrdet) < 0.12

niwin,0,200
niimage,img,/int

if n_elements(pcoeff) eq 0 then pcoeff = 0L
if pcoeff eq 0L then NIkul_free, pcoeff
pcoeff = NIkul_coeff(nrdet, nrproj)

sino = fltarr(nrdet, nrproj)
NIproj, img, sino, pcoeff=pcoeff

profile = sino(*,0)
niwin,1,280,200
plot, profile, back=7,col=0

fftprof = shift(abs(fft(profile)),nrdet/2)
niwin,2,280,200
plot, fftprof, back=7,col=0,/ylog

fftimg = shift(abs(fft(img)), nrdet/2, nrdet/2)
niwin,3,200
niimage,alog(fftimg > 0.00001)
end
