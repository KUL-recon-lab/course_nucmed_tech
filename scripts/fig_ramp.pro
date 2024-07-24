; Plot the ramp filter
;---------------------
NIset_ct,ta=0
x2 = findgen(401) & w2 = 1./20.
x2 -= mean(x2)

daar = where(x2 eq 0)
if daar[0] ne -1 then x2[daar] = 1e-5
x = findgen(41) & w = 1/2.0
x -= mean(x)
daar = where(x eq 0)

x2 *= max(x) / max(x2)

if daar[0] ne -1 then x[daar] = 1e-5

r1 = w * sin(2*!pi*x*w) / (!pi*x)
r2 = - (sin(!pi*w*x) / (!pi*x) )^2
plot,x,r1+r2,back=7,col=0
oplot, [-2,2]*max(abs(x)), [0,0], col=100
oplot,x,r1+r2,col=0,thick=3

r21 = w * sin(2*!pi*x2*w) / (!pi*x2)
r22 = - (sin(!pi*w*x2) / (!pi*x2) )^2

!p.multi = 0
NIset_psfile, 'fig_rampfilter_app.eps', /encaps, /color, $
  xsize = 20, ysize=14
plot, x2, r21+r22, col=0, back=7,thick=4, $
  xtitle='position', ytitle='amplitude', $
  title = 'inverse Fourier transform of ramp filter',$
  charsize=1.2, charthick=2
oplot, x, r1+r2, col=1, psym=4,thick=4
oplot, x, r1+r2, col=1, line=0,thick=2
NIset_psfile, /off


NIset_psfile, 'fig_rampfilter2_app.eps', /encaps, /color, $
  xsize = 15, ysize=7
!p.position = 0
!p.multi = [0,3,1]
freq = findgen(500)
freq -= mean(freq)
freq *= 0.5 / max(abs(freq))
plot, freq, abs(freq), back=7,col=0, thick=4, $
  xrange = [-0.55, 0.55], yrange = [0,0.55], $
  xtitle = 'frequency', ytitle = 'amplitude', title='ramp filter', $
  charsize=1.2, charthick=2

plot, freq, float(abs(freq) lt 0.5) * 0.5, $
  xrange = [-0.55, 0.55], yrange = [0,0.55], $
  xtitle = 'frequency', ytitle = 'amplitude', title='rectangle', $
  charsize=1.2, charthick=2, col=0, back=7, thick=4

plot, freq, 0.5 - abs(freq), $
  xrange = [-0.55, 0.55], yrange = [0,0.55], $
  xtitle = 'frequency', ytitle = 'amplitude', title='triangle', $
  charsize=1.2, charthick=2, col=0, back=7, thick=4
NIset_psfile, /off
