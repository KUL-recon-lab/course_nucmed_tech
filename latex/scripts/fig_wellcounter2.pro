NIwin, 2
NIset_ct, ta=0

H = 2 ;cm
D = findgen(151)/10.

NIset_psfile, 'fig_wellcounter2.eps', /encaps
plot, D, (1.0 + D/sqrt(H^2 + D^2)) / 2.0, back=7, col = 0, $
      xtitle = 'depth in crystal [cm]', $
      ytitle = 'geometrical sensitivity', charsize = 1.4, $
      thick=2, charthick = 2
oplot,  D, (1.0 + D/sqrt(H^2 + D^2)) / 2.0, thick=4, col=0
NIset_psfile, /off
