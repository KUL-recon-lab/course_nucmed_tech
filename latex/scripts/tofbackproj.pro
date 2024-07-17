; Confirm that a TOF backproject is
; 1/|r| multiplied with 2D Gauss.
;----------------------------------
if NIwexist(2) eq 0 then begin
  niwin, 2
  niset_ct,ta=0
endif

if 0 then begin
  npoints = 201
  nangles = 2*npoints
  sigma   = 25.
  x = findgen(npoints)
  x -= mean(x)
  y = exp(- x^2/(2*!pi*sigma^2))
  img = fltarr(npoints, npoints)
  img[npoints/2,*] = y
  outimg = 0.0
  for i =0,nangles-1 do  outimg += NItransform(img, tan=!pi/nangles*i, /int)
  
  numer = outimg[*,npoints/2]
  epsil = 0.1
  daar = where(x ne 0, compl = nul)
  calc = fltarr(npoints)
  calc[daar]  = nangles/(!pi * abs(x[daar])) * exp(-x[daar]^2/(2*!pi*sigma^2))
  calc[nul]   = nangles
  
  
  plot, x, numer
  oplot, x, calc, col=1
  wait, 1
  plot, x, numer, /ylog
  oplot, x, calc, col=1
endif

; TOF FBP filter is the ramp filter in spatial domain
; multiplied with Gauss, or equivalently, the ramp filter in the
; frequency domain, convolved with a Gauss.
;------------------------------------------------------------
if 1 then begin
  npoints = 501
  sigma   = 7.
  nangles = npoints
  x = findgen(npoints)
  x -= mean(x)
  psf = 1./(abs(x) > 0.5)
  ;ramp = 1./ psf
  ramp = abs(x)

  maskx = findgen(2 * (npoints/4) + 1)
  maskx -= mean(maskx)
  masky = exp(- maskx^2/(2*!pi*sigma^2))
  masky /= total(masky)

  ramp_gauss = convol(ramp, masky, /edge_w)

  x2 = x # (fltarr(1,npoints)+1.)
  y2 = transpose(x2)
  psf2 = 1./(sqrt(x2^2 + y2^2) > 0.5)

  ramp2 = sqrt(x2^2 + y2^2)
  ramp2_gauss = convol(ramp2, masky, /edge_w)
  ramp2_gauss = convol(ramp2_gauss, transpose(masky), /edge_w)
  ramp1_gauss = ramp2_gauss[*,npoints/2]
  
  psf2_gauss = convol(psf2, masky, /edge_w)
  psf2_gauss = convol(psf2_gauss, transpose(masky), /edge_w)
  psf_gauss = psf2_gauss[*,npoints/2]
  plot, x, psf_gauss * ramp_gauss, thick=4
endif
end
