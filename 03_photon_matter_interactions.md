---
title: Interaction of photons with matter
---

In nuclear medicine, photon energy ranges roughly from 60 to 600 keV. For example, {sup}`99m`Tc has an energy of 140 keV. This corresponds to a wave length of 9 pm and a frequency of 3.4 Hz. 
%At such energies, γ photons behave like particles rather than like waves.

At these energies, the dominating interactions of photons with matter are photon-electron interactions: Compton scatter and photo-electric effect. As shown in [](#fig:foto_compton_pair), the dominating interaction is a function of energy and electron number. For typical nuclear medicine energies, Compton scatter dominates in light materials (such as water and human tissue), and photo-electric effect dominates in high density materials. Pair production (conversion of a photon in an electron and a positron) is excluded for energies below 1022 keV, since each of the particles has a mass of 511 keV. Rayleigh scatter (absorption and re-emission of (all or a fraction of) the absorbed energy as a photon in a different direction) has a low probability and its effect can be ignored in PET and SPECT imaging.


:::{figure} figs/fig_foto_compton_pair.png
:name: fig:foto_compton_pair
:width: 400px
:align: center
:alt: Dominating interaction as a function of electron number Z and photon energy.

*Dominating interaction as a function of electron number Z and photon energy.*
:::

(photo-electric-effect)=
# Photo-electric effect

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

A photon “hits” an electron, usually from an inner shell (strong binding energy). The electron absorbs all the energy of the photon. If that energy is higher than the binding energy of the electron, the electron escapes from its atom. Its kinetic energy is the difference between the absorbed energy and the binding energy. In a dense material, this photo-electron will collide with electrons from other atoms, and will lose energy in each collision, until no kinetic energy is left.

As a result, there is now a electron vacancy in the atom, which may be filled by an electron from a higher energy state. The difference in binding energy of the two states must be released. This can be done by emitting a photon. Alternatively, the energy can be used by another electron with low binding energy to escape from the atom.

In both cases, the photon is completely eliminated.

The probability of a photo-electric interaction is approximately proportional to {math}`Z^3 / E^3`, where {math}`Z` is the atomic number of the material, and {math}`E` is the energy of the photon. So the photo-electric effect is particularly important for low energy radiation and for dense materials.

(sec:compton_scatter)=
# Compton scatter

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

:::{figure} figs/fig_compton_scatter.png
:name: fig:compton_scatter
:width: 300px
:align: center
:alt: Compton scatter can be regarded as an elastic collision between a photon and an electron.

*Compton scatter can be regarded as an elastic collision between a photon and an electron.*
:::

Compton scatter can be regarded as an elastic collision between a photon and an electron. This occurs with loosely bound electrons (outer shell), which have a binding energy that is negligible compared to the energy of the incident photon. The term “elastic” means that total kinetic energy before and after collision is the same. As in any collision, the momentum is preserved as well. Applying equations for the conservation of momentum and energy (with relativistic corrections) results in the following relation between the photon energy before and after the collision:

```{math}
:label: eq:jn_compton_energy

E'_\gamma \;\;=\;\; E_\gamma \frac{1}{1 
     + \displaystyle\frac{E_\gamma}{m_e c^2} (1 - \cos\theta)} 
   \;\; = \;\; E_\gamma \; P(E_\gamma, \theta)
```

with

```{math}
\begin{align}
            E'_\gamma &= \mbox{energy after collision}\\
            E_\gamma  &= \mbox{energy before collision}\\
            m_e       &= \mbox{electron rest mass}\\
            \theta    &= \mbox{scatter angle}
\end{align}
```




The expression {math}`m_e c^2` is the energy available in the mass of the electron, which equals 511 keV. For a scatter angle θ = 0, the photon loses no energy and it is not deviated from its original direction: nothing happened. The loss of energy increases with θ and is maximum for an angle of 180º. The probability that a photon will interact at all with an electron depends on the energy of the photon. If the interaction takes place, each scatter angle has its own probability, and this probability is proportional to the differential cross section, given by the Klein-Nishina equation:

```{math}
:label: eq:kleinnishina

\frac{d\sigma}{d\Omega} = \frac{1}{2} r_e^2 \; P(E_\gamma, \theta)^2
    \left( P(E_\gamma, \theta) + \frac{1}{P(E_\gamma, \theta)} - \sin^2\theta \right),
```

where {math}`r_e` is the classical electron radius and {math}`P(E_\gamma, \theta)` is defined above. The cross section σ has the unit of area, Ω is the solid angle. Integrating over Ω would produce the total cross section for Compton scatter. For that integration, {math}`d\Omega` can be written as {math}`2 \pi \sin\theta \,d\theta` [^dBuExnTevh]
[^dBuExnTevh]: If you are not sure why, this is explained in the derivation of equation [](#eq:wellcounter). 

The differential cross section [](#eq:kleinnishina) is shown for a few incoming photon energies in [](#fig:kleinnishina). For higher energies, smaller scatter angles become increasingly likely.

:::{figure} figs/fig_klein_nishina.png
:name: fig:kleinnishina
:width: 350px
:align: center
:alt: The differential cross section as a function of the scattering angle for a few photon energies. Figure from Wikipedia (https://en.wikipedia.org/wiki/Klein-Nishina_formula).

*The scattering-angle distribution for a few photon energies. Figure from Wikipedia (https://en.wikipedia.org/wiki/Klein-Nishina\_formula).*
:::

The probability of a Compton decreases very slowly with increasing {math}`E` (see [](#fig:atten_water)) and with increasing {math}`Z`.

Because the energy of the photon after scattering is less than before, Compton scatter is sometimes also called “inelastic scattering”.

%(rayleigh-scatter)=
%# Rayleigh scatter
%
%Rayleigh scattering or coherent scattering can be regarded as the collision between a photon and an entire atom. Because of the huge mass of the atom, the photon is deflected from its original trajectory without any noticeable loss of energy (replace {math}`m_e c^2` with {math}`\infty` in [](#eq:jn_compton_energy)). Rayleigh scattering contributes only significantly at low energies, and can be safely ignored in typical nuclear medicine applications. Because the energy of the photon after scattering is the same as before, this effect is also called “elastic scattering”.

(attenuation)=
# Attenuation

:::{figure} figs/fig_atten_water.png
:name: fig:atten_water
:align: center
:width: 400px
:alt: Photon attenuation in water as a function of photon energy. The photo-electric component decreases approximately with (Z/E)^3 (of course, Z is a constant here). The Compton components varies slowly.

*Photon attenuation in water as a function of photon energy. The photo-electric component decreases approximately with {math}`(Z/E)^3` (of course, {math}`Z` is a constant here). The Compton components varies slowly.*
:::

The *linear attenuation coefficient* μ is defined as the probability of interaction per unit length (unit: cm{sup}`-1`). 
[](#fig:atten_water) shows the mass attenuation coefficients as a function of energy in water. Multiply the mass attenuation coefficient with the mass density to obtain the linear attenuation coefficient. When photons are traveling in a particular direction through matter, their number will gradually decrease, since some of them will interact with an electron and get absorbed (photo-electric effect) or deviated (Compton scatter) into another direction. By definition, the fraction that is eliminated over distance {math}`ds` equals {math}`\mu(s) N(s)`:

```{math}
:label: eq:diff_atten

dN(s) = - \mu(s) N(s) ds.
```

If initially {math}`N(a)` photons are emitted in point {math}`s = a` along the {math}`s`-axis, the number of photons {math}`N(d)` we expect to arrive in the detector at position {math}`s = d` is obtained by integrating [](#eq:diff_atten):

```{math}
:label: eq:spectatten

N(d) = N(a) \  e^{- \int_a^d \mu(s) ds}.
```

Obviously, the attenuation of a photon depends on where it has been emitted.

:::{figure} figs/fig_jnpetatten.png
:width: 300px
:name: fig:jn_petatten
:align: center
:alt: Positron emitting point source in a non-uniform attenuator.

*Positron emitting point source in a non-uniform attenuator.*
:::

For positron emission, a pair of photons need to be detected. Since the fate of both photons is independent, the detection probabilities must be multiplied. Assume that one detector is positioned in {math}`s = d_1`, the second one in {math}`s = d_2`, and a point source in {math}`s = a`, somewhere between the two detectors. Assume further that during a measurement, {math}`N(a)` photon pairs were emitted along the {math}`s`-axis ([](#fig:jn_petatten)). The number of detected pairs then is:

```{math}
N(d_1,d_2) = N(a)  e^{- \int_{d_1}^a \mu(s) ds} e^{- \int_a^{d_2} \mu(s) ds}
```

```{math}
:label: eq:petatten
   N(d_1,d_2) = N(a)  e^{- \int_{d_1}^{d_2} \mu(s) ds}.
```

Equation [](#eq:petatten) shows that for PET, the effect of attenuation is independent of the position along the line of detection.

Photon-electron interactions will be more likely if there are more electrons per unit length. So dense materials (with lots of electrons per atom) have a high linear attenuation coefficient.

