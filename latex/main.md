---
title: Nuclear Medicine Technology and Techniques
authors:
- name: Johan Nuyts
  affiliations:
    - id: kul
      institution: KU Leuven
- name: Georg Schramm
  affiliation: kul
bliography:
  - main
math: {}
github: https://github.com/KUL-recon-lab/course_nucmed_tech
---

+++
(well-counters-radionuclide-calibrators-and-survey-meters)=
## Well counters, radionuclide calibrators and survey meters

On many occasions, it is very handy or even essential to have relatively simple devices to detect or quantify ionizing radiation. Three important applications for such devices are:

*   To determine the amount of radioactivity in a syringe, so that one can adjust and/or verify how much activity is going to be administered to the patient.

*   To determine the amount of radioactivity in a sample (usually blood samples) taken from the patient. The problem is the same as the former one, but the amount of radioactivity in a small sample is typically orders of magnitude less than the injected dose.

*   To detect contaminations with radioactivity, e.g. due to accidents with a syringe or a phantom.

To use a PET or gamma camera for these tasks would obviously be overkill (no imaging required), impractical (they are large and expensive machines) and inefficient (for these tasks, relatively simple systems with better sensitivity can be designed). Special detectors have been designed for each of these tasks:

*   *the well counter*, for measuring small amounts of activity in small volumes,

*   *the radionuclide calibrator* for measuring high amounts of activity in small volumes,

*   *the survey meter* for finding radioactivity in places where there should be none.

(well-counter)=
### Well counter

% %%%%%%%%%%%%%%%%%%%%

:::{figure} figs/fig_wellcounter.pdf
:name: fig:wellcounter
:align: center
:alt: Diagram of a well counter, showing a test tube inside the well.

*Diagram of a well counter, showing a test tube inside the well.*
:::

The well counter consists of a scintillator crystal, typically NaI(Tl), a PMT, lead shielding and electronics to control the PMT and the user interface. The crystal has a cavity (the well), in which a test tube (or any other small object) with a radioactive substance can be put. As illustrated in [](#fig:wellcounter), the radioactive substance is almost completely surrounded by the scintillator crystal. This gives the well counter an extremely high sensitivity, enabling it to detect minute quantities of radioactivity. The well counter detects individual photons, and similar to a gamma camera, it can estimate the energy of the detected photon with an energy resolution of about 10%.

The crystal is usually several centimeters thick to further improve the detection efficiency. The efficiency decreases (non-linearly) with increasing energy, because photons with higher energy have a higher probability of traveling through the crystal without interaction. The effect of the crystal thickness can be taken into account by calibrating the well counter, which is done by the vendor.



:::{figure} figs/fig_wellcountersens.pdf
:name: fig:wellcountersens
:alt: Left: diagram of a well counter, showing a test tube inside the well. Right: the geometrical sensitivity of the well counter to activity inside the tube, as a function of the depth inside the crystal (H = 2 cm).
:::

One problem of the well counter is that its sensitivity varies with the position of the source inside the crystal: the deeper a point source is positioned inside the crystal, the smaller the chance that its photons will escape through the entrance of the cavity. A simple approximate calculation illustrates the effect. Suppose that the radius of the cylindrical cavity is {math}`H` and that a point source is positioned centrally in the hole at a depth {math}`D`. As illustrated in [](#fig:wellcountersens), we have to compute the solid angle of the entrance, as seen from the point source, to obtain the chance that a photon escapes. A similar computation was done near equation [](#eq:collim:fwhm), but this time, we cannot ignore the curvature of the sphere surface, because the entrance hole is fairly large:

```{math}
\mbox{escape-chance}(D)
  = \frac{1}{4\pi R^2}\int_0^\alpha 2\pi H'(\alpha') \; R d\alpha'
```

&#x20;where the value of {math}`H'` in the integral goes from {math}`H'(0) = 0` to {math}`H'(\alpha) = H`. A particular value of {math}`\alpha'` defines a circular line on the sphere, and a small increment {math}`d \alpha'` turns the line into a small strip with thickness {math}`R d \alpha'`.



Substituting {math}`H'(\alpha') = R \sin(\alpha'))` one obtains:

```{math}
:label: eq:wellcounter

\begin{align}
  \mbox{escape-chance}(D)
 &= \frac{1}{4\pi R^2}\int_0^\alpha 2\pi R^2 \sin(\alpha') d\alpha' \nonumber\\
 &=  \frac{1}{2} \left. (- \cos(\alpha')) \right|_0^\alpha \nonumber\\
 &=  \frac{1}{2} (1 - \cos(\alpha)) 
     \;\; = \;\; \frac{1}{2}\left(1 - \frac{D}{\sqrt{D^2 + H^2}}\right)
     
\end{align}
```

And the chance that the photon will be detected equals

```{math}
:label: eq:wellcountersens

\mbox{sensitivity}(D) = 1 - \mbox{escape-chance}(D) = \frac{1}{2}\left(1 + \frac{D}{\sqrt{D^2 + H^2}}\right) \ .
```

We find that for {math}`D = 0`, the sensitivity is 0.5, which makes sense, because all photons going up will escape and all photons going down will hit the crystal. For {math}`D` going to ∞, the sensitivity goes to unity. Note that the equation also holds for negative {math}`D`, which means putting {math}`D` above the crystal. That makes the sensitivity smaller than 0.5, and for 
{math}`D = -\infty`, the sensitivity becomes zero. A plot of the sensitivity as a function of the depth {math}`D` is also shown in 
[](#fig:wellcountersens), for {math}`H` = 2 cm, i.e. a cylinder diameter of 4 cm. This figure clearly shows that the sensitivity variations are not negligible. One should obviously put objects as deep as possible inside the crystal. Suppose we have two identical test tubes, both with exactly the same amount of activity, but dissolved in different amounts of water. If we measure the test tubes one after the other with a well counter, putting each tube in exactly the same position, the tube with less water will produce more counts!

Expression [](#eq:wellcountersens) is approximate in an optimistic way, because it ignores (amongst other effects) the possibility of a photon traveling through the crystal without any interaction. Although the well counter is well shielded, it not impossible that there would be other sources of radioactivity in the vicinity of the device, which could contribute a bit of radiation during the measurement. Even a very small amount of background radiation could influence the measurement, in particular if samples with very low activity are being measured. For that reason, the well counter can do a background measurement (simply a measurement without a source in the detector), and subtract the recorded value from subsequent measurements. Of course, if there would be a significant background contribution, it would usually be much better to remove or shield it than to leave it there and correct for it.

(radionuclide-calibrator)=
### Radionuclide calibrator

% %%%%%%%%%%%%%%%%%%%%%%%%

Because the radionuclide calibrator is a gas filled detector, a small introduction to gas filled detectors is given first.

(gas-filled-detectors)=
#### Gas filled detectors

% --------------------------------

A gas filled detector consists of an anode and a cathode with a gas between them. When a photon or particle travels through the gas, it will ionize some of the atoms in the gas. If there would be no voltage difference between the anode and the cathode, the electrons and ions would recombine. But with a non-zero voltage, the electrons and positive ions travel to the anode and cathode respectively, creating a small current. If enough atoms are ionized, that current can be measured. A cartoon drawing is shown in [](#fig:gasdetector).

If the voltage between the cathode and the anode is low, the electrons and ions travel slowly, and have still time to recombine into neutral atoms. As a result, only a fraction of them will reach the electrodes and contribute to a current between anode and cathode. That fraction increases with increasing voltage, until it becomes unity (i.e. all ionizations contribute to the current). Further increases in the voltage have little effect on the measured current. This first plateau in the amplitude vs voltage curve ([](#fig:gasdetector)) is the region where *ionization chambers* are typically operated. In this mode, the output is proportional to the total number of ionizations, which in turn is proportional to the energy of the particles. A single particle does not produce a measurable current, but if many particles travel through the ionization chamber, they create a measurable current which is proportional to the total energy deposited in the gas per unit of time.



:::{figure} figs/fig_gasdetector.pdf
:name: fig:gasdetector
:alt: The gas detector. Left: the detector consists of a box containing a gas. In this drawing, the anode is a central wire, the cathode is the surrounding box. A photon or particle traveling through the gas produces ionizations, which produce a current between anode and cathode. Right: the current created by a particle depends on the applied voltage.

*The gas detector. Left: the detector consists of a box containing a gas. In this drawing, the anode is a central wire, the cathode is the surrounding box. A photon or particle traveling through the gas produces ionizations, which produce a current between anode and cathode. Right: the current created by a particle depends on the applied voltage.*
:::

With increasing voltage, the speed of the electrons pulled towards the anode increases. If that speed is sufficiently high, the electrons have enough energy to ionize the gas atoms too. This avalanche effect increases the number of ionizations, resulting in a magnification of the measured current. This is the region where proportional counters are operated. As schematically illustrated in 
[](#fig:gasdetector), the amplification increases with the voltage. In this mode, a single particle can create a measurable current, and that current is proportional to the energy deposited by that particle in the gas.

With a still higher voltage, the avalanche effect is so high that a maximum effect is reached, and the output becomes independent of the energy deposited by the traversing particle. The reason is that the electrons hit the anode with such a high energy that UV photons are emitted. Some of those UV photons travel through the gas and liberate even more electrons. In this mode, the gas detector can be used as a Geiger-Muller counter.



[^wjSp7GyECy]

[^wjSp7GyECy]: Special tricks must actually be used to make sure that the avalanche dies out after a while, the avalanche must be quenched. A common approach is to use "quenching gases", which happen to have the right features to avoid the excessive positive feedback that would maintain the ionization avalanche.



The Geiger-Muller counter detects individual particles, but its output is independent of the energy deposited by the particle.

(radionuclide-calibrator)=
#### Radionuclide calibrator

% ---------------------------

A radionuclide calibrator looks similar to a well counter, it also has a small cylindrical hole surrounded by the detector. But instead of a crystal with PMT, an ionisation chamber is used.



The output of the detector is proportional to the total number of ionized gas atoms, which in turn is proportional to the energy deposited in the gas, and therefore also proportional to the activity put in the detector gap. The detector measures the contribution of many photons simultaneously, and therefore it obtains no information about the energy of individual photons. This lack of energy discrimination is a drawback, but the capability of dealing with many simultaneous incident photons (or other particles) makes this detector useful for the measurement of high activities (which would saturate photon counting devices, see section [](#sec:deadtime)).

Ionisation chambers often use air, but for radionuclide calibrators, typically pressurised Argon is used. The high pressure in the chamber reduces the sensitivity to the atmospheric pressure. In addition, the high pressure (more atoms) and the higher attenuation of Ar improve the sensitivity of the detector. Radionuclide calibrators designed for higher activities (up to ± 20 Ci or ± 750 GBq) use typically a pressure of around 5 bar. These radionuclide calibrators are more likely to be found at PET sites, where higher activities can be used because of the short half lifes of most PET isotopes. For quantifying lower activities (up to ± 5 Ci or ± 200 GBq), radionuclide calibrators with a higher pressure (± 12 bar) are used, because a higher pressure improves the stability for low activity counting.

Since the geometry of the radionuclide calibrator is similar to that of the well counter, it suffers from the same position dependent response illustrated in [](#fig:wellcountersens). But in contrast to the well counter, the response of the radionuclide calibrator is also heavily dependent upon the energy of the photons emitted by the isotope. The photons have to reach the gas, and to do so, they must travel through the water in the test tube, through the wall of the test tube and through the wall of the radionuclide calibrator. Then, they have to interact with the gas to produce ionisations. The probability of interactions (attenuation) decreases with increasing energy. Finally, in every interaction, a few tens of eV are transferred, so the higher the energy of the photon, the more ionisations that same photon could produce. These three effects are illustrated in [](#fig:dosecalib). The figure also shows their product, which has a sharp local maximum at low energies, and increases with increasing energy. This is only a rough approximation, the actual curve for a particular radionuclide calibrator depends on many things and it is safer (and much easier) to measure it than to compute it. Knowing the emissions of a particular isotope, and the sensitivity of the radionuclide calibrator for each of those emissions, one can deduce the activity of the isotope from the radionuclide calibrator measurement. A well calibrated radionuclide calibrator will do this automatically for you, you only have to tell it which isotope you are measuring, typically by selecting it from a menu.

The high sensitivity at low energies can be problematic for isotopes such as {sup}`123`I and {sup}`111`In, which emit a fairly large amount of low energy photons (see [](#tab:dosiscalib)). The problem is that these low energy photons are easily attenuated by a little bit of water or a small amount of glass, and therefore, the dosis calibrator would give very different responses when measuring the same activity in different test tubes. The reproducibility improves dramatically when these photons are eliminated by adding a bit of attenuating material, such as a “Cu-filter”. This filter is basically a copper recipient with a very thin wall (half a mm or less), which has very high attenuation for low energies, but only moderate attenuation for higher energies. This is illustrated in the right panel of [](#fig:dosecalib).

:::{list-table} Emissions of {sup}`123`I and {sup}`111`In.
:header-rows: 0
:name: tab:dosiscalib
:align: center

*   *   Energy [keV]

    *   Iodine-123 emissions

    *   Energy

    *   Indium-111 emissions

*   *   159

    *   83.5%

    *   172

    *   90%

*   *

    *

    *   247

    *   94%

*   *   27

    *   71 %

    *   23

    *   70%

*   *   31

    *   15 %

    *   26

    *   14%
:::

:::{figure} figs/fig_dosecalib1.pdf
:name: fig:dosecalib
:alt: Left: loss of photons due to attenuation in the test tube, detector wall etc., probability of interaction of the photons with the gas and the number of ionisations that could be produced with the energy of the photon (in arbitrary units), all as a function of the photon energy. Right: the combination of these three effects yields the sensitivity of the radionuclide calibrator as a function of the photon energy (solid line). The dashed line shows the sensitivity when the sample is surrounded by an additional Cu-filter of 0.2 mm thick.
:::

Just like the well counter, the dosis calibrator can measure the background contribution and correct for it during measurements of radioactive sources.

Radionuclide calibrators are designed to be very accurate, but to fully exploit that accuracy, they should be used with care (e.g. using Cu-filters when needed, position the syringe correctly et), and their performance should be monitored with a rigorous quality control procedure.

An important quality control test is to verify the linearity of the radionuclide calibrator over the entire range of activities that is supported, from 1 MBq to about 400 GBq.

(survey-meter)=
### Survey meter

% %%%%%%%%%%%%%%%%%%%%%

Survey meters are small hand held, battery powered devices, usually containing a gas detector, i.e. an unshielded ionization chamber, proportional counter or Geiger-Muller counter. Survey meters based on ionization chambers basically measure the energy deposited in a particular mass of air, i.e. the *air Kerma*, where “Kerma” stands for “kinetic energy released in media”. Air Kerma is the amount of energy per unit mass released in air, and has units of Gy. The output of such a dosimeter would then typically be expressed in microGy/hr or similar unit. Since the attenuation per gram air is similar to the attenuation per gram tissue, air Kerma provides a reasonable estimate of the absorbed dose in human tissues produced by the radiation, the conversion factor is about 1.1, so

```{math}
\mbox{(absorbed dose in water or tissue)} \; \simeq \; 1.1 \; \times \;
    \mbox{(air Kerma)}.
```

Other types of survey meters use a Geiger-Muller counter. Often the device has a microphone and makes a clicking sound for every detected particle. The Geiger-Muller counter counts the incoming photons (or other particles), but it does not measure its energy.

Finally, still other survey meters contain a scintillation crystal with photomultiplier. These are also called “contamination monitors”, because they can be used to measure the spectrum of the activity, to find out which tracer has caused the contamination. This is important information: a contamination with a long lived tracer is obviously a more serious problem than with a short lived tracer.

Most survey meters can usually measure both photons and beta-particles (electrons and positrons). Remember that to measure contamination with beta-particles, the survey meter must be hold at small distance, because in contrast to x-rays or gamma rays, beta-particles have non-negigible attenuation in air.

+++
(image-analysis)=
## Image analysis

%  ROI

%  SUV

%  Kinetic modeling

In principle, PET and SPECT have the potential to provide quantitative images, that is pixel values can be expressed in Bq/ml. This is only possible if the reconstruction is based on a “sufficiently accurate” model, e.g. if attenuation is not taken into account, the images are definitely not quantitative. It is difficult to define “sufficiently accurate”, the definition should certainly depend upon the application. Requirements for visual inspection are different from those for quantitative analysis.

In image analysis often *regions of interest* (ROI’s) are used. A region of interest is a set of pixels which are supposed to belong together. Usually, an ROI is selected such that it groups pixels with (nearly) identical behavior, e.g. because they belong to the same part of the same organ. The pixels are grouped because the relative noise on the mean value of the ROI is lower than that on the individual pixels, so averaging over pixels results in strong noise suppression. ROI definition must be done carefully, since averaging over non-homogeneous regions leads to errors and artifacts! Ideally an ROI should be three-dimensional. However, mostly two dimensional ROI’s defined in a single plane are used for practical reasons (manual ROI definition or two-dimensional image analysis software).

In this chapter only two methods of quantitative analysis will be discussed: standard uptake values (SUV) and the use of compartmental models. SUV’s are simple to compute, which is an important advantage when the method has to be used routinely. In contrast, tracer kinetic analysis with compartmental models is often very time consuming, but it provides more quantitative information. In nuclear medicine it is common practice to study the kinetic behavior of the tracer, and many more analysis techniques exist. However, compartmental modeling is among the more complex ones, so if you understand that technique, learning the other techniques should not be too difficult. The book by Cherry, Sorenson and Phelps {cite:t}`Cherry` contains an excellent chapter on kinetic modeling and discusses several analysis techniques.

(standardized-uptake-value)=
### Standardized Uptake Value

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

The standardized uptake value provides a robust scale of tracer amounts. It is defined as:

```{math}
\begin{align}
  \mbox{SUV}_j &= \frac{\mbox{tracer concentration in $j$}}
                          {\mbox{average tracer concentration}}\\
  &= \frac{\mbox{tracer amount in Bq/g at pixel $j$}}
                      {\mbox{total dose in Bq / total mass in g}}
\end{align}
```

To compute it, we must know the total dose administered to the patient. Since the total dose is measured prior to injection, and the image is produced after injection, we must correct for the decay of the tracer in between. Moreover, the tracer amounts are measured with different devices: the regional tracer concentration is measured with the SPECT or PET, the dose is measured with a radionuclide calibrator. Therefor, the sensitivity of the tomograph must be determined. This is done by acquiring an image of a uniform phantom filled with a know tracer concentration. From the reconstructed phantom image we can compute a calibration factor which converts “reconstructed pixel values” into Bq/ml (see section [](#sec:scalefactor)).

A SUV of 1 means that the tracer concentration in the ROI is identical to the average tracer concentration in the entire patient body. A SUV of 4 indicates markedly increased tracer uptake. The SUV-value is intended to be robust, independent from the administered tracer amount and the mass of the patient. However, it changes with time, since the tracer participates in a metabolic process. So SUVs can only be compared if they correspond to the same time after injection. Even then, one can think of many reasons why SUV may not be very reproducible, and several publications have been written about its limitations. Nevertheless, it works well in practice and is used all the time.

The SUV is a way to quantify the tracer concentration. But we don’t really want to know that. The tracer was injected to study a metabolic process, so what we really want to quantify is the intensity of that process. The next section explains how this can be done. Many tracers have been designed to accumulate as a result of the metabolic process being studied. If the tracer is accumulated to high concentrations, many photons will be emitted resulting in a signal with good signal to noise ratio. In addition, although the tracer concentration is not nicely proportional to the metabolic activity, it is often an increasing function of that activity, so it still provides useful information.

(tracer-kinetic-modeling)=
### Tracer kinetic modeling

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

(introduction)=
#### Introduction

% ========================

:::{figure} figs/fig_dyncardio.pdf
:name: fig:dyncardio
:align: center
:alt: Four samples from a dynamic study. Each sample shows a short axis and long axis slice through the heart. The wall of the left ventricle is delineated. 20 s after injection, the tracer is in the right ventricle. At 40 s it arrives in the left ventricle. At 3 min, the tracer is accumulating in the ventricular wall. At 20 min, the tracer concentration in the wall is increased, resulting in better image quality.

*Four samples from a dynamic study. Each sample shows a short axis and long axis slice through the heart. The wall of the left ventricle is delineated. 20 s after injection, the tracer is in the right ventricle. At 40 s it arrives in the left ventricle. At 3 min, the tracer is accumulating in the ventricular wall. At 20 min, the tracer concentration in the wall is increased, resulting in better image quality.*
:::

The evolution of the tracer concentration as a function of time can be imaged with PET (or SPECT) using “dynamic acquisition”. Instead of creating a single image, a series of images is created, typically starting at the time of tracer injection and continuing for 30 - 90 minutes, depending on the tracer and the kinetic model that is used to analyse the results.

The evolution of the tracer concentration with time in a particular point (pixel) depends on the tracer and on the characteristics of the tissue in that point. [](#fig:dyncardio) shows the evolution of radioactive ammonia {sup}`13`NH{sub}`3` (recall that {sup}`13`N is a positron emitter) in the heart region. This is a perfusion tracer: its concentration in tissue depends mainly on blood delivery to the cells. The tracer is injected intravenously, so it first shows up in the right atrium and ventricle. From there it goes to the lungs, and arrives in the left ventricle after another 20 s. After that, the tracer is gradually removed from the blood since it is accumulated in tissue. The myocardial wall is strongly perfused, after 20 min accumulation in the left ventricular wall is very high, and even the thin right ventricular wall is clearly visible.

The most important factor determining the dynamic behavior of ammonia is blood flow. However, the ammonia concentration is not *proportional* to blood flow. To quantify the blood flow in ml blood per g tissue and per s, the flow must be computed from dynamic behavior of the tracer. To do that, we need a mathematical model that describes the most important features of the metabolism for this particular tracer. Since different tracers trace different metabolic processes, different models may be required for different tracer.

(the-compartmental-model)=
#### The compartmental model

% ===================================

(the-compartments)=
##### The compartments

% -------------------------------

In this section, the three compartment model is described. It is a relatively general model and can be used for a few different tracers. We will focus on the tracer {sup}`18`F-fluorodeoxyglucose (FDG), which is a glucose analog. “Analog” means that it is *no* glucose, but that it is sufficiently similar to follow, to some extent, the same metabolic pathway as glucose. In fact, it is a better tracer than radioactive glucose, because it is trapped in the cell, while glucose is not. When glucose enters the cell, it is metabolized and the metabolites may escape from the cell. As a result, radioactive glucose will never give a strong signal. In contrast, FDG is not completely metabolized (because of the missing oxide), and the radioactive {sup}`18`F atom stays in the cell. If the cells have a high metabolism, a lot of tracer will get accumulated resulting in a strong signal (many photons will be emitted from such a region, so the signal to noise ratio in the reconstructed image will be good).

:::{figure} figs/fig_kinemodel.pdf
:name: fig:kinemodel
:align: center
:alt: Three compartment model, and corresponding regions in a cardiac study. The first compartment represents plasma concentration (blood pool ROI), the second and third compartment represent the extavascular tracer in original and metabolized form (tissue ROI). For the tissue curve, both the measured points and the fitted curve are shown.

*Three compartment model, and corresponding regions in a cardiac study. The first compartment represents plasma concentration (blood pool ROI), the second and third compartment represent the extavascular tracer in original and metabolized form (tissue ROI). For the tissue curve, both the measured points and the fitted curve are shown.*
:::

[](#fig:kinemodel) shows the three compartmental model and its relation to the measured concentrations. The first compartment represents the radioactive tracer molecule present in blood plasma. The second compartment represents the unmetabolized tracer in the “extravascular space”, that is, everywhere except in the blood. The third compartment represents the radioactive isotope after metabolization (so it may now be part of a very different molecule). In some cases, the compartments correspond nicely to different structures, but in other cases the compartments are abstractions. E.g., the second two compartments may be present in a single cell. We will denote the blood plasma compartment with index **P**, the extravascular compartment with index **E** and the third compartment with index **M**.

These compartments are an acceptable simplified model for the different stages in the FDG and glucose pathways. A model for another tracer may need fewer or more compartments.

To analyse the tracer concentration curves with the compartmental model, regions of interest (ROI) are drawn in the image and the mean tracer concentration in the ROI as a function of time is extracted to produce the time-activity curves. In [](#fig:kinemodel) a region is drawn inside the left ventricle to obtain the tracer concentration in the blood. A second region is drawn in the left ventricular wall to obtain the tracer concentration in that region of the heart. The model is then applied to analyse how the concentration in the blood influences the concentration in the tissue.



:::{figure} figs/fig_kinemodel2.pdf
:name: fig:kinemodel2
:align: center
:alt: The time-dependent tracer concentration in the blood and the rate constants in the tissue region determine the evolution of the tissue tracer concentration. The blood interacts with a large amount of tissue. Since the tissue region we study is small, its effect on the blood concentration is negligible.

*The time-dependent tracer concentration in the blood and the rate constants in the tissue region determine the evolution of the tissue tracer concentration. The blood interacts with a large amount of tissue. Since the tissue region we study is small, its effect on the blood concentration is negligible.*
:::



As illustrated in [](#fig:kinemodel2), the analysis must explain how the tissue concentration is determined by the blood concentration and the tissue features. In contrast, the blood concentration is essentially independent of the concentration in the region we study. It is determined by the way the tracer is injected and by the tracer exchange with the entire body. The contribution of the small region we study to the blood concentration is negligible compared to the contribution of the entire body.

(the-rate-constants)=
##### The rate constants

% ---------------------------------

The amount of tracer in a compartment can be specified in several ways: number of molecules, mole, gram or Bq. All these numbers are directly proportional to the absolute number of molecules. If we study a single gram of tissue, the amounts can be expressed in Bq/g, which is the unit of concentration. Remark, though, that these are not tracer concentrations of the compartments, since the gram tissue contains several compartments.

The compartments may exchange tracer molecules with other compartments. It is assumed that this exchange can be described with simple first order rate constants. This means that the amount of tracer traveling away from a compartment is proportional to the amount of tracer in that compartment. The constant of proportionality is called a *rate constant*. For the three compartment model, there are two different types of rate constants. Constant {math}`K_1` is a bit different from {math}`k_2`, {math}`k_3` and {math}`k_4` because the first compartment is a bit different from the other two ([](#fig:kinemodel)).

The amount of tracer going from the blood plasma compartment to the extravascular compartment is

```{math}
\mbox{Tracer}_{P \rightarrow E} = K_1 C_P
```

where {math}`C_P` is the plasma tracer concentration (units: Bq/ml). {math}`K_1` is the product of two factors. The first one is the blood flow {math}`F`, the amount of blood supplied in every second to the gram tissue. {math}`F` has units ml/(s g). The second factor is the extraction fraction {math}`f`, which specifies which fraction of the tracer passing by in {math}`P` is exchanged with the second compartment {math}`E`. Since it is a fraction, {math}`f` has no unit. For some tracers, {math}`f` is almost 1 (e.g. for radioactive water). For other tracers it is 0, which means that the tracer stays in the blood. For FDG it is in between. Consequently, the product {math}`K_1 C_P = F f C_P` has units Bq/(s g) and tells how many Bq are extracted from the blood per second and per gram tissue. {math}`C_P` is a function of the time, {math}`K_1` is not (or more precisely, we assume it stays constant during the scan). Both {math}`K_1` and {math}`C_P` are also a function of position: the situation will be different in different tissue types.

The amount of tracer going from {math}`E` to {math}`M` equals:

```{math}
\mbox{Tracer}_{E \rightarrow M} = k_3 C_E(t),
```

where {math}`C_E` is the total amount of tracer in compartment {math}`E` per gram tissue (units: Bq/g). Constant {math}`k_3` tells which fraction of the available tracer is metabolized in every second, so the unit of {math}`k_3` is 1/s. The physical meaning of {math}`k_2` and {math}`k_4` is similar: they specify the fractional transfer per second.

(the-target-molecule)=
##### The target molecule

% ----------------------------------

The tracer is injected to study the metabolism of a particular molecule. It is assumed that the metabolic process being studied is constant during the measurement, and that the target molecule (glucose in our example) has reached a steady state situation. Steady state means that a dynamic equilibrium has been reached: all concentrations remain constant. Steady state can only be reached with well-designed feedback systems (poor feedback systems oscillate), but it is reasonable to assume that this is the case for metabolic processes in living creatures.

Since FDG and glucose are not identical, their rate constants are not identical. The glucose rate constants will be labeled with the letter {math}`g`. The glucose and FDG amounts are definitely different: glucose is abundantly present and is in steady state condition. FDG is present in extremely low concentrations (pmol) and has not reached steady state since the images are acquired immediately after injection.

The plasma concentration {math}`C_P^g` is supposed to be constant. We can measure it by determining the glucose concentration in the plasma from a venous blood sample. The extravascular glucose amount {math}`C_E^g` is supposed to be constant as well, so the input must equal the output. For glucose, {math}`k_4^g` is very small. Indeed, {math}`k_4^g` corresponds to reversal of the initiated metabolization, which happens only rarely. Setting {math}`k_4^g` to zero we have

```{math}
\frac{d C_E^g}{dt} = 0 = K_1^g C_P^g - (k_2^g + k_3^g) C_E^g.
```

Thus, we can compute the unknown glucose amount {math}`C_E^g` from the known plasma concentration {math}`C_P^g`:

```{math}
C_E^g = \frac{K_1^g}{k_2^g + k_3^g} C_P^g.
```

The glucose metabolization in compartment {math}`M` is proportional to the glucose transport from {math}`E` to {math}`M`. Of course, the glucose metabolites may be transported back to the blood, but we don’t care. We are only interested in glucose. Since it ceases to exist after transport to compartment {math}`M` we ignore all further steps in the metabolic pathway. In our compartment model, it is as if glucose is accumulated in the metabolites compartment. This virtual accumulation rate is the metabolization rate we want to find:

```{math}
\begin{align}
  \frac{d C_M^g}{d t} = k_3^g C_E^g &= 
   \frac{K_1^g k_3^g}{k_2^g + k_3^g} C_P^g.\\
  &= \bar{K^g}  C_P^g. \hspace{2cm} \mbox{$($definition of } \bar{K^g})
\end{align}
```

So if we can find the values of the rate constants, we can compute the glucose metabolization rate. As mentioned before, we cannot compute them via the tracer, since it has different rate constants. However, it can be shown that, due to its similarity, the trapping of FDG is *proportional* to the glucose metabolic rate. The constant of proportionality depends on the tissue type (difference in affinity for both molecules), but not on the tracer concentration. The constant of proportionality is usually called “the lumped constant”, because careful theoretical analysis shows that it is a combination of several constants. So the lumped constant LC is:

```{math}
LC = \frac{\frac{K_1 k_3}{k_2 + k_3}}{\frac{K_1^g k_3^g}{k_2^g + k_3^g}}
  = \frac{\bar{K}}{\bar{K^g}}
```

For the (human) brain (which gets almost all its energy from glucose) and for some other organs, several authors have attempted to measure the lumped constant. The values obtained for brain are around 0.8. This means that the human brain has a slight preference for glucose: if the glucose and FDG concentrations in the blood would be identical, the brain would accumulate only 8 FDG molecules for every 10 glucose molecules. If we had used radioactive glucose instead of deoxyglucose, the tracer and target molecules would have had identical rate constants and the lumped constant would have been 1. But as mentioned before, with glucose as a tracer, the radioactivity would not accumulate in the cells, which would result in poorer PET images.

(the-tracer)=
##### The tracer

% -------------------------

(problem-statement)=
##### Problem statement 

% ''''''''''''''''''''''''''''''

Because the lumped constant is known, we can compute the glucose metabolization rate from the FDG trapping rate. To compute the trapping rate, we must know the FDG rate constants. Since the tracer is not in steady state, the equations will be a bit more difficult than for the target molecule. We can easily derive differential equations for the concentration changes in the second and third compartment:



```{math}
:label: eq:C_E

\frac{dC_E(t)}{dt} = K_1 C_P(t) - (k_2 + k_3) C_E(t)
```



```{math}
:label: eq:C_M

\frac{dC_M(t)}{dt} = k_3 C_E(t)
```



For a cardiac study, we can derive the tracer concentration {math}`C_P(t)` in the blood from the pixel values in the center of the left ventricle or atrium. If the heart is not in the field of view, we can still determine {math}`C_P(t)` by measuring the tracer concentrations in blood samples withdrawn at regular time intervals. As with the SUV computations, this requires cross-calibration of the plasma counter to the PET camera.

The compartments {math}`E` and {math}`M` can only be separated with subcellular resolution, so the PET always measures the sum of both amounts, which we will call {math}`C_I(t)`:

```{math}
C_I(t) = C_E(t) + C_M(t).
```

Consequently, we must combine the equations [](#eq:C_E) and [](#eq:C_M) in order to write {math}`C_I(t)` as a function of {math}`C_P(t)` and the rate constants. This is the operational function. Since {math}`C_I(t)` and {math}`C_P(t)` are known, the only remaining unknown variables will be the rate constants, which are obtained by solving the operational function.

(deriving-the-operational-function)=
##### Deriving the operational function 

% ''''''''''''''''''''''''''''''''''''''''''''

To deal with differential equations, the Laplace transform is a valuable tool. Appendix [](#app:laplace) gives the definition and a short table of the features we need for the problem at hand. The strength of the Laplace transform is that derivatives and integrals with respect to {math}`t` become simple functions of {math}`s`. After transformation, elimination of variables is easy. The result is then back-transformed to the time domain. Laplace transform of [](#eq:C_E) and [](#eq:C_M) results in

```{math}
:label: eq:sc_E

s c_E(s) = K_1 c_P(s) - (k_2 + k_3) c_E(s)
```

```{math}
:label: eq:sc_M

s c_M(s) = k_3 c_E(s)
```

where we have assumed that at time {math}`t=0` (time of injection) all tracer amounts are zero. From [](#eq:sc_E) we find {math}`c_E(s)` as a function of {math}`c_P(s)`. Inserting in [](#eq:sc_M) produces {math}`c_M(s)` as a function of {math}`c_P(s)`.

```{math}
:label: eq:c_I

\begin{align}
  c_E(s) &= \frac{K_1}{s + k_2 + k_3} c_P(s)\\
  c_M(s) &= \frac{K_1 k_3}{s (s + k_2 + k_3)} c_P(s)\\
  c_I(s) &= c_E(s) + c_M(s) \\
         &= \left( \frac{K_1}{s + k_2 + k_3} 
                    + \frac{K_1 k_3}{s (s + k_2 + k_3)}\right) c_P(s)
           
\end{align}
```

The two factors in {math}`s` can be split from the denominator using the equation

```{math}
\frac{a}{x(x + b)} = \frac{a}{b} \left( \frac{1}{x} - \frac{1}{x+b} \right)
```

Applying this to [](#eq:c_I) and rearranging a bit yields:

```{math}
c_I(s) = \frac{K_1 k_2}{(k_2 + k_3)} \frac{c_P(s)}{(s + k_2 + k_3)} + 
           \frac{K_1 k_3}{(k_2 + k_3)} \frac{c_P(s)}{s}
```

Applying the inverse Laplace transform is now straightforward (see appendix [](#app:laplace)) and produces the operational function:

```{math}
:label: eq:3comp_ci

C_I(t) = \frac{K_1 k_2}{k_2 + k_3} \int_0^t C_P(u) e^{-(k_2 + k_3)(t - u)}du
         + \frac{K_1 k_3}{k_2 + k_3} \int_0^t C_P(u) du.
```

:::{figure} figs/fig_3comp_ci.pdf
:name: fig:3comp_ci
:align: center
:alt: The tracer amount C_I(t) and its two terms when C_P(t) is a step function (equation (%s)).

*The tracer amount {math}`C_I(t)` and its two terms when {math}`C_P(t)` is a step function (equation [](#eq:3comp_ci)).*
:::



[](#fig:3comp_ci) plots {math}`C_I` and the two terms of equation [](#eq:3comp_ci) for the case when {math}`C_P(t)` is a step function. {math}`C_P(t)` is never a step function, but the plot provides interesting information. The first term of [](#eq:3comp_ci) represents tracer molecules that leave the vascular space, stay a while in compartment {math}`E` and then return back to the blood. As soon as the tracer is present in the blood, this component starts to grow until it reaches a maximum. When {math}`C_P(t)` becomes zero again, the component gradually decreases towards zero. This first term follows the input, but with some delay (CI{sub}`1`(t) in [](#fig:3comp_ci)).

The second term of [](#eq:3comp_ci) represent tracer molecules that enter compartment {math}`E` and will never leave (CI{sub}`2`(t) 
in [](#fig:3comp_ci)). Eventually, they will be trapped in compartment {math}`M`. Note that the first term is not equal to but smaller than {math}`C_E(t)`. The reason is that part of the molecules in {math}`E` will not return to the blood but end up in {math}`M`. It is easy to compute which fraction of {math}`C_E(t)` is described by the first term of [](#eq:3comp_ci). (The rest of {math}`C_E(t)` and {math}`C_M(t)` correspond to the second term of [](#eq:3comp_ci)). This is left as an exercise to the reader.

(impulse-response)=
##### Impulse response 

% '''''''''''''''''''''''''''''

Equation [](#eq:3comp_ci) can be rewritten as

```{math}
C_I(t) = \frac{K_1}{k_2 + k_3} \int_0^t C_P(u) \left(
       k_2 \; e^{-(k_2 + k_3)(t - u)} + k_3 \right) du.
```

This is a convolution of the input function with the factor in brackets, showing that that factor is the impulse response function. To illustrate this, we simply compute the response to an impulse, by replacing {math}`C_p(u)` with a Dirac impulse at time ξ:

```{math}
\begin{align}
  C_I(t) &= \frac{K_1}{k_2 + k_3} \int_0^t \delta(u-\xi) \left(
                k_2 \; e^{-(k_2 + k_3)(t - u)} + k_3 \right) du\\
   &= \frac{K_1}{k_2 + k_3} \left( k_2 \; e^{-(k_2 + k_3)(t - \xi)} +
                k_3 \right).
\end{align}
```

(alternative-derivation-avoiding-the-laplace-transform)=
##### Alternative derivation, avoiding the Laplace transform 

% '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The same result [](#eq:3comp_ci) can be obtained with the method of variation of parameters. For simplicity, we set {math}`\beta = k_2 + k_3`, rewriting equation [](#eq:C_E) as follows

```{math}
:label: eq:vp1

\frac{dC_E(t)}{dt}  =  K_1 C_P(t) - \beta C_E(t).
```

First, we solve the corresponding homogeneous equation, obtained by dropping the terms independent of {math}`C_E(t)`:

```{math}
\frac{dC_E(t)}{dt}  =  - \beta C_E(t).
```

The solution is {math}`C_E(t) = A e^{-\beta t}`. Now we assume that the solution to [](#eq:vp1) is similar, except that the constant {math}`A` must be replaced by a function of {math}`t`: {math}`C_E(t) = A(t) \; e^{-\beta
t}`. Inserting this in [](#eq:vp1) we obtain:

```{math}
:label: eq:vp2

\begin{align}
   \frac{d ( A(t) \; e^{-\beta t})}{dt} 
             &=  K_1 C_P(t) - \beta A(t) \; e^{-\beta t}\\
 = \hspace{5mm} 
   \frac{d A(t)}{dt} \; e^{-\beta t} - \beta A(t) e^{-\beta t} 
              &= K_1 C_P(t) - \beta A(t) \; e^{-\beta t}\\
\Leftrightarrow  \hspace{5mm} 
   \frac{d A(t)}{dt} \; e^{-\beta t} &= K_1 C_P(t)\\
\Leftrightarrow  \hspace{5mm} 
   A(t) &= K_1 \int_0^t C_P(u) e^{\beta u} du\\
\Leftrightarrow  \hspace{5mm} 
   C_E(t) = A(t)  \; e^{-\beta t}
      &= K_1 \int_0^t C_P(u) e^{- \beta (t -u)} du 
\end{align}
```



Having solved the equation for the first tissue compartment, we can use {math}`C_E(t)` to find the activity in the second compartment. We simply insert [](#eq:vp2) in the equation [](#eq:C_M) for {math}`C_M(t)` to obtain:

```{math}
\begin{align}
  \frac{d C_M(t)}{dt} = k_3 C_E(t) 
    &= K_1 k_3 \int_0^t C_P(u) e^{- \beta (t -u)} du \nonumber\\
    &= K_1 k_3 \; e^{- \beta t} \; \int_0^t C_P(u) e^{\beta u} du
\end{align}
```

and therefore

```{math}
:label: eq:vp3

C_M(t) = K_1 k_3 \; \int_0^t d\xi \; e^{-\beta \xi} 
       \int_0^\xi  C_P(u) e^{\beta u} du.
```

This is the integral of an integral, which may seem somewhat intimidating at first. However, it can be simplified using integration by parts. If you are unfamiliar with that trick, you can easily derive it by noting that the integral of the derivative of the product of two functions {math}`f(t)` and {math}`g(t)` equals:

```{math}
f(t) g(t) - f(0) g(0) = \int_0^t \frac{d ((f(\xi) g(\xi))}{d\xi} d\xi
 = \int_0^t \frac{d f(\xi)}{d\xi} g(\xi) d\xi 
   +  \int_0^t f(\xi) \frac{d g(\xi)}{d\xi} d\xi
```

And therefore we can write

```{math}
:label: eq:vptrick

\int_0^t \frac{d f(\xi)}{d\xi} g(\xi) d\xi = f(t) g(t) - f(0) g(0)
        - \int_0^t f(\xi) \frac{d g(\xi)}{d\xi} d\xi
```

We apply this trick to get rid of the inner integral in [](#eq:vp3) as follows:

```{math}
\begin{align}
  f(\xi) &= -\frac{e^{-\beta \xi}}{\beta}\\
  \frac{d f(\xi)}{d\xi} &= e^{-\beta\xi}\\
  g(\xi) &= \int_0^\xi  C_P(u) e^{\beta u} du\\
  \frac{d g(\xi)}{d\xi} &= C_P(\xi) e^{\beta \xi}
\end{align}
```

With these definitions, the left hand side of [](#eq:vptrick) is equal to [](#eq:vp3). Note that {math}`g(0) = 0` here, which makes things slightly simpler. The trick converts [](#eq:vp3) into:

```{math}
:label: eq:vp4

\begin{align}
 C_M(t) &= K_1 k_3 \left( 
  -\frac{e^{-\beta t}}{\beta} \int_0^t  C_P(u) e^{\beta u} du
  - \int_0^t (-\frac{e^{-\beta u}}{\beta}) C_P(u) e^{\beta u} du
   \right) \nonumber \\
 &= \frac{K_1 k_3}{k_2 + k_3} \left(
   - \int_0^t C_P(u) e^{-(k_2 + k_3) (t -u)} du + \int_0^t C_P(u) du
 \right) 
\end{align}
```

where we have replaced β again with {math}`k_2 + k_3`. Finally, to obtain {math}`C_I(t) = C_E(t) + C_M(t)` 
we sum [](#eq:vp2) and [](#eq:vp4):

```{math}
\begin{align}
C_I(t) &= (K_1 - \frac{K_1 k_3}{k_2 + k_3}) 
            \int_0^t C_P(u) e^{- (k_2 + k_3) (t -u)} du \;\;
       + \;\; \frac{K_1 k_3}{k_2 + k_3} \int_0^t C_P(u) du \nonumber\\
 &=
  \frac{K_1 k_2}{k_2 + k_3} \int_0^t C_P(u) e^{- (k_2 + k_3) (t -u)} du
    \;\; + \;\;
   \frac{K_1 k_3}{k_2 + k_3} \int_0^t C_P(u) du,
\end{align}
```

which is identical to equation [](#eq:3comp_ci).

(computing-the-rate-constants-with-non-linear-regression)=
##### Computing the rate constants with non-linear regression 

% '''''''''''''''''''''''''''''''''''''''''

At this point, we have the operational function relating {math}`C_I(t)` to {math}`C_p(t)` and the rate constants. We also know {math}`C_p(t)` and {math}`C_I(t)`, at least in several sample points (dynamic studies have typically 20 to 40 frames). Every sample point is an equation, so we actually have a few tens of equations and 3 unknowns. Because of noise and the fact that the operational function is only an approximation, there is probably no exact solution. The problem is very similar to the reconstruction problem, which has been solved with the maximum likelihood approach. The same will be done here. If the likelihood is assumed to be Gaussian, maximum likelihood becomes weighted least squares.

With this approach, we start with an arbitrary set of rate constants. It is recommended to start close to the solution if possible, because the likelihood function may have local maxima. Typically the rate constants obtained in healthy volunteers are used as a start. With these rate constants and the known input function {math}`C_p(t)`, we can compute the expected value of {math}`C_I(t)`. The computed curve will be diff erent from the measured one. Based on this difference, the non-linear regression algorithm will improve the values of the rate constants, until the sum of weighted squared differences is minimal. It is always useful to plot both the measured and computed curves {math}`C_I(t)` to verify that the fit has succeeded, since there is small chance that the solution corresponds to an unacceptable local minimum. In that case, the process must be repeated, starting from a different set of rate constant values. The tissue curve in [](#fig:kinemodel) is the result of non-linear regression. The fit was successful, since the curve is close to the measured values.

The glucose consumption can now be computed as

```{math}
:label: eq:glucmet

\mbox{glucose consumption} =
     \frac{1}{\mbox{LC}} \frac{K_1 k_3}{k_2 + k_3} C_P^g
     = \frac{\bar{K}}{\mbox{LC}} C_P^g
```

Non-linear regression programs often provide an estimate of the confidence intervals or standard deviations on the fitted parameters. These can be very informative. Depending on the shape of the curves, the noise on the data and the mathematics on the model, the accuracy of the fitted parameters can be very poor. However, the errors on the parameters are correlated such that the accuracy on {math}`\bar{K}` is better than the accuracy on the individual rate constants.

(computing-the-trapping-rate-with-linear-regression)=
##### Computing the trapping rate with linear regression 

% '''''''''''''''''''''''''''''''''''''''''

By introducing a small approximation, the computation of the glucose consumption can be simplified. [](#fig:kinemodel) shows a typical blood function. The last part of the curve is always very smooth. As a result, the first term of [](#eq:3comp_ci) nicely follows the shape of {math}`C_p(t)`. Stated otherwise, {math}`C_p(u)` changes very little over the range where {math}`e^{-(k_2 + k_3)(t - u)}` is significantly different from zero. Thus, we can put {math}`C_p(t)` in front of the integral sign. Since {math}`t` is large relative to the decay time of the exponential, we can set {math}`t` to ∞:

```{math}
\begin{align}
\int_0^t C_P(u) e^{-(k_2 + k_3)(t - u)}du
  &\simeq  C_P(t) \int_0^t  e^{-(k_2 + k_3)(t - u)}du\\
  &=       C_P(t) \int_0^t  e^{-(k_2 + k_3)u}du\\
  &\simeq  C_P(t) \int_0^\infty  e^{-(k_2 + k_3)u}du\\
  &= \frac{C_p(t)}{k_2 + k_3}
\end{align}
```

The operational function then becomes:

```{math}
C_I(t) \simeq \frac{K_1 k_3}{k_2 + k_3} \int_0^t C_P(u) du + 
  \frac{K_1 k_2}{(k_2 + k_3)^2} C_P(t).
```

Now both sides are divided by {math}`C_p(t)`:

```{math}
:label: eq:patlak

\frac{C_I(t)}{C_P(t)} \simeq 
    \frac{K_1 k_3}{k_2 + k_3} \frac{\int_0^t C_P(u) du}{C_P(t)} + 
  \frac{K_1 k_2}{(k_2 + k_3)^2}.
```

Equation [](#eq:patlak) says that {math}`C_I(t)/C_P(t)` is a linear function of {math}`\int_0^t C_P(u) du / C_P(t)`, at least for large values of {math}`t`. We can ignore the constants, all we need is the slope of the straight curve. This can be obtained with simple linear regression. For linear regression no iterations are required, there is a closed form expression, so this solution is orders of magnitudes faster to compute than the previous one.

The integral {math}`\int_0^t C_P(u) du / C_P(t)` has the unit of time. If {math}`C_P(t)` would be a constant, the integral simply equals {math}`t`. It can be regarded as a correction, required because {math}`C_P(t)` is not constant but slowly varying. As shown in 
[](#fig:3comp_ci), when {math}`C_P(t)` is constant, {math}`C_I(t)` has a linear and a constant term. 
Equation [](#eq:3comp_ci) confirms that the slope of the linear term is indeed {math}`\bar{K}`. A potential disadvantage is that the values of the rate constants are not computed.

(image-quality)=
### Image quality

% ======================

It is extremely difficult to give a useful definition of image quality. As a result, it is even more difficult to measure it. Consequently, often debatable measures of image quality are being used. This is probably unavoidable, but it is good to be fully aware about the limitations.

(subjective-evaluation)=
#### Subjective evaluation

% ---------------------------------

A very bad but very popular way to assess the performance of some new method is to display the image produced by the new method together with the image produced in the classical way, and see if the new image is “better”. In many cases, you cannot see if it is better. You can see that you like it better for some reason, but that does not guarantee that it will lead to an improvement in the process (e.g. making a diagnosis) to which the image is supposed to contribute.

As an example, a study has been carried out to determine the effect of 2D versus 3D PET imaging on the diagnosis of a particular disease, and for a particular PET system. In addition, the physicians were asked to tell what images they preferred. The physicians preferred the 3D images because they look nicer, but their diagnosis was statistically significantly better on the 2D images (because scatter contribution was lower).

It is not forbidden to look at an image (in fact, it is usually a good idea to look at it carefully), but it is important not to jump to a conclusion.

(task-dependent-evaluation)=
#### Task dependent evaluation

% -------------------------------------

The best way to find out if an image is good, is to use it as planned and check if the results are good. Consequently, if a new image generation or processing technique is introduced, it has to be compared very carefully to the classical method on a number of clinical cases. Evaluation must be done blindly: if the observer remembers the image from the first method when scoring the image from the second method, the score is no longer objective. If possible the observer should not even be aware of the method, in order to exclude the influence of possible prejudice about the methods.

(continuous-and-digital)=
#### Continuous and digital

% ----------------------------------

Intuitively, the best image is the one closest to the truth. But in emission tomography, the truth is a continuous tracer distribution, while the image is digital. It is not always straightforward to define how a portion of a continuous curve can be best approximated as a single value. The problem becomes particularly difficult if the images to be compared use a different sampling grid (shifted points or different sampling density). So if possible, make sure that the sampling is identical.

(bias-and-variance)=
#### Bias and variance

% -----------------------------

Assume that we have a reference image e.g. in a simulation experiment. In this case, we know the true image, and in most cases it is even digital. Then we can compare the difference between the true image and the image to be evaluated. A popular approach is to compute the mean squared difference:

```{math}
\mbox{mean squared difference} = \frac{1}{J} \sum_{j=1}^J (\lambda_j - r_j)^2,
```

where {math}`\lambda_j` and {math}`r_j` are the image and the reference image respectively. This approach has two problems. First, it assumes that all pixels are equally important, which is almost never true. Second, it combines systematic (bias) and random (variance) deviations. It is better to separate the two, because they behave very differently. This is illustrated in [](#fig:bias_var). Suppose that a block wave was measured with two different methods A and B, producing the noisy curves shown at the top row. Measurement A is noisier, and its sum of squared differences with the true wave is twice as large as that of measurement B. If we know that we are measuring a block wave, we know that a bit of smoothing is probably useful. The bottom row shows the result of smoothing. Now measurement A is clearly superior. The reason is that the error in the measurement contains both bias and variance. Smoothing reduces the variance, but increases the bias. In this example the true wave is smooth, so variance is strongly reduced by smoothing, while the bias only increases near the edges of the wave. If we keep on smoothing, the entire wave will converge to its mean value; then there is no variance but huge bias. Bias and variance of a sample (pixel) {math}`j` can be defined as follows:

```{math}
\begin{align}
  \mbox{bias}_j     &= E(\lambda_j - r_j)\\
  \mbox{variance}_j &= E\left((\lambda_j - E(\lambda_j))^2 \right),
\end{align}
```

where {math}`E(x)` is the expectation of {math}`x`. Variance can be directly computed from repeated independent measurements. If the true data happen to be smooth and if the measurement has good resolution, neighboring samples can be regarded as independent measurements. Bias can only be computed if the true value is known.

In many cases, there is the possibility to trade in variance for bias by smoothing or imposing some constraints. Consequently, if images are compared, bias and variance must be separated. If an image has better bias for the same variance, it is probably a “better” image. If an image has larger bias and lower variance when compared to another image, the comparison is meaningless.

:::{figure} figs/fig_bias_var.pdf
:name: fig:bias_var
:align: center
:alt: Top: a simulated true block wave and two measurements A and B with different noise distributions. Bottom: the true block wave and the same measurements, smoothed with a simple rectangular smoothing kernel.

*Top: a simulated true block wave and two measurements A and B with different noise distributions. Bottom: the true block wave and the same measurements, smoothed with a simple rectangular smoothing kernel.*
:::

(evaluating-a-new-algorithm)=
#### Evaluating a new algorithm

% -----------------------------------

A good way to evaluate a new image processing algorithm (e.g. an algorithm for image reconstruction, for image segmentation, for registration of images from different modalities) is to apply the following sequence:

1.  evaluation on computed, simulated data

2.  evaluation on phantom data

3.  (evaluation on animal experiments)

4.  evaluation on patient data

This sequence is in order of increasing complexity and decreasing controllability. Tests on patient data are required to show that the method can be used. However, if such a test fails it is usually very difficult to find out why. To find the problem, simple and controllable data are required. Moreover, since the true solution is often not known in the case of patient data, it is possible that failure of the method remains undetected. Consequently, there is no gain in trying to skip one or a few stages, and with a bit of bad luck it can have serious consequences.

Evaluation on simulation has the following important advantages:

*   The truth is known, comparing the result to the true answer is simple. This approach is also very useful for finding bugs in the algorithm or its implementation.

*   Data can be generated in large numbers, sampling a predefined distribution. This enables direct quantitative analysis of bias and variance.

*   Complexity can be gradually increased by making the simulations more realistic, to analyze the response to various physical phenomena (noise, attenuation, scatter, patient motion …).

*   A nice thing about emission tomography is that it is relatively easy to make realistic simulations. In addition, many research groups are willing to share simulation code.

*   It is possible to produce simulations which are sufficiently realistic to have them diagnosed by the nuclear medicine physicians. Since the correct diagnosis is known, this allows evaluation of the effect of the new method on the final diagnosis.

When the method survives complex simulations it is time to do phantom experiments. Phantom experiments are useful because the true system is always different from even a very realistic simulation. If the simulation phase has been done carefully, phantom experiments are not likely to cause much trouble.

A possible intermediate stage is the use of animal experiments, which can be required for the evaluation of very delicate image processing techniques (e.g. preparing stereotactic operations). Since the animal can be sacrificed, it is possible, at least to some extent, to figure out what result the method should have produced.

The final stage is the evaluation on patient data, and comparing the output of the new method to that of the classical method. As mentioned before, not all failures will be detected since the correct answer may not be known.

+++
(chap:biol)=
## Biological effects of radiation

Radiation which interacts with electrons can affect chemical bonds in DNA, and as a result, cause damage to living tissues. The probability that an elementary particle will cause an adverse ionisation is proportional to the energy of the particle deposited in the tissue. In addition, the damage done per unit energy depends on the type of particle.

In diagnostic nuclear medicine, the aim is of course to obtain diagnostic images without or with minimum damage to the patient. Consequently, the amount of activity administered to the patient should be as low as reasonably achievable (ALARA). “Reasonably achievable” means that the radiation emitted by the tracer should still be sufficient to make valuable clinical images.

The amount of radiation deposited in an object is expressed in gray (Gy). A dose of 1 gray is defined as the deposition of 1 joule per kg absorber:

```{math}
1 Gy = 1 \frac{J}{kg}.
```

To quantify (at least approximately) the amount of damage done to living tissue, the influence of the particle type must be included as well. E.g. it turns out that 1 J deposited by neutrons does more damage than the same energy deposited by photons. To take this effect into account, a quality factor {math}`Q` is introduced. Multiplication with the quality factor converts the dose into the dose equivalent. Quality factors are given in [](#tab:qualfactor).



:::{list-table} Quality factor converting dose in dose equivalent (ICRP2007).
:header-rows: 0
:name: tab:qualfactor
:align: center

*   *   Radiation

    *   Q

*   *   X-ray, 

        γ

        -ray,

    *

*   *   electrons, positrons

    *   1

*   *   protons

    *   2

*   *   neutrons

    *   2.5 … 22, depending on energy

*   *   α

        -particals

    *   20
:::

The dose equivalent is expressed in Sv (sievert). Since {math}`Q = 1` for photons, electrons and positrons, we have 1 mSv per mGy in diagnostic nuclear medicine. The natural background radiation is about 2 mSv per year, or about 0.2 μSv per hour.\


The older units for radiation dose and dose equivalent are rad and rem:

```{math}
\begin{align}
  \mbox{1 Gy} &= \mbox{100 rad}\\
  \mbox{1 Sv} &= \mbox{100 rem}
\end{align}
```

When the dose to every organ is computed, one can in addition compute an “effective dose”, which is a weighted sum of organ doses. The weights are introduced because damage in one organ is more dangerous than damage in another organ. The most sensitive organs are the gonads (weight about 0.25), the breast, the bone marrow and the lungs (weight about 0.15), the thyroid and the bones (weight about 0.05), see [](#tab:effdose). The sum of all the weights is 1. The weighted average produces a single value in mSv. The risk of death due to tumor induction is about 5% per “effective Sv” according to report ICRP-60 (International Commission on Radiological Protection (http://www.icrp.org)), but it is of course very dependent upon age (e.g. 14% for children under 10). Research in this field is not finished and the tables and weighting coefficients are adapted every now and then.

:::{list-table} Organ weight factors to compute the effective dose (ICRP 103, 2007).
:header-rows: 0
:name: tab:effdose
:align: center

*   *   organ

    *   weight

    *   total

*   *   red marrow, colon, lungs, stomach, breast

    *   0.12

    *   0.60

*   *   gonads

    *   0.08

    *   0.08

*   *   bladder, liver, esophagus, thyroid

    *   0.04

    *   0.16

*   *   brain, skin, salivary glands, bone surfaces

    *   0.01

    *   0.04

*   *   remainder (adrenals, extrathoracic region,

    *

    *

*   *   gallbladder, heart, kidneys, lymphatic nodes,

    *   0.00923

    *   0.12

*   *   muscle, oral mucosa, pancreas, prostate,

    *

    *

*   *   small intestine, spleen, thymus, uterus/cervix)

    *

    *

*   *   total

    *

    *   1
:::

To obtain the dose equivalent delivered by one organ {math}`A` to another organ {math}`B` (or to itself, in which case {math}`A = B`), we have to make the following computation:

```{math}
:label: eq:DE

\mbox{DE} = \sum_i Q_i \;\times\; N_{iA} \;\times\; p_i(A \rightarrow B) 
               \;\times\; E_i \;/\; M_B,
```

DE

:   is the dose equivalent;

{math}`i`

:   denotes a particular emission. Often, multiple photons or particles are emitted during a single radioactive event, and we have to compute the total dose equivalent by summing all contributions;

{math}`Q_i`

:   is the quality factor for emission 

    {math}`i`

    ;

{math}`N_{iA}`

:   is the total number of particles 

    {math}`i`

     emitted in organ 

    {math}`A`

    ;

{math}`p_i(A \rightarrow B)`

:   is the probability that a particle 

    {math}`i`

     emitted in organ 

    {math}`A`

     will deposit (part of) its energy in organ 

    {math}`B`

    ;

{math}`E_i`

:   is the (average) energy that is carried by the particles 

    {math}`i`

     and that can be released in the tissue. For electrons and positrons, this is their kinetic energy. For photons, it is all of their energy.

{math}`M_B`

:   is the mass of organ 

    {math}`B`

    .

In the following paragraphs, we will discuss these factors in more detail, and illustrate the procedure with two examples.

(the-particle-i)=
### The particle {math}`i`

% =========================

The ideal tracer for single photon emission would emit exactly one photon in every radioactive event. However, most realistic tracers have a more complex behaviour. Some of them emit several photons at different energies and in different quantities. For example, Iodine-123 has several different ways of decaying (via electron capture) from {math}`^{123}_{53}`I into {math}`^{123}_{52}`Te. Each decay scheme produces its own set of photons. Most of these schemes share an energy jump of 159 keV, and the mean number of 159 keV photons emitted per desintegration equals 0.836. In some of the decay schemes, there is an internal conversion electron with an average energy of 127 keV, that comes with a probability of 0.134 per desintegration. In total, {math}`^{123}_{53}`I uses combinations of 14 different gamma rays, 5 x-rays, 3 internal conversion electrons and 5 Auger electrons to get rid of its excess energy. Each of those has its own probability. In principle, we need to include them all, but it usually suffices to include only the few dominating emissions.

(the-total-number-of-particles-n-ia)=
### The total number of particles {math}`N_{iA}`

% =========================

The number of particles emitted per s changes with time. Due to the finite half life, the radioactivity decays exponentially 
(see equation [](#eq:decay)). Moreover, the distribution of the tracer molecule in the body is determined by the metabolism, and it changes continuously from the time of injection. Often, the tracer molecule is metabolized: the molecule is cut in pieces or transformed into another one. In those cases, the radioactive atoms may follow one or several metabolic pathways. As a result, it is often very difficult or simply impossible to accurately predict the amount of radioactivity in every organ as a function of time. When a new tracer is introduced, the typical time-activity curves are mostly determined by repeated emission scans in a group of subjects.

Assuming that we know the amount of radioactivity as a function of time, we can compute the total number of particles as

```{math}
N_{iA} =  \int_0^{\infty} n_{iA}(t) dt,
```

where {math}`n_{iA}(t)` is the number of particles emitted per s at time {math}`t`. For some applications, it is reasonable to assume that the tracer behaviour is dominated by its physical decay. Then we have that

```{math}
:label: eq:biol_decay

\begin{align}
  N_{iA} &= n_{iA}(0) \int_0^{\infty} e^{- \ln(2) \frac{t}{t_{1/2}}} dt \nonumber\\
         &= n_{iA}(0) \frac{t_{1/2}}{\ln(2)}. 
\end{align}
```

Here {math}`n_{iA}(0)` is the number of particles or photons emitted per s at time 0, and {math}`t_{1/2}` is the half life. For a source of 1 MBq at time 0, {math}`n_{iA}(0) = 10^6` per s, since 1 Bq is defined as 1 emission per s.

Often, the tracer is metabolized and sent to the bladder, which implies a decrease of the tracer concentration in most other organs. Therefore, the amount of radioactivity decreases faster than predicted by [](#eq:biol_decay) in these organs. One way to approximate the combined effect of metabolism and physical decay could be to replace the physical half life with a shorter, effective half life in [](#eq:biol_decay). In other cases, it may be necessary to integrate the measured time activity curves numerically.

(the-probability-p-i-a-rightarrow-b)=
### The probability {math}`p_i(A \rightarrow B)`

% =========================

This probability depends on the geometric configuration of the organs and on the attenuation coefficients. The situation is very different for photons on the one hand and electrons and positrons on the other. As illustrated by [](#tab:positron_length) for positrons, the mean path length of an electron and positron in tissue is very short, even for relatively high kinetic energies. Consequently, for these particles, {math}`p_i(A \rightarrow A)` is close to 1, while {math}`p_i(A \rightarrow B)` is negligible for different organs {math}`A` and {math}`B`. The probability that a photon travels from A to B depends on the attenuation along that trajectory. Similarly the probability that it deposits all or a part of its energy in B depends on the attenuation coefficient in organ B.

(the-energy-e-i)=
### The energy {math}`E_i`

% =========================

As mentioned above, {math}`E_i` denotes kinetic energy for electrons and positrons, and the total amount of energy for photons. This energy is usually given in electronvolt. However, to compute the result in Gy, we need the energy in joule. The eV is defined as the amount of energy acquired by an electron if it is accelerated in an electrical field of 1 V. Because joule equals coulomb times volt, we have that

```{math}
1 \mbox{eV} = 1.6 \times 10^{-19} \mbox{coulomb} \times \mbox{volt}
             = 1.6 \times 10^{-19} \mbox{J}.
```

(example-1-single-photon-emission)=
### Example 1: single photon emission

% =========================

Consider the configuration shown in [](#fig:biol-singlephoton). Assume that the point source in the left box contains 1 MBq of the isotope {sup}`123`I. As discussed before, this isotope has a very busy decay scheme, but we will assume that we can ignore all emissions except the following two:

1.  Gamma radiation of 159 keV, with an abundance of 0.84,

2.  Conversion electron of 127 keV, with an abundance of 0.13.

&#x20;The half life of {sup}`123`I is 13.0 hours. The boxes are made of plastic or something like that, with an attenuation coefficient of 0.15 cm{sup}`-1` for photons with energy of 159 keV. The density of the boxes is 1 kg/liter. The boxes are hanging motionless in air, the attenuation of air is negligible. Our task is to estimate the dose that both boxes will receive if we don’t touch this configuration for a few days.





:::{figure} figs/fig_biol_singlephoton.pdf
:name: fig:biol-singlephoton
:align: center
:alt: Two objects, one with a radioactive source in the center. The size of the right box is 2 \times 2 \times 4 cm^3.

*Two objects, one with a radioactive source in the center. The size of the right box is 2 × 2 × 4 cm{sup}`3`*.
:::

We are going to need the mass of the boxes. For the left box we have:

```{math}
W_{\mbox{left}} = \frac{4}{3} \pi R^3 \; \times \; 1 \frac{\mbox{kg}}{\mbox{dm}^3}
      = 0.034 \;\mbox{kg},
```

and for the right box:

```{math}
W_{\mbox{right}} = d^2 L\; \times \; 1 \frac{\mbox{kg}}{\mbox{dm}^3}
      = 0.016 \;\mbox{kg}.
```

Because a few days lasts several half lifes, a good approximation is to integrate until infinity using equation [](#eq:biol_decay). Consequently, the total number of desintegrations is estimated as

```{math}
N = 1 \mbox{MBq} \times \frac{13\ \mbox{hours}}{\ln(2)} 
    \times 3600 \frac{s}{\mbox{hour}}
    = 6.75 \times 10^{10}.
```

&#x20;This number must be multiplied with the mean number of particles per desintegration:



*   number of photons is 0.84 N = 5.67 × 10{sup}`10`\


*   number of electrons is 0.13 N = 8.78 × 10{sup}`9`



The radius of the left box is large compared with the mean path length of the electrons, so the box receives all of their energy: {math}`p_{\beta^-}(\mbox{leftbox} \rightarrow \mbox{leftbox}) = 1`. Thus, the dose of the left box due to the electrons is:

```{math}
\mbox{dose}(\beta^-,\mbox{leftbox}) = 8.78 \times 10^9 \; \times \; 
         127000 \ \mbox{eV} \;
    \times \frac{1.6 \times 10^{-19} \ \mbox{J}}{\mbox{eV}} \times 
          \frac{1}{0.034 \ \mbox{kg}}
      = 5 \mbox{mGy}.
```

For the photons, the situation is slightly more complicated, because not all of them will deposit their energy in the box. Because the box is spherical and the point source is in the center, the amount of attenuating material seen by a photon is the same for every direction. With equation [](#eq:spectatten) we can compute the probability that a photon will escape without interaction:

```{math}
p_{\mbox{escape}} = e^{- \int_0^R \mu dr} = e^{- \mu R} 
     = \exp(- \frac{0.15}{\mbox{cm}} \; \times \; 2 \ \mbox{cm}) = 0.74.
```

Thus, there is a chance of 1 - 0.74 = 0.26 that a photon will interact. This interaction could be a Compton event, in which only a part of the photon energy will be absorbed by the box. This complicates the computations considerably. To avoid the problem, we will go for a simple but pessimistic solution: we simply assume that every interaction results in a complete absorption of the photon. That yields for the photon dose to the left box:

```{math}
\mbox{dose}(\gamma, \mbox{leftbox}) 
   =  5.67 \times 10^{10} \; \times  159\ \mbox{keV} 
    \times \frac{1.6 \times 10^{-19} \ \mbox{J}}{\mbox{eV}}
    \times \frac{1}{0.034 \ \mbox{kg}} \times \; 0.26 = 11 \mbox{mGy}.
```

So the total dose to the left box equals about 16 mGy.

For the right box, we can ignore the electrons, they cannot get out of the left box. We already know that a fraction of 0.74 of the photons escapes the left box. Now, we still have to calculate which of those will interact with the right box. We first estimate the fraction traveling along a direction that will bring it into the right box. When observed from the point source position, the right box occupies a solid angle of approximately {math}`d^2 / (D +
R)^2`. The total solid angle equals {math}`4 \pi`, so the fraction of photons travelling towards the right box equals

```{math}
p_{\mbox{geometry}} = \frac{d^2}{4 \pi (D + R)^2} = 0.0022.
```

These photons are travelling approximately horizontally, so most of them are now facing 4 cm of attenuating material. Applying the same pessimistic approach as above yields the fraction that interacts with the material of the right box:

```{math}
p_{\mbox{attenuation}} = 1 - e^{- \mu L} = 0.45.
```

Combining all factors yields then number of photons interacting with the right box:

```{math}
5.67 \times 10^{10} \times 0.74 \times 0.0022 \times 0.45 = 4.2 \times 10^7.
```

Finally, multiplying with the energy and dividing by the mass yields:

```{math}
\mbox{dose}(\gamma, \mbox{rightbox}) = 4.2 \times 10^7\ \times 159\ \mbox{keV}
  \times \frac{1.6 \times 10^{-19} \ \mbox{J}}{\mbox{eV}}
   \times \frac{1}{ 0.016 \ \mbox{kg}}
   = 0.067 \mbox{mGy}.
```

This is much less than the dose of the left box. The right box is protected by its distance from the source!

(example-2-positron-emission-tomography)=
### Example 2: positron emission tomography

% =========================

Here, we study the same setup of [](#fig:biol-singlephoton), but now with a point source containing 1 MBq of {sup}`18`F. This is a positron emitter. From [](#tab:positron_length), we know that the average kinetic energy of the positron is 250 keV. Most of this energy is dissipated in the tissue before the positron annihilates. Thus, there are three contributions to the dose of the left box: the positron and the two photons. The right box can at most be hit by one of the photons.



We assume that in every desintegration, exactly one positron is produced, which annihilates with an electron into two 511 keV. At 511 keV, the attenuation of the boxes is 0.095 cm{sup}`-1`. The half life of {sup}`18`F is 109 minutes.

The total number of desintegrations is

```{math}
N = 1 \mbox{MBq} \times \frac{109\ \mbox{min}}{\ln(2)} \times 60
    \frac{s}{\mbox{min}} = 9.44 \times 10^9.
```

Proceeding in the same way as above, we find the following doses:

```{math}
\begin{align}
\mbox{dose}(\beta^+,\mbox{leftbox}) &= 9.44 \times 10^9 \; \times \; 250000
    \ \mbox{eV} \; \times \frac{1.6 \times 10^{-19} \ \mbox{J}}{\mbox{eV}}
        \times \frac{1}{0.034 \ \mbox{kg}}  \nonumber\\
     &= 11 \mbox{mGy}.  \\
\mbox{dose}(\gamma, \mbox{leftbox}) &= 9.44 \times 10^9 \; \times
    \; 511000 \ \mbox{eV} \;
    \times \frac{1.6 \times 10^{-19} \ \mbox{J}}{\mbox{eV}} \;
     \times \frac{1}{0.034\ \mbox{kg}} \times \; 0.17 \nonumber\\
     &= 3.9 \mbox{mGy}.
\end{align}
```

The total dose then equals {math}`\mbox{dose}(\beta^+,\mbox{leftbox}) + 2 \;
\mbox{dose}(\gamma, \mbox{leftbox})` = 18.8 mGy.

For the right box, we first estimate the number of interacting photons (remember that there are two photons per desintegration):

```{math}
2N \ p_{\mbox{escape}}\ p_{\mbox{geometry}}\ p_{\mbox{attenuation}}
   = 2N \times 0.83 \times 0.0022 \times 0.32 = 1.09 \times 10^7.
```

And for the dose to the right box we get:

```{math}
\mbox{dose}(\gamma, \mbox{rightbox}) = 1.09 \times 10^7\; \times \; 511000 \ \mbox{eV} \;
  \times \frac{1.6 \times 10^{-19} \ \mbox{J}}{\mbox{eV}}  \times \frac{1}{0.016\ \mbox{kg}}
   = 0.056 \mbox{mGy}.
```

(internal-dosimetry-calculations)=
### Internal dosimetry calculations

% =========================

Internal dosimetry calculations use the same principle as in the examples above to compute the dosage to every organ. Because there are many organs, and because the activity in any organ contributes to the dose in any other organ, the computations are complex and tedious. This is one of the reasons why dedicated software has been developed. With the fast computers we have today, the calculations can be carried out more accurately. E.g. it is possible to take the effects of Compton scatter into account using Monte Carlo techniques.

Of course, we still have to provide a meaningful input to the software. In principle, we should input the precise anatomy of the patient. Because this is usually not available, this problem is avoided by using a few standard geometries, which model the human anatomy, focussing on the most senstive organs. It follows that the resulting doses should only be considered as estimates, not as accurate numbers.

We also have to provide the tracer concentration as a function of time for all organs. For known tracers, the software may contain typical residence times; for new ones, measurements in humans have to be carried out to estimate the dosimetry.

+++
(radionuclide-therapy-and-dosimetry)=
## Radionuclide therapy and dosimetry

(introduction)=
### Introduction

% %%%%%%%%%%%%%%%%%%%%%

In nuclear medicine, radiopharmaca are mostly used for diagnostic imaging (with SPECT or PET) and activity concentration measurements in samples (with a gamma counter). For that purpose, the radiopharmacon is labeled with a single photon or a positron emitting isotope. The photon energy of the single photon emitter is ideally between 100 and 200 keV, because that is a good compromise between good penetration of human tissues and good stopping by detector crystal. This is one of the reasons why {sup}`99m`Tc (emitting photons of 140 keV) is the most used radionuclide for single photon emission imaging. Positron emission will always produce 511 keV photons. That is a bit higher that we would have liked; for PET, there was no choice but to design detectors with sufficient stopping power. Ideally, the isotope would emit nothing else, because other emitted particles will not contribute to imaging, but they will damage the tissues (DNA) they traverse.

In recent years, radionuclide therapy is being used increasingly in cancer therapy. Radionuclide therapy makes use of molecules or other particles that accumulate preferentially in tumors, and which are labeled with radioactive isotopes (radionuclides). The aim is that this radiation will destroy the tumor, with minimal damage to the surrounding healthy tissues. For that purpose, the radiation should have a small penetration depth, as is the case for electrons (aka {math}`\beta^-`), protons and α-particles (particle consisting of two protons and two neutrons, He{sup}`2+`). [](#tab:rntisotopes) and [](#fig:223Ra) list the main emissions by a few of such radionuclides. The decay scheme of {sup}`223`Ra is complex, because several of its daughter products are radiactive as well.

Most radionuclides used for therapy not only emit β or α particles, but also photons. The drawback of these photons is that they cause some radiation to the healthy tissues, but an advantage is that images can be made of the distribution of the radionuclide, enabling accurate dose verification (at least if the photon energies are suitable for imaging).

If the radiopharmacon has high affinity for the tumor and is very specific, i.e. it binds to the tumor and to (almost) nothing else, then the therapy can be more effective than external beam therapy for two reasons: it will treat all metastases, even small ones that may not be revealed by imaging, and a high radiation can be achieved with minimum damage to the surrounding healthy tissues.

To be effective, the amount of radioactivity administered to the patient should be high enough to destroy the tumors, but at the same time low enough to ensure that the radiation to healthy tissues (which may also accumulate some of the radioactivity) remains below safety limits. Consequently, it is important to estimate the expected dose distributions before treatment, and determine the delivered doses after treatment.

% ------------------

:::{list-table} Some radionuclides used in radionuclide therapy
:header-rows: 0
:name: tab:rntisotopes
:align: center

*   *   **{sup}`131`I**

    *   half-life

    *   8.03 days

*   *   emission

    *   mean energy

    *   intensity

*   *

    *   keV

    *   %

*   *   {math}`\beta^-`

    *   182

    *   100

*   *

    *   80

    *   2.62

*   *

    *   284

    *   6.12

*   *   γ

    *   364

    *   81.5

*   *

    *   637

    *   7.16

*   *

    *   723

    *   1.77
:::

:::{figure} figs/fig_223Ra.png
:name: fig:223Ra
:align: center
:alt: Decay scheme of   ^{223}Ra, based on .

*Decay scheme of   {sup}`223`Ra, based on {cite:t}`Martin2006`.*
:::

(mird-formalism)=
### MIRD formalism

% %%%%%%%%%%%%%%%%%%%%%%%

MIRD refers to the Committee on Medical Internal Radiation Dose of the Society of Nuclear Medicine, which provides standard methods for internal radiation dosimetry. The focus has mostly been on producing reasonable dose estimates, to assess and control the risk associated with diagnostic imaging. These days, refinements are being made for more accurate dose calculations as required for radionuclide therapy.

The basic principles of internal dosimetry have already been explained in chapter [??](#chap:biol). MIRD uses the same principles, but formulates them slightly differently, introducing the dose rate and the S-factors. Another difference is that in chapter [??](#chap:biol), we integrated the activity over time to compute the total number of decays, and then computed the resulting dose from them. MIRD computes the dose associated with a single decay event (the dose rate), and integrates that over time.

The body of the patient is considered as a collection of 3D regions which contain an amount of radioactivity. To compute the dose (in Gy) received by a particular region, that region is treated as the *target region* {math}`r_T`, while all regions (including {math}`r_T`) are considered one by one as *source regions* {math}`r_S`. The source region contains a time dependent activity {math}`A(t)`, which is usually assumed uniform for convenience. At each point in time, that activity {math}`A(t)` in the source region produces a dose rate {math}`\dot{D}(t)` in the target region. It is assumed that the two are proportional:

```{math}
:label: eq:doserate

\frac{d D(t)}{dt} = \dot{D}(t) = S \; A(t)
```

The activity {math}`A(t)` is expressed in Bq, the dose rate {math}`\dot{D}(t)` in Gy/s. Consequently, the unit of {math}`S` is Gy / (Bq s) = Gy.

The factor {math}`S`, usually called the S-value, accounts for the following:

*   the probability that a particular particle ({math}`\gamma, \beta^+,
        \beta^-, \alpha`, …) is produced during a decay in source region {math}`r_S`,

*   the energy of each particle,

*   the probability that the particle reaches target region {math}`r_T`,

*   the probability that it deposits (part of) its energy in {math}`r_T`,

*   the mass of {math}`r_T`.

Because patients breathe, the shape of {math}`r_S` and {math}`r_T` and the distance between them may change, which would affect {math}`S`. Consequently, {math}`S` is a function of time, although that is typically ignored to keep the problem tractable. The S-value can be written as

```{math}
:label: eq:Svalue

S(r_T \leftarrow r_S, t) = \frac{1}{M(r_T,t)}
     \sum_i p_i \; E_i \; \phi(r_T \leftarrow r_S, E_i, t)
```

{math}`M(r_T,t)` is the mass of {math}`r_T`, which might be time dependent. The summation is over all emissions {math}`i` that may occur during a decay; {math}`p_i` is the branching ratio, i.e. the probability that emission {math}`i` will occur during a decay. {math}`E_i` is the energy of particle {math}`i` and {math}`\phi(r_T \leftarrow r_S, E_i, t)` gives the fraction of the energy that this particle is expected to deposit in {math}`r_T`. Thus, ϕ depends on the geometry and attenuation of {math}`r_T` and {math}`r_S` and the structures between and around them.

Since the dose rate in {math}`r_T` depends on all the radioactivity inside the patient’s body, we have to sum over all {math}`r_S`:

```{math}
\dot{D}(r_T, t) = \sum_j S\left(r_T \leftarrow r_{S_j}, t\right)
                \; A\left(r_{S_j}, t\right)
```

The dose in {math}`r_T` is obtained by integrating over time:

```{math}
:label: eq:mirddose

\begin{align}
  D(r_T) &= \int_0^{T_D} \dot{D}(r_T, t)\;dt \nonumber\\
     &\simeq \sum_j S\left(r_T \leftarrow r_{S_j} \right)
        \int_0^{T_D} A\left(r_{S_j},t\right) dt \nonumber\\
     &= \sum_j S\left(r_T \leftarrow r_{S_j} \right)
        \tilde A \left(r_{S_j} \right) 
\end{align}
```

{math}`T_D` is some interesting time duration. In many cases, one can set {math}`T_D = \infty`, because the effective half life (combining decay half life and the biogical dynamics) of the radionuclide will be short. {math}`\tilde A` is the time integrated activity. To put {math}`S` in front of the integral sign, we had to make the common approximation that it does not depend on time.

The time integrated activity {math}`\tilde A` has no units, since Bq is the number of desintegrations per s, and a number is unitless. In practice, one often normalizes {math}`\tilde A` with the administered activity {math}`A_0`:

```{math}
\tilde a(r_S) = \frac{\tilde A(r_S)}{A_0}
```

and therefore {math}`\tilde A(r_S) = \tilde a(r_S) A_0`. The unit of {math}`\tilde
a` is time, and for that reason it was called the *residence time*. If all the administered activity {math}`A_0` would stay for a short duration {math}`\tilde a(r_S)` in the region {math}`r_S` and then vanish, then the same {math}`\tilde A(r_S)` would be obtained. Since 2009, {math}`\tilde a(r_S)` is called the *time-integrated activity coefficient* of {math}`r_S` [^w6qBGbp2DM][^w6qBGbp2DM]: In 2009, the MIRD committee adopted a standardization of nomenclature (Journal of Nuclear Medicine, 2009; 50: 477-484)..

To apply equation [](#eq:mirddose) for treatment planning or verification, we need

1.  a 3D segmentation (delineation) of all important structures: organs, parts of organs, tumors, lesions, …, to produce the set of regions

2.  the function {math}`\phi(r_T \leftarrow r_S, E_i, t)` for all possible region pairs ({math}`r_S`, {math}`r_T`), all relevant particles {math}`i` and all relevant energies {math}`E_i`.

3.  the activity {math}`A\left(r_{S_j},t\right)` as a function of time in all these regions,



This should really be done for each individual patient (“personalized dosimetry”). Because that is very difficult, the segmentation and calculation of {math}`\phi(r_T \leftarrow r_S, E_i, t)` have first been addressed based on models of “average patients”. 
[](#fig:MIRD) shows two such models, an early one based on simplified shapes and a more recent and realistic model using non-uniform rotational B-splines (NURBS). Similar models have been developed for children of different ages.



:::{figure} figs/fig_MIRD_average_man.png
:name: fig:MIRD
:align: center
:alt: Left: representation of the average man for MIRD dose computation, as used in 1969 . Right: human body models based on non-uniform rational B-splines (NURBS) .
:::

When the patient model is available, the S-value can be computed with equation [](#eq:Svalue) for every region pair and for all radionuclides of interest. For electrons, positrons and α-particles, one can usually assume that their energy is deposited locally. That makes the calculation of {math}`\phi(r_T \leftarrow
r_S, E_i, t)` very easy:

*   if {math}`r_S \neq r_T`, then {math}`\phi(r_T \leftarrow r_S, E_i, t) \simeq 0`

*   for {math}`r_S = r_T`: {math}`\phi(r_S \leftarrow r_S, E_i, t) \simeq 1`

On the other hand, for photons the calculations are very complicated and have to be done with Monte Carlo simulation.

Finally, to obtain a dose for a particular case, we need to determine the time-activity curves {math}`A\left(r_{S_j},t\right)` for each organ {math}`r_{S_j}`. Currently, this is done by acquiring SPECT or PET scans and manually segmenting the organs in the activity images, or in the corresponding CT images (relying on the spatial alignment produced by the SPECT/CT or PET/CT system). The time-activity curve is typically obtained by acquiring a dynamic SPECT or PET scan. For tracers with long (physical and biological) half life, some additional scans at later time points may be required. A good balance must be found between minimizing the number of scans (and their duration) for optimal patient comfort, and obtaining sufficient samples to reach an acceptable accuracy. In single photon emission imaging, some of the SPECT or SPECT/CT scans may be replaced by planar imaging to improve the temporal resolution (early after injection) or to reduce the imaging time (late after injection).

The anatomical models have been designed for assessing the typical radiation dose associated with diagnostic procedures. Because these doses are relatively low, it is assumed that the dose estimates obtained for such average patients are sufficiently accurate for producing clinical guidelines on the activity to be injected for different tracers and imaging tasks. Novel tracers are often first characterized in animal experiments. If those tests produce good results, they are evaluated in a small group of healthy volunteers, using one or multiple SPECT/CT or PET/CT scans, manual organ delineation and the S-values from the average patient. Because organ delineation is extremely time consuming, the delineation is usually restricted to source organs that accumulate a significant amount of activity and target organs that are known to be radiosensitive. The resulting radiation doses (in mGy or Gy) can then be converted to an effective dose (in mSv or Sv) by multiplying the energies with the appropriate quality factor Q ([](#tab:qualfactor)) and computing the weighted sum of the organ doses [](#tab:effdose).

Application of such models to compute the required activity for radionuclide therapy is controversial, because the model may deviate strongly from the individual patient. However, because no clinical tools are currently available for accurate personalized dosimetry, they are often used for estimating tumor and organ doses in radionuclide therapy as well. This is likely to change in the next several years. It is found that “deep learning” (using multiple layers of convolutional neural networks or CNNs) is an excellent tool to capture the prior knowledge of experts, and it is increasingly being used for organ segmentation in clinical images. In addition, the execution time of Monte Carlo simulation can be decreased from several days to several minutes by implementing them in a clever way on GPU. Consequently, personalized dosimetry for radionuclide therapy in clinically acceptable times and with acceptable efforts seems possible.

(radiation-biologically-effective-dose-bed)=
### Radiation Biologically Effective Dose (BED)

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

As mentioned above, for diagnostic applications, the effect of the radiation is converted to an effective dose in mSv using a simple weighted sum of organ doses. That approach is too simplistic for application in radionuclide therapy, where the doses are much higher and errors in dose calculation can result in undertreatment or irreversible damage to healthy tissues.

In radionuclide therapy, the aim is to destroy the tumor while minimizing the toxicity to the normal tissues. Therefore, we have to estimate the biological effects of the radiation on the normal tissues and the tumor.

Suppose that a piece of tissue, consisting of {math}`N` cells, is being irradiated with a particular dose rate {math}`\dot D`. And assume also that this dose rate kills on average a fraction {math}`k_{\dot D}` per unit of time. Then at any time {math}`t`, the expected number of dying cells per unit of time would equal

```{math}
\frac{d N(t)}{dt} = - k_{\dot D} N(t)
```

After irradiating that tissue for a finite time {math}`T`, the expected number of surviving cells will be

```{math}
N(T) = N(0) e^{- k_{\dot D} T}
```



Assuming that {math}`k_{\dot D}` can vary as a function of time, this generalizes to

```{math}
N(T) = N(0) e^{- \int_0^T k_{\dot D}(t) dt}
```



If we assume that {math}`k_{\dot D}` is proportional to the dose rate {math}`\dot D`, we can write

```{math}
N(T) = N(0) e^{- \alpha \int_0^T \dot D(t) dt} = N(0) e^{-\alpha
    D(T)}
   = N(0) e^{-\mathrm{BED}}
```

where {math}`D(T)` is the total dose accumulated at time {math}`T`. The exponent {math}`\alpha D(T)` is called the *Biologically Effective Dose* or *BED*. The value {math}`\exp(-\mathrm{BED})` is the fraction of surviving cells.

However, it has been observed that the BED depends non-linearly on the dose. This can be explained intuitively as follows. Radiation damages the tissue mostly by ionizing DNA molecules. It is possible that a single hit by a photon or electron produces so much damage to a DNA molecule that the cell dies. But it is also possible (and more likely) that a single hit produces an error in the DNA that can still be repaired. However, this sublethal damage could become lethal, if that same DNA molecule would be hit a second time during the same treatment. Assuming a sublethal hit is more likely than a lethal one, and that the probability of hitting the same location more than two times is very small, the cell killing could be well approximated as

```{math}
:label: eq:kdotD

k_{\dot D}(t) = \alpha \dot D(t) + 2 \beta D(t) \dot D(t)
```

&#x20;The first term corresponds to a single lethal hit at time {math}`t`. The second corresponds to the lethal combination of two sublethal hits, one which happened between 0 and {math}`t`, and the second one at time {math}`t`.



[^t5hYUpKegJ]

[^t5hYUpKegJ]: The factor 2 in the second term of [](#eq:kdotD) is added to make the final expression [](#eq:BED) slightly shorter. We can add any factor, it will be absorbed in β, which must be determined from measurements.



Integration over time produces

```{math}
:label: eq:BED

\begin{align}
  \mbox{BED} &= \int_0^T k_{\dot D}(t) dt \nonumber\\
  &= \alpha \int_0^T \dot D(t) dt
      + 2 \beta \int_0^T D(t) \dot D(t) dt\nonumber\\
  &= \alpha \int_0^T \frac{dD(t)}{dt} dt
      + 2 \beta \int_0^T D(t)\frac{dD(t)}{dt} dt\nonumber\\
  &= \alpha D(T) + \beta \int_0^T \frac{d D^2(t)}{dt} dt \nonumber\\
  &= \alpha D(T) + \beta D^2(T) 
\end{align}
```

This expression can be further refined to include also the effect of repair mechanisms. After sublethal damage, the cell may be able to undo that damage, in which case it would survive a second sublethal hit. Assume for convenience that the probability of repair is constant over time, such that a fraction μ of the damaged cells heal themselves per unit of time. Then if {math}`M` cells took a sublethal hit at time {math}`s`, only {math}`M e^{-\mu (t - s)}` of them would still be damaged at time {math}`t > s`. Adjusting equation [](#eq:BED) accordingly produces

```{math}
:label: eq:BEDrepair

\begin{align}
  \mbox{BED} &=\;\; \alpha \int_0^T \dot D(t) dt
  + 2 \beta \int_0^T \dot D(t) dt
  \int_0^t \dot D(s) e^{-\mu(t-s)}ds \nonumber\\
  &=\;\; \alpha D(T) + \beta \, G \, D^2(T) \\
  \mbox{with\;\;} G &=\;\; \frac{2}{D^2(T)} \int_0^T \dot D(t) dt
    \int_0^t \dot D(s) e^{-\mu(t-s)}ds \nonumber
\end{align}
```

The G-factor is called the Lea-Catcheside factor (after the authors who derived these equations). It is easy to check that with {math}`\mu =
0`, i.e. no cell repair, equation [](#eq:BEDrepair) reduces to [](#eq:BED). Fortunately, normal cells are typically better at repairing radiation damage than tumor cells.

(dosimetry-software)=
### Dosimetry software

% %%%%%%%%%%%%%%%%%%%%%%%%%%%

Several software tools have been developed and commercialized to support dosimetry calculations. The first tools (e.g. Olinda/EXM, [^cSFbKGFd6J][^cSFbKGFd6J]: Organ Level INternal Dose Assessment & EXponential Modeling developed by Vanderbilt University, TN, USA and recently commercialized) focused on dosimetry for diagnostic imaging procedures. This kind of software takes as input the activity values in organs at a few different time points, and provides

*   pre-computed S-values based on anatomical models, such as in [](#fig:MIRD) (and listed in MIRD pamphlet 11), for many radionuclides, and

*   software for fitting kinetic models, typically a sum of exponentials, which are used to interpolate between the time points and extrapolate to infinity in a sensible way.

The output is the dose in mGy to all organs, and the corresponding effective dose in mSv.

Some research teams share their more recent software tools for personalized internal dosimetry. An example is the LundaDose Program from Lund University, Sweden. This program focuses on internal dosimetry for therapy with {sup}`177`Lu or {sup}`90`Y labeled molecules. It takes SPECT/CT images as input and computes the organ and tumor doses with Monte Carlo simulation. Other similar free software packages can be found at mirdsoft.org, www.idac-dose.org and www.opendose.org.

By taking directly the images of the activity distribution as input, the need for segmenting the source organs is eliminated. The Monte Carlo simulation can make use of the activity in each voxel, or in other words, each voxel is treated as a source region {math}`r_S`. And similarly, the dose can be computed in each voxel. This is called *voxelized dosimetry*. It is not only more convenient, it is also more accurate, because it eliminates the need for assuming a uniform activity distribution within large source and target regions. For the final analysis of the dose images, still organ and lesion segmentation is necessary for the target regions {math}`r_T`, because we need to know where the tumor and the radiosensitive organs are. However, the analysis of the dose in regions {math}`r_T` can now be made more informative, by taking into account the non-uniform dose distribution in the region.

(examples)=
### Examples

% %%%%%%%%%%%%%%%%%

%  isotopes 131-I, 177-Lu, 90-Y, 223-Ra

%  radiopharmaceuticals

%     - 131I NaI (thyroid cancer)

%     - 131mIBG neuroendocrine tumors

%     - 177Lu and 90Y PRRT (Peptide Receptor Radionuclide Therapy) for

%       neuroendocrine tumors

%     - 223RaCl2 and 177Lu-PSMA for prostate cancer

%     - 90Y-ibritumomab tiuxetan (90Y-IT) for treatment of follicular

%       lymphoma or B-cell non-Hodgkin's lymphoma

%     - 90Y microspheres for SIRT

%     - 166Ho microspheres

(annual-effective-dose-due-to-natural-40-k)=
#### Annual effective dose due to natural {sup}`40`K

% ========================================================

{sup}`40`K is a naturally occurring radioactive isotope of potassium. Its abundance, i.e. the amount of {sup}`40`K in natural K, is 0.012%. Humans have approximately 2 g K per kg body weight. The half life of {sup}`40`K is {math}`1.25 \cdot 10^9` years. It decays by {math}`\beta^-` emission with a branching ratio of 90%, see [](#fig:40Kdecay). The mean energy of the emitted electron equals 0.59 MeV.

:::{figure} figs/fig_40K_decay.png
:name: fig:40Kdecay
:align: center
:alt: Decay scheme of ^{40}K.

*Decay scheme of {sup}`40`K.*
:::

To compute the radiation dose due to {sup}`40`K, we assume that this dose is only due to the {math}`\beta^-` emission. Suppose there are {math}`N_0` {sup}`40`K atoms in a g at time {math}`t = 0`. Then the number of radioactive atoms at time {math}`t` equals

```{math}
N(t) = N_0 \; e^{- \ln 2 \frac{t}{T_{1/2}}}
```

implying that the activity, i.e. the number of decaying atoms per unit of time equals

```{math}
A(t) = - \frac{dN(t)}{dt} = \frac{\ln 2}{T_{1/2}} N(t).
```

where we have to express {math}`T_{1/2}` in seconds to obtain a result in Bq. Denoting the number of seconds per year as {math}`s_y`, we have {math}`T_{1/2} = 1.25 \cdot 10^9 \; s_y`.

Avogadro’s number equals {math}`N_A = 6.022 \cdot 10^{23}` atoms/mole, and 1 mole of {math}`^{40}K` weighs 40 g. Consequently, the activity per kg tissue equals

```{math}
\frac{A}{m} = \frac{\ln 2}{T_{1/2}} \;
  \frac{N_A}{40 \text{g}} \;
  \frac{2 \text{g} \;}{\text{kg}} \;
  1.2 \cdot 10^{-4}
```

This produces an activity per mass in Bq/kg. In 90% of these decays, an electron is emitted which deposits on average an energy of 0.59 MeV. Thus, the energy deposited by a decay equals

```{math}
E = 0.9 \cdot 0.59 \cdot 10^6 \mbox{ eV} \cdot 1.6
    \cdot 10^{-19} \frac{\mbox{J}}{\mbox{eV}}
```

Multiplying {math}`A` and {math}`E` produces the deposited energy per mass and per s in J / (kg s) = Gy / s. Finally, we multiply this with the number of seconds per year {math}`s_y` and with 1000 to obtain the result in mGy per year:

```{math}
\begin{align}
  &\frac{A}{m}\;E \; \frac{\mbox{1000 mGy}}{\mbox{Gy}} \frac{s_y}{\mbox{ year}}\\
  &= \frac{\ln 2}{1.25 \cdot 10^9 \; s_y} \;
  \frac{6.022 \cdot 10^{23}}{40} \;
  \frac{2 \cdot 1.2 \cdot 10^{-4}}{\mbox{kg}} \;
  0.9 \cdot 0.59 \cdot 10^6 \cdot 1.6 \cdot 10^{-19} \mbox{ J}
   \frac{\mbox{1000 mGy}}{\mbox{Gy}} \; \frac{s_y}{\mbox{ year}} \nonumber\\
  &= 0.17 \;\frac{\mbox{mGy}}{\mbox{year}}
\end{align}
```

This calculation seems OK, since the UNSCEAR 2008 report gives also 0.17 mSv for the effective dose from natural {sup}`40`K irradiation.

(thyroid-therapy-with-131-i)=
#### Thyroid therapy with {sup}`131`I

% =========================================

The thyroid has a strong affinity for iodine, and thyroid tumors inherit this affinity from the normal cells. Consequently, a beta-emitting isotope like {sup}`131`I is a good radionuclide for treating thyroid cancer. As can be seen in [](#tab:rntisotopes), {sup}`131`I not only emits electrons, but also several gammas. This has the drawback that the radionuclide trapped in the tumor will not only irradiate the tumor with electrons, it will also send some energy to the entire body as photons. But an advantage of these photons is that they can be used for imaging with a gamma camera or activity estimations with a gamma detector. Because several of these gammas have high energies, imaging must be done with high energy collimators, and detectors targeting the thyroid must be well shielded to avoid contributions from {sup}`131`I uptake in the rest of the body.

To determine the activity to be administered, a low activity of {sup}`131`I is administered and imaging is performed to see which fraction of the activity is taken up in the thyroid. For therapy follow up, imaging (or photon counting) is be done to monitor the {sup}`131`I uptake in the thyroid as a function of time.

[](#fig:thyroid) illustrates the calibration and activity monitoring with a photon counting detector (typically a NaI crystal with PMT). A standard setup is used to scan the patient, to ensure good reproducibility, such that after calibration the measurement is quantitative. For calibration, a phantom mimicking the geometry and attenuation of the neck is used, containing {sup}`131`I at the position of the thyroid.

:::{figure} figs/fig_thyroid_therapy.png
:name: fig:thyroid
:align: center
:alt: Thyroid therapy with ^{\it{131}}I. At different time points, activity measurements are done with a simple detector, calibrated with a phantom. A tracer kinetic model is applied to estimate the time activity curve from a few measurements. The figures are from . (RIU(t) denotes fractional ^{\it{131}}I uptake in the target tissue at time t, and k_t, k_B and k_T are time constants of the kinetic model.)

*Thyroid therapy with {math}`^{\it{131}}`I. At different time points, activity measurements are done with a simple detector, calibrated with a phantom. A tracer kinetic model is applied to estimate the time activity curve from a few measurements. The figures are from {cite:t}`Haenscheid2013`. (RIU(t) denotes fractional {math}`^{\it{131}}`I uptake in the target tissue at time t, and {math}`k_t`, {math}`k_B` and {math}`k_T` are time constants of the kinetic model.)*
:::

With this setup, the patient is scanned a few times over a week, producing measurements of the activity in the thyroid. Then a kinetic model is applied, to fit a smooth and realistic time-activity curve through these points. A good model must be used, because estimating the total dose to the thyroid involves a very strong extrapolation beyond the last time point (see [](#fig:thyroid)).

(id-131-i-mibg-therapy-for-neuroblastoma)=
#### {sup}`131`I-mIBG therapy for neuroblastoma

% ==================================================

The compound mIBG (meta-iodobenzylguanidine) is taken up by cells of the sympathetic nervous system. Neuroblastoma usually inherit this affinity for mIBG, and as a result, {sup}`131`I-mIBG can be used to selectively irradiate these tumors. To circumvent the toxic effects on the bone marrow (which makes red blood cells), stem cells are collected before treatment and reinfused after the treatment. This will ensure the production of blood cells after treatment. The {sup}`131`I-mIBG treatment is combined with Topotecan, a drug that makes neuroblastoma more sensitive to radiation {cite:t}`Gaze2015`.

The aim of the {sup}`131`I-mIBG procedure, applied to treat children with metastatic neuroblastoma, is to achieve a whole body dose of 4 Gy. It has been shown that with this whole body dose, the dose to the neuroblastoma is sufficiently high and side effects are limited. To achieve this, the therapy is given in two fractions. The first fraction delivers a first whole body dose well below 4 Gy. In addition, the photons emitted by {sup}`131`I are used to determine the whole body dose. This is often done with a simple gamma detector and appropriate calibration, similar to what is shown in [](#fig:thyroid), but this time focusing on the entire body. Alternatively (and more accurately), planar imaging or SPECT can be used. From that measured dose and the known amount of administered activity in the first fraction, the amount of activity for the second fraction is computed, to obtain the target dose of 4 Gy.

:::{figure} figs/fig_mIBG.png
:name: fig:mibg
:align: center
:alt: The whole body doses achieved in 8 patients (left), and the activity that was administered to obtain this dose of approximately 4 Gy (right). The red and green blocks correspond to the first and second fraction, respectively. For patients 6 and 7, much more activity was needed to achieve the same whole body dose. Courtesy of Gaze et al. .

*The whole body doses achieved in 8 patients (left), and the activity that was administered to obtain this dose of approximately 4 Gy (right). The red and green blocks correspond to the first and second fraction, respectively. For patients 6 and 7, much more activity was needed to achieve the same whole body dose. Courtesy of Gaze et al. {cite:t}`Sangro2012`.*
:::



[](#fig:mibg) shows for 8 patients the whole body doses produced by the two fractions. The dose of the first fraction was only based on the patient weight, and produced roughly 2 Gy. This was used to adjust the activity given in the second fraction, shown in the plot at the right hand side in the figure. The plot at the left shows that this produced a total dose of approximately 4 Gy. This treatment is effective. However, more accurate tumor dose computation would be useful, to provide more information about the relation between the administered doses, the tumor control and the toxic effects to healthy tissues, which would facilitate the development of even more effective, personalized treatment.

(id-90-y-selective-internal-radiation-therapy-for-liver-tumors)=
#### {sup}`90`Y selective internal radiation therapy for liver tumors

% ============================================

The liver can be affected by a primary liver (hepatic) tumor or by tumor metastases originating from elsewhere in the body.

One approach to treating liver tumors is radioembolization, i.e. to release small radioactive spheres into the blood supplying the tumors. These microspheres, made of resin or glass, have a diameter of 25-35 μm, which is small enough to travel through larger blood vessels, and big enough to get stuck in the tumor micro-vasculature. The microsphere then hinders or blocks the perfusion through the microvessel, which is already bad for the tumor. But more importantly, these microspheres contain a β-emitting isotope. The emitted electrons interact with the surrounding tissue, depositing their energy within a few mm from where they are emitted. The aim is to have the microspheres accumulated in or very close to the tumor lesions, such that the β-radiation destroys the tumor with minimal damage to the healthy liver.

The liver is perfused not only by the hepatic artery, but also by the portal vein. Veins are typically outputting blood from organs, but the liver takes input from a vein too, because its task involves processing venous blood from the stomach, intestines and spleen. Healthy liver cells receive about 75% of their blood from the portal vein, and only 25% from the hepatic artery. In contrast, tumors take most of their blood from the hepatic artery. For that reason, the microspheres are released via a catheter that is maneuvered into the hepatic artery. To further increase selectivity, the catheter is steered into one or a few branches of the hepatic artery which are known to supply tumors. As illustrated in [](#fig:Sangro), a better healthy tissue sparing can be achieved when the tumor is more localized in the liver. For this reason, the treatment is called *selective internal radiation therapy* (SIRT).

:::{figure} figs/fig_SIRT_Sangro.png
:name: fig:Sangro
:align: center
:alt: Radioactive microspheres are sent into the liver through selected branches of the portal vein, targeting the tumors. .

*Radioactive microspheres are sent into the liver through selected branches of the portal vein, targeting the tumors. {cite:t}`Sangro2012`.*
:::

One of the electron-emitting isotopes that is often used for SIRT is the yttrium isotope {sup}`90`Y.

(dose-verification-for-sirt-with-90-y-microspheres)=
##### Dose verification for SIRT with {sup}`90`Y microspheres

% '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

As shown in [](#tab:rntisotopes), {sup}`90`Y is really a pure β-emitter, but in 32 of each million decays, it produces a positron. Obviously, it is a poor positron emitter, but because the treatment involves large doses (a few GBq), because the microspheres are concentrated near the liver tumors and because the effective sensitivity of current PET systems is high, it is possible to make quantitative images of the {sup}`90`Y distribution in the body of the patient. Since the microspheres remain trapped for a long time in the microvessels, we can assume that the microspheres concentrations remain constant over time, and that the radioactive decay of {sup}`90`Y is the only cause of change to the activity concentration. Therefore, we only need a single PET image for dose verification after treatment.

Since the electrons deposit their energy very close to their emission source, the radiation dose to the tissues can be computed using the “local deposition model”. That means that with good approximation, the dose is proportional to the activity concentration achieved shortly after injection: multiplication with a global scale factor transforms the PET activity image with voxel values in Bq/ml to a dose image with voxel values in Gy.

The time integrated activity {math}`\tilde A` equals

```{math}
\tilde A = \int_0^\infty A_0\; e^{- \frac{\ln 2}{T_{1/2}}} dt
  \;=\; A_0 \frac{T_{1/2}}{\ln 2}
```

where {math}`A_0` is the activity in Bq in a particular region of interest, and {math}`T_{1/2}` = 64.1 hours is the half life of {sup}`90`Y. Following equation [](#eq:mirddose), the dose is obtained by multiplying {math}`\tilde A` with the S-factor, given by equation [](#eq:Svalue). For {sup}`90`Y, the S-factor reduces to

```{math}
S(r \leftarrow r) = \frac{E}{M(r)}
```

where {math}`M(r)` is the mass of the region {math}`r` and {math}`E` is the average energy of the emitted electron. Consequently, the accumulated dose in a particular region {math}`r` equals

```{math}
\begin{align}
  D_r &= S(r\leftarrow r) \; \tilde A\\
      &= \frac{A_0}{M(r)} \;E \;\frac{T_{1/2}}{\ln 2}\\
  &= \frac{A_0}{M(r)} \mbox{ 933.6 $\cdot 10^3$ eV } \cdot 1.6
     \cdot 10^{-19} \frac{\mbox{J}}{\mbox{eV}} \;
     \frac{\mbox{64.1 h} \cdot \mbox{3600 s/h}}{0.693}\\
  &= 49.7 \cdot 10^{-9} \;\mbox{Js} \; \frac{A_0}{M(r)}
\end{align}
```

Consequently, an activity of 1 GBq {sup}`90`Y trapped in a region of 1 kg produces an accumulated radiation dose of approximately 50 Gy.

An image in Bq/ml can be converted to an image in Bq/g by dividing it by the tissue density in g/ml, which is close to unity except for bone and lung. An {sup}`90`Y activity image in Bq/g can be converted to accumulated dose in Gy, by multiplying it with {math}`49.7 \cdot 10^{-9}` Js • 1000 g/kg = {math}`49.7 \cdot 10^{-6}` Gy g s.

%  Annual exposure in Belgium (laatste dia van Kristof)

(sirt-treatment-planning-with-99mtc-labeled-micro-aggregated-albumin)=
##### SIRT treatment planning with {sup}`99m`Tc labeled micro-aggregated albumin

% ''''''''''''''''''''''''''''''''''''''''''''''''''''

Albumin microaggregates (MAA) are very small particles (a few microns) which tend to accumulate in microvasculature, much like resin or glass microspheres. MAA labeled with {sup}`99m`Tc are used to simulate a SIRT treatment: the {sup}`99m`Tc-MAA is released in selected branch(es) of the portal vein, and the result is imaged with SPECT. SPECT imaging must be done shortly after MAA-administration, because unlike the therapeutic microspheres, MAA is only trapped temporally. The {sup}`99m`Tc-MAA study is done to check if the injected particles will remain in the liver, or if a significant portion of them ends up in the lungs. In some patients this happens, because their vasculature has some liver-to-lung shunts. The study is also done to verify that the catheterization procedure will reach all the tumors. [](#fig:SirtMaaY) shows transaxial slices from a pre-treatment {sup}`99m`Tc-MAA image and the corresponding post-treatment {sup}`90`Y-PET image. In this study, a good agreement between the pre- and post-treatment images was obtained.



:::{figure} figs/fig_SIRT_Tc_Y.png
:name: fig:SirtMaaY
:align: center
:alt: Left: the 99mTc-MAA image (in color) fused with the corresponding CT image (black and white), from the pre-treatment SPECT/CT image. Right: the ^{90}Y-PET image fused with the corresponding MR image, from the post-treatment PET/MR image.

*Left: the {sup}`99m`Tc-MAA image (in color) fused with the corresponding CT image (black and white), from the pre-treatment SPECT/CT image. Right: the {sup}`90`Y-PET image fused with the corresponding MR image, from the post-treatment PET/MR image.*
:::



(quantitative-imaging)=
### Quantitative imaging

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Treatment planning and dose verification require quantitative imaging, since we need activity images in Bq/ml to compute dose images in Gy. The creation and analysis of accurate dose images is not only useful to verify if the treatment was successful, it also provides valuable data to learn more about the complicated relationship between radiation dose and biological effect, both in the tumors and the normal tissues. This new knowledge should enable us to make radionuclide therapy more effective. Doing that will require more accurate treatment planning, and therefore also quantitative imaging.\




As explained in previous chapters, PET and SPECT are quantitative, provided that

*   all corrections for sensitivity, attenuation, Compton scatter and/or randoms are performed well.

*   the reconstructed image values are calibrated by determining the calibration factor, which converts the reconstructed voxel values into values in Bq/ml, see sections [](#sec:spectquant) for SPECT and [](#sec:scalefactor) for PET. The calibration factor is radionuclide dependent, and in particular in SPECT, this dependence is so complicated that it necessitates determining the calibration factor from phantom measurements for each tracer.

+++
(appendix)=
## Appendix

(app:poisson)=
### Poisson noise

% =========================

Assume that the expected amount of measured photons per unit time equals {math}`r`. Let us now divide this unit of time in a {math}`k` time intervals. If {math}`k` is sufficiently large, the time intervals are small, so the probability of detecting a photon in such an interval is small, and the probability of detecting two or more is negligible. Consequently, we can assume that in every possible measurement, only zero or one photon is detected in every interval. The probability of detecting one photon in an interval is then {math}`r /
k`. A measurement of {math}`n` photons must consist of {math}`n` intervals with one photon, and {math}`k - n` intervals with no photons. The probability of such a measurement is:

```{math}
:label: jn:poisson:1

p_r(n) = \left( \frac{r}{k} \right)^n \left(1 - \frac{r}{k} \right)^{k-n}
       \frac{k!}{n!(k-n)!}
```

The first factor is the probability of detecting {math}`n` photons in {math}`n` intervals. The second factor is the probability of detecting no photons in {math}`n - k` intervals. The third factor is the amount of ways that these {math}`n` successful and {math}`n-k` unsuccessful intervals can be combined in different measurements.

As mentioned above, equation [](#eq:poisson:1) becomes better when {math}`k` is larger. To make it exact, we simply have to let {math}`k` go to infinity.

```{math}
\lim_{k \rightarrow \infty} p_r(n) 
  = \frac{r^n}{n!} \lim_{k \rightarrow \infty} \left( 1 - \frac{r}{k} \right)^k
```

It turns out that computing the limit of the logarithm is easier, so we have

```{math}
\begin{align}
  \lim_{k \rightarrow \infty} \left( 1 - \frac{r}{k} \right)^k
 &=
 \exp \left(\lim_{k \rightarrow \infty} \frac{\ln(k - r) - ln(k)}{1/k}  \right)
\nonumber\\
&= 
  \exp \left(\lim_{k \rightarrow \infty}  
  \frac{1/ (k-r) - 1/k}{-1/k^2} \right) \nonumber \\
&= \exp (-r)
\end{align}
```

So it follows that

```{math}
\lim_{k \rightarrow \infty} p_r(n) = \frac{e^{-r} r^n}{n!}.
```

(app:convolution)=
### Convolution and PSF

% =========================

In section [](#sec:collimation), the collimator point spread function (PSF) was computed. The collimator PSF tells us which image is obtained for a point source at distance {math}`H` from the collimator. What happens if two point sources are positioned in front of the camera, both at the same distance {math}`H`? Since the sources and the photons don’t interact with each other, all what was said above still applies, for each of the sources. The resulting image will consist of two PSFs, each centered at the detector point closest to the point source. Where the PSFs overlap, they must be added, since the detector area in the overlap region gets photons from both sources. The same is true for three, four, or one million point sources, all located at the same distance {math}`H` from the collimator. To predict the image for a set of one million point sources, simply calculate the corresponding PSFs centered at the corresponding positions on the detector, and sum everything.

The usual mathematical description of this can be considered as a two step approach:

1.  &#x20;Assume that the system is perfect: the image of a point source is a point, located on the perpendicular projection line through the point source. Mathematicians would call that “point” in the image a “Dirac impulse”. The image of two or more point sources contains simply two or more Dirac impulses, located at corresponding projection lines.\




    Let {math}`f(x,y)` represent the image value at position {math}`(x,y)`. This image can be regarded as the sum of an infinite number of Dirac impulses {math}`\delta(x,y)`, one at every location {math}`(x,y)`:

    ```{math}
    \begin{align}
    f(x,y) &= (f \otimes \delta) (x,y)\\
           &= \int_{-\infty}^{\infty} du \int_{-\infty}^{\infty} dv \, f(u,v) \, \delta(x-u, y-v)
    \end{align}
    ```

2.  Correction of the first step: the expected image of a point is not a Dirac impulse, but a PSF. Therefore, replace each of the Dirac impulses in the image by the corresponding PSF, centered at the position of the Dirac impulse.

    ```{math}
    \begin{align}
    g(x,y) &= (f \otimes \mbox{PSF}) (x,y)\\
           &= \int_{-\infty}^{\infty} du \int_{-\infty}^{\infty} dv \, f(u,v) \, \mbox{PSF}(x-u, y-v)
    \end{align}
    ```

The second operation is called the *convolution* operation. Assume that a complex flat (e.g. a inhomogeneous radioactive sheet) tracer distribution would be put in front of the camera, parallel to the collimator (at distance {math}`H`). What image will be obtained? Regard the distribution as consisting of an infinite number of point sources. This does not change the distribution, it only changes the way you look at it. Project all of these sources along an ideal perpendicular projection line into the image. You will now obtain an image consisting of an infinite number of Dirac impulses. Replace each of these impulses with the PSF and sum the overlapping values to obtain the expected image.

If the distance to the collimator is not the same for every point source, then things get more complicated. Indeed, the convolution operator assumes that the PSF is the same for all point sources. Therefore, to calculate the expected image, the previous procedure has to be applied individually for every distance, using the corresponding distance dependent PSF. Finally, all convolved images have to be summed to yield the expected image.

(app:convol2gauss)=
### Combining resolution effects: convolution of two Gaussians

% =========================

Very often, the PSF can be well approximated as a Gaussian. This fact comes in handy if we want to combine two PSFs. For example: what is the combined effect of the intrinsic resolution (PSF of scintillation detection) and the collimator resolution (collimator PSF)?

How can two PSFs be combined? The solution is given in appendix [](#app:convolution): one of the PSFs is regarded as a collection of Dirac impulses. The second PSF must be applied to each of these pulses. So we must compute the convolution of both PSFs. This appendix shows that if both are approximately Gaussian, the convolution is easy to compute.

Let us represent the first and second PSFs as follows:

```{math}
F_1(x) = A \exp\left( -\frac{x^2}{a^2}\right)  \;\;\; \mbox{and} \;\;\;
  F_2(x) = B \exp\left( -\frac{x^2}{b^2}\right)
```

&#x20;Thus, {math}`\sigma_1 = a / \sqrt{2}` and {math}`A = 1 / (\sqrt{2 \pi} \sigma_1)`, and similar for the other PSF. The convolution is then written as:



```{math}
\begin{align}
(F_1 \otimes F_2)(x) &=
  AB \int_{-\infty}^{\infty} \exp\left(- \frac{u^2}{a^2} - \frac{(x-u)^2}{b^2}\right) du\\
&= AB \int_{-\infty}^{\infty} \exp\left(- m u^2   + \frac{2xu}{b^2} - \frac{x^2}{b^2}\right)
  du \\
m &= \left( \frac{1}{a^2} + \frac{1}{b^2}\right)
\end{align}
```



The exponentiation contains a term in {math}`u^2` and a term in {math}`u`. We can get rid of the {math}`u` by requiring that both terms result from squaring something of the form {math}`(u + C)^2`, and rewriting everything as {math}`(u + C)^2 - C^2`. The {math}`C^2` is not a function of {math}`u`, so it can be put in front of the integral sign.

%  

```{math}
\begin{align}
 (F_1 \otimes F_2)(x)  &= AB \int_{-\infty}^{\infty} \exp\left(- \left( \sqrt{m} u 
         - \frac{x}{b^2 \sqrt{m}} \right)^2
       + \frac{x^2}{b^4 m}
       - \frac{x^2}{b^2}\right) du\\
 &=  AB \exp\left(\frac{x^2}{b^4 m} - \frac{x^2}{b^2}\right)
     \int_{-\infty}^{\infty} \exp\left(- \left( \sqrt{m} u 
         - \frac{x}{b^2 \sqrt{m}} \right)^2\right) du
\end{align}
```

&#x20;The integrand is a Gaussian. The center is a function of {math}`x`, but the standard deviation is not. The integral from {math}`-\infty` to ∞ of a Gaussian is a finite value, only dependent on its standard deviation. Consequently, the integral is not a function of {math}`x`. Working out the factor in front of the integral sign and combining all constants in a new constant {math}`D`, we obtain



```{math}
(F_1 \otimes F_2)(x) =  D \exp\left(-\frac{x^2}{a^2 + b^2}\right)
```



So the convolution of two Gaussians is again a Gaussian. The variance of the resulting Gaussian is simply the sum of the input variances (by definition, the variance is the square of the standard deviation).

The FWHM of a Gaussian is proportional to the standard deviation, so we obtain a very simple expression to compute the FWHM resulting from the convolution of multiple PSFs:

```{math}
\mbox{FWHM}^2 = \mbox{FWHM}_1^2 + \mbox{FWHM}_2^2 + \ldots + \mbox{FWHM}_n^2
```

(app:error)=
### Error propagation

% ==========================

The mean and the variance of a distribution {math}`a` are defined as:

```{math}
\begin{align}
  \mbox{mean}(a) &= \overline{a} = E(a) = \frac{1}{N} \sum_{i=1}^N a_i\\
  \mbox{variance}(a) &= \sigma_a^2 = E\left[ (a - \overline{a})^2 \right]
   = \frac{1}{N} \sum_{i=1}^N (a_i - \overline{a})^2,
\end{align}
```

where {math}`E` is the expectation, {math}`a_i` is a sample from the distribution and the summation is over the entire distribution. By definition, {math}`\sigma_a` is the standard deviation. When computations are performed on samples from a distribution (e.g. Poisson variables) the noise propagates into the result. Consequently, one can regard the result also as a sample from some distribution which can be characterized by its (usually unknown) mean value and its variance or standard deviation. We want to estimate the variance of that distribution to have an idea of the precision on the computed result. We will compute the variance of the sum or difference and of the product of two independent variables. We will also show how the variance on any function of independent samples can be easily estimated using a first order approximation.

Keep in mind that these derivations only hold for *independent* samples. If some of them are dependent, you should first eliminate them using the equations for the dependencies.

(sum-or-difference-of-two-independent-variables)=
#### Sum or difference of two independent variables

% ----------------------------------------------

We have two variables {math}`a` and {math}`b` with mean {math}`\overline{a}` and {math}`\overline{b}` and variance {math}`\sigma_a^2` and {math}`\sigma_b^2`. We compute {math}`a \pm b` and estimate the corresponding variance {math}`\sigma_{a \pm b}^2`.

```{math}
:label: eq:app_sumerror

\begin{align}
\sigma_{a \pm b}^2 &= E\left[\left((a \pm b) - (\overline{a} \pm \overline{b}) \right)^2\right]
           \nonumber\\
 &= E\left[(a-\overline{a})^2\right] + E\left[(b-\overline{b})^2\right] \pm E\left[2(a-\overline{a})(b-\overline{b})\right]
           \nonumber\\
 &= E\left[(a-\overline{a})^2\right] + E\left[(b-\overline{b})^2\right] \pm 2 E\left[(a-\overline{a})\right]E\left[(b-\overline{b})\right]
           \nonumber\\
 &= \sigma_a^2 + \sigma_b^2, 
\end{align}
```

because the expectation of {math}`(a - \overline{a})` is zero. The expectation {math}`E\left[(a-\overline{a})(b-\overline{b})\right]` is the covariance of {math}`a` and {math}`b`. The expectation of the product is the product of the expectations if the variables are independent samples, and therefore, the covariance of independent variables is zero.

So in linear combinations the noise adds up, even if the variables are subtracted!

(product-of-two-independent-variables)=
#### Product of two independent variables

% ------------------------------------

For independent variables, the expectation of the product is the product of the expectations, so we have:

```{math}
:label: eq:app_noise_prod1

\begin{align}
 \sigma_{ab}^2 &= E\left[\left( ab - \overline{a} \overline{b}\right)^2\right] \nonumber\\
  &= E\left[a^2b^2\right] + \overline{a}^2\overline{b}^2 - E\left[2 a b \overline{a} \overline{b}\right] \nonumber\\
  &= E\left[a^2\right] E\left[b^2\right] - \overline{a}^2 \overline{b}^2 
\end{align}
```

This expression is not very useful, it must be rewritten as a function of {math}`\overline{a}`, {math}`\overline{b}`, {math}`\sigma_a` and {math}`\sigma_b`. To obtain that, we rewrite {math}`a` as {math}`\overline{a} + (a - \overline{a})`:

```{math}
\begin{align}
  E\left[a^2\right] &= E\left[(\overline{a} + (a - \overline{a}))^2\right] \nonumber\\
 &= \overline{a}^2 + E\left[\left( a - \overline{a} \right)^2\right] + E\left[2 \overline{a}(a - \overline{a})\right]
       \nonumber\\
 &= \overline{a}^2 + \sigma_a^2
\end{align}
```

Substituting this result for {math}`E[a^2]` and {math}`E[b^2]` in [](#eq:app_noise_prod1) we obtain:

```{math}
\begin{align}
\sigma_{ab}^2 &= (\overline{a}^2 + \sigma_a^2)(\overline{b}^2 + \sigma_b^2) 
                     - \overline{a}^2 \overline{b}^2 \nonumber\\
 &= \overline{a}^2\sigma_b^2 + \overline{b}^2\sigma_a^2 + \sigma_a^2 \sigma_b^2
        \nonumber\\
 &= \overline{a}^2\overline{b^2}\left( \frac{\sigma_a^2}{\overline{a}^2} + 
       \frac{\sigma_b^2}{\overline{b}^2} 
     + \frac{\sigma_a^2\sigma_b^2}{\overline{a}^2\overline{b}^2}\right)\\
 &\simeq \overline{a}^2\overline{b^2}\left( \frac{\sigma_a^2}{\overline{a}^2} + 
       \frac{\sigma_b^2}{\overline{b}^2}\right)
\end{align}
```

The last line is a first order approximation which is acceptable if the relative errors are small. We conclude that when two variables are multiplied the relative variances must be added.

(any-function-of-independent-variables)=
#### Any function of independent variables

% -----------------------------------------

If we can live with first order approximations, the variance of any function of one or more variables can be easily estimated. Consider a function {math}`f(x_1, x_2, \ldots x_n)` where the {math}`x_i` are independent samples from distributions characterized by {math}`\overline{x_i}` and {math}`\sigma_i`. Applying first order equations means that {math}`f` is treated as a linear function:

```{math}
\begin{align}
  E\left[\left( f(x_1, \ldots x_n) - E\left[f(x_1, \ldots x_n)\right]\right)^2\right]
  &\simeq  E\left[\left( f(x_1,\ldots x_n) 
        - f(\overline{x_1}, \ldots \overline{x_n})\right)^2\right] \nonumber \\
  &\simeq  E\left[\left( \left. \frac{\partial f}{\partial x_1} \right|_{\overline{x_1}}
                 (x_1 - \overline{x_1}) + \ldots
            \left. \frac{\partial f}{\partial x_n} \right|_{\overline{x_n}}
                 (x_n - \overline{x_n}) \right)^2\right] \nonumber \\
  &= \left( \left. \frac{\partial f}{\partial x_1} \right|_{\overline{x_1}} \right)^2
        \sigma_1^2 + \ldots
    \left( \left. \frac{\partial f}{\partial x_n} \right|_{\overline{x_n}} \right)^2
         \sigma_n^2
\end{align}
```

The first step is a first order approximation: the expectation of a linear function is the function of the expectations. Similarly, the second line is a Taylor expansion, assuming all higher derivatives are zero. The third step is the application of [](#eq:app_sumerror).

With this approach you can easily verify that the variance on a product or division is obtained by summing the relative variances.

(app:cs)=
### Central slice theorem

% =================================

This appendix gives a proof of eq ([62](#fouriertheorem)) for any angle θ. The projection {math}`q(s,\theta)` can be written as

```{math}
q(s, \theta) = \int_{-\infty}^{\infty} \lambda(s \cos\theta - r\sin\theta, 
                                s \sin\theta + r\cos\theta) dr
```

The 1D Fourier transform of {math}`q(s,\theta)` along {math}`s` equals:

```{math}
:label: eq:Q1

\begin{align}
  Q_1(\nu_s, \theta) &= \int_{-\infty}^{\infty} q(s, \theta) e^{-j2\pi \nu_s s} ds \nonumber \\
  &= \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\lambda(s\cos\theta - r\sin\theta, 
                          s\sin\theta + r\cos\theta)e^{-j2\pi \nu_s s} dr ds
      
\end{align}
```

Now consider the 2D Fourier transform of {math}`\lambda(x,y)`:

```{math}
\Lambda(\nu_x, \nu_y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \lambda(x,y) 
       e^{-j2\pi (\nu_x x + \nu_y y)} dx dy
```

We now switch to a rotated coordinate system by setting:

```{math}
\begin{align}
   x = s \cos\theta - r\sin\theta \;\;\;&\mbox{and}& \;\;\;
   y = s\sin\theta + r\cos\theta\\
   \nu_x = \nu_s \cos\theta - \nu_r\sin\theta \;\;\;&\mbox{and}& \;\;\;
   \nu_y = \nu_s\sin\theta + \nu_r\cos\theta
\end{align}
```

It follows that {math}`\nu_x x + \nu_y y = \nu_s s + \nu_r r`. The Jacobian of the transformation equals unity, so {math}`dx dy = dr ds`. Thus, we obtain:

```{math}
\begin{align}
&\Lambda(\nu_s \cos\theta - \nu_r\sin\theta, 
      \nu_s\sin\theta + \nu_r\cos\theta) \nonumber \\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} 
     \lambda(s \cos\theta - r\sin\theta, s\sin\theta + r\cos\theta) 
       e^{-j2\pi (\nu_s s + \nu_r r)} ds dr
\end{align}
```

Comparison with [](#eq:Q1) reveals that setting {math}`\nu_r = 0` in Λ produces {math}`Q_1`:

```{math}
Q_1(\nu_s, \theta) = \Lambda(\nu_s\cos\theta, \nu_s\sin\theta )
```

A central profile through Λ along θ yields the Fourier transform of the projection {math}`q(s,\theta)`.

(app:ramp)=
### The inverse Fourier transform of the ramp filter

% ========================

To compute the inverse Fourier transform of the ramp filter, it is useful to consider it as the difference between a rectangular and a triangular filter, as illustrated in [](#fig:rampapp2). In practical implementations, the ramp filter must be broken off at some point, which we will call {math}`W` in the following. The highest value of {math}`W` in a discrete implementation is the Nyquist frequency, which is the highest frequency that can be represented with pixels. It equals 0.5, meaning that its period is 0.5 pixels long: a (co)sine at the Nyquist frequence has a value of 1 in one pixel and a value of -1 in the next.

:::{figure} figs/fig_rampfilter2_app.pdf
:name: fig:rampapp2
:align: center
:alt: The ramp filter can be computed as the difference between a rectangular and a triangular filter

*The ramp filter can be computed as the difference between a rectangular and a triangular filter*
:::

Consider the rectangular filter {math}`{\cal R}(\omega)` of [](#fig:rampapp2): its value equals {math}`W` for frequency ω between {math}`-W` and {math}`W`, and it is zero elsewhere. Its inverse Fourier transform equals:

```{math}
\begin{align}
R(x) & =  W \int_{-\infty}^{\infty} {\cal R}(\omega) e^{2\pi j \omega x} 
           d\omega \nonumber \\
 &= W \int_{-W}^W e^{2\pi j \omega x} d\omega = W \int_{-W}^W (\cos(2\pi \omega x) + j \sin(2\pi \omega x)) d\omega 
       \nonumber \\
 &= W \int_{-W}^W \cos(2\pi \omega x) d\omega \nonumber \\
 & = W \frac{\sin(2\pi W x)}{\pi x} 
\end{align}
```

The third equality follows from the fact that the integral of a sine over an interval symmetrical about zero is always zero. The inverse Fourier of a rectangular filter is a so-called sinc function.

The convolution of a rectangular function with itself is a triangular function. More precisely, consider the rectangular function {math}`{\cal R}_2(\omega)` and the triangular function {math}`{\cal T}(\omega)` defined as:



```{math}
{\cal R}_2(\omega) = 
\begin{cases}
1 &\text{if}   -W/2 < \omega < W/2 \\
0 &\text{otherwise}
\end{cases}
```



```{math}
{\cal T}(\omega) = 
\begin{cases}
W - |\omega| &\text{if} -W < \omega < W \\
0 &\text{otherwise}
\end{cases}
```



Then it is easy to verify that the convolution of {math}`{\cal R}_2(\omega)` with itself equals {math}`{\cal T}(\omega)`:

```{math}
\begin{align}
    \int_{-\infty}^\infty {\cal R}_2(\omega') 
                          {\cal R}_2(\omega - \omega') d\omega'
&= \int_{-W/2}^{W/2} {\cal R}_2(\omega - \omega') d\omega' \nonumber\\
&= \int_{\omega-W/2}^{\omega+W/2} {\cal R}_2(\omega') d\omega' \nonumber\\
&= {\cal T}(\omega) 
\end{align}
```

Note that the rectangular filters {math}`{\cal R}_2(\omega)` and {math}`{\cal
R}(\omega)` have a different width and amplitude.

Convolution in the Fourier transform corresponds to a product in the spatial domain, so the inverse Fourier transform of a triangular filter is the square of a sinc function. Therefore, the inverse Fourier transform of the difference between the rectangular and triangular filters, i.e. the ramp filter, equals:

```{math}
:label: eq:ramp

W \frac{\sin(2 \pi W x)}{\pi x} - \frac{\sin^2(\pi W x)}{(\pi x)^2}.
```

[](#fig:rampapp) shows a plot of [](#eq:ramp). In a discrete implementation, where one only needs the function values at integer positions {math}`x = -N, -N+1, \ldots,N`, the highest possible value for {math}`W` is 0.5, the Nyquist frequency. The red dots in the figure show these discrete function values for {math}`W = 0.5`.

:::{figure} figs/fig_rampfilter_app.pdf
:name: fig:rampapp
:align: center
:alt: The inverse Fourier transform of the ramp filter, with a fine sampling (black curve). Also shown is the sampling of the usual discretisation (red dots).

*The inverse Fourier transform of the ramp filter, with a fine sampling (black curve). Also shown is the sampling of the usual discretisation (red dots).*
:::

(app:laplace)=
### The Laplace transform

% =========================

The Laplace transform is defined as:

```{math}
{\cal L} F(t) = f(s) = \int_0^\infty e^{-st} F(t) dt.
```



The Laplace transform is very useful in computations involving differential equations, because integrals and derivatives with respect to {math}`t` are transformed to very simple functions of {math}`s`. Some of its interesting features are listed below (most are easy to prove). The functions of the time are at the left, the corresponding Laplace transforms are at the right:

```{math}
:label: eq:lap1

\begin{align}
F(t)                        & \Longleftrightarrow f(s) \\
\frac{dF(t)}{dt}            & \Longleftrightarrow s f(s) - F(0) \\
e^{at} F(t)                 & \Longleftrightarrow f(s - a)\\
\int_0^t F(u) G(t - u) du   & \Longleftrightarrow f(s) g(s) 
\end{align}
```

```{math}
:label: eq:lap2

\begin{align}
\int_0^t F(u) du            & \Longleftrightarrow \frac{f(s)}{s}\\
1                           & \Longleftrightarrow \frac{1}{s}\\
e^{at}                      & \Longleftrightarrow \frac{1}{s - a} 
\end{align}
```

By combining [](#eq:lap1) and [](#eq:lap2) one obtains

```{math}
\begin{align}
\int_0^\infty F(u) e^{-a(t - u)} du & \Longleftrightarrow \frac{f(s)}{s-a}
\end{align}
```

+++
(second-appendix)=
## Second appendix

(app:expected_a_b)=
### Expectation of Poisson data contributing to a measurement

% =========================

Assume the configuration of [](#fig:expected_a_b): two radioactive sources contribute to a single measurement {math}`N`. We know the a-priori expected values {math}`\bar{a}` and {math}`\bar{b}` for each of the sources, and we know the measured count {math}`N = a + b`. The question is to compute the expected values of {math}`a` and {math}`b` given {math}`N`.

By definition, the expected value equals:

```{math}
:label: eq:appab1

E(a | a + b = N) = \frac{\sum_{a=0}^\infty p(a | a + b = N) a}
                          {\sum_{a=0}^\infty p(a | a + b = N)}
```

The denominator should be equal to 1, but if we keep it, we can apply the equation also if {math}`p` is known except for a constant factor.

The prior expectations for {math}`a` and {math}`b` are:

```{math}
p_{\bar{a}}(a) = e^{-\bar{a}} \frac{\bar{a}^a}{a!} \hspace{2cm}
  p_{\bar{b}}(b) = e^{-\bar{b}} \frac{\bar{b}^b}{b!}
```

After the measurement, we know that the first detector can only have produced {math}`a` counts if the other one happened to contribute {math}`N-a` counts. Dropping some constants this yields:

```{math}
\begin{align}
  p(a | a + b = N) \sim e^{-\bar{a}} \frac{\bar{a}^a}{a!} \;\;
                        e^{-\bar{b}} \frac{\bar{b}^{N-a}}{(N-a)!}\\
    \sim \frac{\bar{a}^a}{a!} \frac{\bar{b}^{N-a}}{(N-a)!}
\end{align}
```

Applying [](#eq:appab1) yields:

```{math}
E(a | a+b=N)
  = \frac{\sum_{a=0}^N \frac{\bar{a}^a}{a!} \frac{\bar{b}^{N-a}}{(N-a)!} a}
         {\sum_{a=0}^N \frac{\bar{a}^a}{a!} \frac{\bar{b}^{N-a}}{(N-a)!}}
```

Let us first look at the denominator:

```{math}
\sum_{a=0}^N \frac{\bar{a}^a}{a!} \frac{\bar{b}^{N-a}}{(N-a)!}
  = \frac{(\bar{a} + \bar{b})^N}{N!}
\hspace{1cm} \mbox{since } \left( \begin{array}{cc} N\\a \end{array}\right)
   = \frac{N!}{a! (N-a)!}
```

A bit more work needs to be done for the numerator:

```{math}
\begin{align}
 \sum_{a=0}^N \frac{\bar{a}^a}{a!} \frac{\bar{b}^{N-a}}{(N-a)!} a
  & = \sum_{a=1}^N \frac{\bar{a}^a}{a!} \frac{\bar{b}^{N-a}}{(N-a)!} a
    \hspace{1cm} \mbox{summation can start from 1}\\
  & = \sum_{a=1}^N \frac{\bar{a}^a}{(a-1)!} \frac{\bar{b}^{N-a}}{(N-a)!}\\
  & = \bar{a} \sum_{a=1}^N \frac{\bar{a}^{a-1}}{(a-1)!}
                             \frac{\bar{b}^{N-a}}{(N-a)!}\\
  & = \bar{a} \sum_{a=0}^{N-1} \frac{\bar{a}^a}{a!} 
                                 \frac{\bar{b}^{N-1-a}}{(N-1-a)!}\\
  & = \bar{a} \frac{(\bar{a} + \bar{b})^{N-1}}{(N-1)!}
\end{align}
```

Combining numerator and denominator results in:

```{math}
\begin{align}
  E(a | a+b=N) &= \bar{a} \frac{(\bar{a} + \bar{b})^{N-1}}{(N-1)!}
                     \frac{N!}{(\bar{a} + \bar{b})^N}\\
  &= \bar{a} \frac{N}{\bar{a} + \bar{b}}
\end{align}
```

(app:em)=
### The convergence of the EM algorithm

% =============================================

This section explains why maximizing the likelihood of the complete variables {math}`L_x` is equivalent to maximizing the likelihood {math}`L` of the observed variables {math}`Q`.

First some notations and definitions must be introduced. As in the text, Λ denotes the reconstruction, {math}`Q` the measured sinogram and {math}`X` the complete variables. We want to maximize the logarithm of the likelihood given the reconstruction:

```{math}
L(\Lambda) = \ln g(Q | \Lambda)
```

The conditional likelihood of the complete variables {math}`f(X | \Lambda)` can be written as:

```{math}
f(X | \Lambda) = k(X | Q, \Lambda) \; g(Q | \Lambda),
```

where {math}`k(X | Q, \Lambda)` is the conditional likelihood of the complete variables, given the reconstruction and the measurement. These definitions immediately imply that

```{math}
:label: eq:appmlem_f

\ln f(X | \Lambda) = L(\Lambda) + \ln k(X | Q, \Lambda).
```

The objective function we construct during the E-step is defined as

```{math}
:label: eq:appmlem_h

h(\Lambda' | \Lambda) = E\left[\ln f(X | \Lambda') | Q, \Lambda)\right],
```

which means that we write the log-likelihood of the complete variables as a function of {math}`\Lambda'`, and that we eliminate the unknown variables {math}`X` by computing the expectation based on the current reconstruction Λ. Combining [](#eq:appmlem_f) and [](#eq:appmlem_h) results in

```{math}
:label: eq:appmlem_h2

h(\Lambda' | \Lambda) = L(\Lambda') + E\left[\ln k(X | Q, \Lambda') | Q,\Lambda\right]
```

Finally, we define a generalized EM (GEM) algorithm. This is a procedure which computes a new reconstruction from the current one. The procedure will be denoted as {math}`M`. {math}`M` is a GEM-algorithm if

```{math}
h(M(\Lambda) | \Lambda) \geq h(\Lambda | \Lambda).
```

This means that we want {math}`M` to increase {math}`h`. We can be more demanding and require that {math}`M` maximizes {math}`h`; then we have a regular EM algorithm, such as the MLEM algorithm of section [](#sec:iterrecon).

Now, from equation [](#eq:appmlem_h2) we can compute what happens with {math}`L` if we apply a GEM-step to increase the value of {math}`h`:

```{math}
:label: eq:appmlem_l

\begin{align}
  L(M(\Lambda)) - L(\Lambda) &=
  h(M(\Lambda) | \Lambda) - h(\Lambda, \Lambda) \nonumber \\
  &  + E\left[\ln k(X | Q, \Lambda) | Q,\Lambda\right] 
       - E\left[\ln k(X | Q, M(\Lambda)) | Q,\Lambda\right] 
\end{align}
```

Because {math}`M` is a GEM-algorithm, we already know that {math}`h(M(\Lambda) | \Lambda) -
h(\Lambda, \Lambda)` is positive. If we can also show that

```{math}
:label: eq:appmlem_k

E\left[\ln k(X | Q, \Lambda) | Q,\Lambda\right] 
   - E\left[\ln k(X | Q, M(\Lambda)) | Q,\Lambda\right] \geq 0
```

then we have proven that every GEM-step increases the likelihood {math}`L`.\


By definition, we have

```{math}
E\left[\ln k(X | Q, \Lambda') | Q,\Lambda\right] =
     \int k(X | Q, \Lambda) \ln k(X | Q, \Lambda') dX.
```

Therefore, the left hand side of equation [](#eq:appmlem_k) can be rewritten as

```{math}
:label: eq:appmlem_k2

\begin{align}
&  \int k(X | Q, \Lambda) \ln k(X | Q, \Lambda) dX 
  - \int k(X | Q, \Lambda) \ln k(X | Q, M(\Lambda)) dX \\
&= \int k(X | Q, \Lambda)
        \ln \frac{k(X | Q, \Lambda)}{k(X | Q, M(\Lambda))} dX, 
        
\end{align}
```

with the additional requirement that 
{math}`\int k(X | Q, \Lambda) dX = \int k(X |Q, M(\Lambda)) dX = 1`. 
It turns out that [](#eq:appmlem_k2) is always positive, due to the convexity of {math}`t \ln t`. We will have a look at that now.\


Consider the function {math}`\psi(t) = t \ln t`. It is only defined for {math}`t >
0`. Here are its derivatives:

```{math}
\begin{align}
  \psi'(t) &= \frac{d \psi(t)}{dt} = 1 + \ln t\\
  \psi''(t) &= \frac{d^2 \psi(t)}{dt^2} = \frac{1}{t} > 0
\end{align}
```

The second derivative is continuous and strictly positive ({math}`t \ln t` is a convex function). Consequently, we can always find a value {math}`u` such that

```{math}
\psi(t) = \psi(1) + (t - 1) \psi'(1) + \frac{(t-1)^2}{2} \psi''(u) 
       \;\; \mbox{with} \;\; 0 < u \leq t.
```

Because {math}`\psi(1) = 0` and {math}`\psi'(1) = 1`, this becomes:

```{math}
\psi(t) = (t - 1) + \frac{(t-1)^2}{2} \psi''(u) 
       \;\; \mbox{with} \;\; 0 < u \leq t.
```

Consider now an integral of the same form as in [](#eq:appmlem_k2):

```{math}
\int f_1(x) \ln \frac{f_1(x)}{f_2(x)} dx \;\; \mbox{with} \;\;
  \int f_1(x) dx = \int f_2(x) dx = 1.
```

We can rework it such that we can exploit the convexity of {math}`t \ln t`:

```{math}
\begin{align}
  &  \int f_1(x) \ln \frac{f_1(x)}{f_2(x)} dx \nonumber\\
  &= \int \frac{f_1(x)}{f_2(x)} \ln \left( \frac{f_1(x)}{f_2(x)} \right)
        f_2(x) dx \nonumber\\
  &= \int \left[ \frac{f_1(x)}{f_2(x)} -1 + 
       \frac{1}{2}\left( \frac{f_1(x)}{f_2(x)} - 1\right)^2 
        \psi''(u(x)) \right]  f_2(x) dx \; \mbox{with} \; 0 < u(x) < \infty 
        \nonumber\\
  &= \int \left( f_1(x) - f_2(x) \right) dx + 
        \frac{1}{2} \int \left( \frac{f_1(x)}{f_2(x)} - 1 2\right)^2
        \psi''(u(x)) f_2(x) dx \;\; \geq \;\; 0
\end{align}
```

Now we have proved that the GEM-step increases {math}`L`. It still remains to be shown that the algorithm indeed converges towards the maximum likelihood solution. If you want to know really everything about it, you should read the paper by Dempster, Laird and Rubin, “Maximum likelihood from incomplete data via the EM algorithm”, *J R Statist Soc* 1977; 39; 1-38.

(app:bprojproj)=
### Backprojection of a projection of a point source

% =========================

(id-2d-parallel-projection)=
#### 2D parallel projection

% ----------------------------------

Consider a point source located in the center of the field of view. The projection is a sinogram {math}`q(s, \theta)`, given by

```{math}
q(s, \theta) = \delta(s),
```

where {math}`\delta(x)` is the delta function: {math}`\delta(x) = 1` if {math}`x = 0`, and {math}`\delta(x) = 0` if {math}`x \neq 0`. The backprojection {math}`b(x,y)` is then given by

```{math}
:label: eq:app2bp1

\begin{align}
  b(x,y) &= \int_0^\pi q(x \cos\theta + y\sin\theta, \theta)
                d\theta \nonumber\\
         &= \int_0^\pi \delta(x\cos\theta + y\sin\theta) d\theta
                
\end{align}
```

To proceed, the argument of the delta function must be changed. This can be done with the following expression:

```{math}
\delta(f(x)) = \sum_1^N \frac{\delta(x_n)}{|f'(x_n)|},
```

where {math}`f'` is the derivative of {math}`f`, and {math}`x_n, n=1 \ldots N` are the zeros of {math}`f(x)`, i.e. {math}`f(x_n) = 0`. A simple example is {math}`\delta(ax) =
\delta(x) / |a|`. Applying this to [](#eq:app2bp1) yields:

```{math}
b(x,y)  =  \int_0^\pi \frac{\delta(\theta - \theta_0)}
                              {|-x\sin\theta_0 + y\cos\theta_0|} d\theta,
```

where {math}`\theta_0` is such that {math}`x\cos\theta_0 + y\sin\theta_0 =
0`. This is satisfied if

```{math}
\cos\theta_0 = \pm \frac{y}{\sqrt{x^2+y^2}} 
       \;\;\;\mbox{and}\;\;\;
  \sin\theta_0 = \mp \frac{x}{\sqrt{x^2+y^2}},
```

which results in

```{math}
b(x,y) = \frac{1}{\sqrt{x^2 + y^2}}.
```

(id-2d-parallel-projection-with-tof)=
#### 2D parallel projection with TOF

% -------------------------------------------

Consider again the projection of a point source in the center of the field of view. With time-of-flight, the parallel projection along angle θ can be considered as a Gaussian blurring along lines with angle θ. That gives for the TOF-sinogram {math}`q(x,y,\theta)`:

```{math}
q(x,y,\theta) = \frac{1}{\sqrt{2\pi}\sigma}
               \exp(-\frac{x^2+y^2}{2 \sigma^2}) \;
              \delta(x\cos\theta + y\sin\theta),
```

where σ represents the uncertainty of the TOF-measurement. The corresponding backprojection operator is obtained by applying the same blurring to the projections, followed by integration over θ. The convolution of a Gaussian with itself is equivalent to multiplying its standard deviation with {math}`\sqrt{2}` (see appendix [](#app:convol2gauss)). One finds

```{math}
\begin{align}
  b(x,y) &= \int_0^\pi \frac{1}{2\sqrt{\pi}\sigma}
               \exp(-\frac{x^2+y^2}{4 \sigma^2}) \;
              \delta(x\cos\theta + y\sin\theta) d\theta\\
 &= \frac{1}{2\sqrt{\pi}\sigma \sqrt{x^2 + y^2}}
               \exp(-\frac{x^2+y^2}{4 \sigma^2}),
\end{align}
```

which is equivalent to equation [](#eq:TOFpsf).