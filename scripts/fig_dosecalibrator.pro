;energy
en = findgen(600)+1
charsize = 1.5
thick = 7

NIset_psfile, 'fig_dosecalib2.eps', /encaps
plot, en, $
     (1-exp(-nimu2('ar', en)*2*5.)) $  ;attenuation in argon
     * exp(-nimu2('pmma',en)*0.5) $  ;attenuation of recipient or wall.
     * exp(-nimu2('cu',en)*0.005) $  ;attenuation of recipient or wall.
     * en,$                         ;proportional to energy
     xtitle = 'energy keV', $
     ytitle = 'sensitivity (arbitrary units)', yrange = [0,1], $
     charsize = charsize, back = 7, col = 0, thick = thick
oplot, en, $
     (1-exp(-nimu2('ar', en)*2*5.)) $ ;attenuation in argon
     * exp(-nimu2('pmma',en)*0.5) $  ;attenuation of recipient or wall.
     * exp(-nimu2('cu',en)*0.025) $  ;attenuation of recipient or wall.
     * en, col = 1, thick = thick, line = 2
NIset_psfile, /off

NIset_psfile, 'fig_dosecalib1.eps', /encaps, /color
plot, en, $
     (1-exp(-nimu2('ar', en)*2*5.)), $
     xtitle = 'energy keV', $
     ;ytitle = 'attenuation in argon', $
     yrange = [0,1], $
     charsize = charsize, back = 7, col = 0, thick = thick
oplot, en, $
       exp(-nimu2('pmma',en)*0.5) $  ;attenuation of recipient or wall.
       * exp(-nimu2('cu',en)*0.005), $ ;attenuation of recipient or wall.
       col = 1, thick = thick, line = 2

oplot, en, en / 700, col=4, thick=thick, line=3

plots,  [100, 150], [0,0]+0.8, col=1,line=2,thick=thick
xyouts, 170, 0.8, 'Attenuation detector wall, tube, ...', col=1, chars=charsize

plots,  [100, 150], [0,0]+0.7, col=0,line=0,thick=thick
xyouts, 170, 0.7, 'Interaction with gas', col=0, chars=charsize

plots,  [150, 200]-50, [0,0]+0.1, col=4,line=3,thick=thick
xyouts, 220-50, 0.1, 'energy available for ionizations', col=4, chars=charsize
NIset_psfile, /off
