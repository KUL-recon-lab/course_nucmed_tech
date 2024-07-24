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