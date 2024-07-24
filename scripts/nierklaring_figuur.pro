;cd /nge/maps10000/study/s/soppe_apollonia________________550719V192___77286896/20080829_nier_dyn_lasix/
; .r /home/Sun/nuyts/idl/allerhande/flowfase
;-------
;img1 = fltarr(128,128,120)
;tijd1 = fltarr(120)
;for i = 1,120 do begin
;  img1[*,*,i-1] = niread_file('image2.hd',1,1,i,header=hdr)
;  startt = float(NIfrom_header(hdr,'FRAME_START_TIME_MS')) / 1000.
;  durt   = float(NIfrom_header(hdr,'FRAME_DURATION_MS')) / 1000.
;  tijd1[i-1] = (startt + durt/2) /60.
;  img1[*,*,i-1] /= durt
;endfor

img2 = fltarr(128,128,120)
tijd2 = fltarr(120)
for i = 1,120 do begin
  img2[*,*,i-1] = niread_file('image3.hd',1,1,i,header=hdr)
  startt = float(NIfrom_header(hdr,'FRAME_START_TIME_MS')) / 1000.
  durt   = float(NIfrom_header(hdr,'FRAME_DURATION_MS')) / 1000.
  tijd2[i-1] = (startt + durt/2) /60.
  img2[*,*,i-1] /= durt
endfor


; Twee rois, 'links' en 'rechts'
;------------------------------
if n_elements(rois) eq 0 $
  then rois = niask_roi(total(img2,3))

daar1 = NIwhere_roi(*rois[0], size(img2))
daar2 = NIwhere_roi(*rois[1], size(img2))

value1 = fltarr(120)
value2 = fltarr(120)
for i = 0, 119 do value1[i] = total((img2[*,*,i])[daar1])
for i = 0, 119 do value2[i] = total((img2[*,*,i])[daar2])

niwin, 2, 500,300
plot, tijd2, value2, /nodata, back=7, col=0, xrange=[0,39.5], $
   xtitle='time (min)', chars=1.4, ytitle='activity'
oplot, tijd2[0:79], value1[0:79], col=1, thick=2, line=5
oplot, tijd2[0:79], value2[0:79], col=4, thick=2

pos = 150
niwin, 1, pos*6, pos
interval = [0, 1, 2, 3, 4, 20, 40]
frames = interval*0
c1 = 32
c2 = 95
for i = 0, n_elements(interval)-1 do $
  frames[i] = min(where(tijd2[*] ge interval[i])) > 0
for i = 0, n_elements(frames)-2 do begin &$
  NIimage, total(img2[c1:c2,c1:c2,frames[i]:frames[i+1]],3)$
           /(frames[i+1]-frames[i]+1), $
           /int, xpos = pos*i, /noerase, max=max(img2)*0.6 & $
endfor

niwin,3
niimage,total(img,3), /int
end
