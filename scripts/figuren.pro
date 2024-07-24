
; Dalende exponent, halfleven = 10 min
;

t = findgen(61)
value = 100 * exp(-t / 10 * alog(2))
plot,t,value,back=7,col=0
niset_ct
oplot, [10,10],[0,50],line=1
oplot, [10,10],[0,50],line=1,col=0
oplot,[0,10],[50,50],line=1,col=0
oplot,t,value,col=0, thick=2


; Poisson versus Gauss
;
value = findgen(30)
mode  = 4
poisson = NIcalcpoisson(value, mode)
plot, value, poisson, psym=1, back=4, thick=2
oplot, value, poisson, psym=1, thick=2
oplot, value, 1/sqrt(2*!pi*mode) * exp(-(value - mode)^2/(2* mode)),thick=2

mode  = 15
poisson = NIcalcpoisson(value, mode)
oplot, value, poisson, psym=1, thick=2, col=3
oplot, value, 1/sqrt(2*!pi*mode) * exp(-(value - mode)^2/(2* mode)),col=3,thi=2

; Energy with angle after scatter
; ------------------------------
hoek = findgen(101) * 2 * !pi / 100. + !pi

energie1 = 511.
energie2 = energie1 / (1 + energie1 * (1 - cos(hoek)) / 511)
x = energie2 * cos(hoek)
y = energie2 * sin(hoek)
plot,x,y, thick=2, back=4
oplot, [0,0], [-511,511], line=1
oplot, [-511,511], [0,0], line=1
daar = where(energie2 ge energie1 * 0.9)
oplot, x(daar), y(daar), color = 1, thick=6
oplot,x,y, thick=2

energie1 = 140.
energie2 = energie1 / (1 + energie1 * (1 - cos(hoek)) / 511)
x = energie2 * cos(hoek)
y = energie2 * sin(hoek)
daar = where(energie2 ge energie1 * 0.9)
oplot, x(daar), y(daar), color = 1, thick=6
oplot,x,y, thick=2

; Dead time
; ---------
countrate = findgen(100)/100. * 5e5
dead = 700 * 1e-9  ; 700 ns
measured = countrate * exp(-countrate * dead)
plot, countrate, countrate, back=4, thick=2, /nodata
oplot, countrate, countrate, col=7, thick = 3, line=2
oplot, countrate, measured, col=3, thick=3 
