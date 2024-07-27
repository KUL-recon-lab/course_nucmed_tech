---
title: Appendix One
---

(app:poisson)=
# Poisson noise

% =========================

Assume that the expected amount of measured photons per unit time equals {math}`r`. Let us now divide this unit of time in a {math}`k` time intervals. If {math}`k` is sufficiently large, the time intervals are small, so the probability of detecting a photon in such an interval is small, and the probability of detecting two or more is negligible. Consequently, we can assume that in every possible measurement, only zero or one photon is detected in every interval. The probability of detecting one photon in an interval is then {math}`r /
k`. A measurement of {math}`n` photons must consist of {math}`n` intervals with one photon, and {math}`k - n` intervals with no photons. The probability of such a measurement is:

```{math}
:label: eq:poisson:1

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
# Convolution and PSF

% =========================

In section [](#sec:collimation), the collimator point spread function (PSF) was computed. The collimator PSF tells us which image is obtained for a point source at distance {math}`H` from the collimator. What happens if two point sources are positioned in front of the camera, both at the same distance {math}`H`? Since the sources and the photons don’t interact with each other, all what was said above still applies, for each of the sources. The resulting image will consist of two PSFs, each centered at the detector point closest to the point source. Where the PSFs overlap, they must be added, since the detector area in the overlap region gets photons from both sources. The same is true for three, four, or one million point sources, all located at the same distance {math}`H` from the collimator. To predict the image for a set of one million point sources, simply calculate the corresponding PSFs centered at the corresponding positions on the detector, and sum everything.

The usual mathematical description of this can be considered as a two step approach:

1.  Assume that the system is perfect: the image of a point source is a point, located on the perpendicular projection line through the point source. Mathematicians would call that “point” in the image a “Dirac impulse”. The image of two or more point sources contains simply two or more Dirac impulses, located at corresponding projection lines.\




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
# Combining resolution effects: convolution of two Gaussians

% =========================

Very often, the PSF can be well approximated as a Gaussian. This fact comes in handy if we want to combine two PSFs. For example: what is the combined effect of the intrinsic resolution (PSF of scintillation detection) and the collimator resolution (collimator PSF)?

How can two PSFs be combined? The solution is given in appendix [](#app:convolution): one of the PSFs is regarded as a collection of Dirac impulses. The second PSF must be applied to each of these pulses. So we must compute the convolution of both PSFs. This appendix shows that if both are approximately Gaussian, the convolution is easy to compute.

Let us represent the first and second PSFs as follows:

```{math}
F_1(x) = A \exp\left( -\frac{x^2}{a^2}\right)  \;\;\; \mbox{and} \;\;\;
  F_2(x) = B \exp\left( -\frac{x^2}{b^2}\right)
```

Thus, {math}`\sigma_1 = a / \sqrt{2}` and {math}`A = 1 / (\sqrt{2 \pi} \sigma_1)`, and similar for the other PSF. The convolution is then written as:



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

The integrand is a Gaussian. The center is a function of {math}`x`, but the standard deviation is not. The integral from {math}`-\infty` to ∞ of a Gaussian is a finite value, only dependent on its standard deviation. Consequently, the integral is not a function of {math}`x`. Working out the factor in front of the integral sign and combining all constants in a new constant {math}`D`, we obtain



```{math}
(F_1 \otimes F_2)(x) =  D \exp\left(-\frac{x^2}{a^2 + b^2}\right)
```



So the convolution of two Gaussians is again a Gaussian. The variance of the resulting Gaussian is simply the sum of the input variances (by definition, the variance is the square of the standard deviation).

The FWHM of a Gaussian is proportional to the standard deviation, so we obtain a very simple expression to compute the FWHM resulting from the convolution of multiple PSFs:

```{math}
\mbox{FWHM}^2 = \mbox{FWHM}_1^2 + \mbox{FWHM}_2^2 + \ldots + \mbox{FWHM}_n^2
```

(app:error)=
# Error propagation

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
## Sum or difference of two independent variables

% ----------------------------------------------

We have two variables {math}`a` and {math}`b` with mean {math}`\overline{a}` and {math}`\overline{b}` and variance {math}`\sigma_a^2` and {math}`\sigma_b^2`. We compute {math}`a \pm b` and estimate the corresponding variance {math}`\sigma_{a \pm b}^2`.

```{math}
\begin{align}
\sigma_{a \pm b}^2 &= E\left[\left((a \pm b) - (\overline{a} \pm \overline{b}) \right)^2\right]
           \nonumber\\
 &= E\left[(a-\overline{a})^2\right] + E\left[(b-\overline{b})^2\right] \pm E\left[2(a-\overline{a})(b-\overline{b})\right]
           \nonumber\\
 &= E\left[(a-\overline{a})^2\right] + E\left[(b-\overline{b})^2\right] \pm 2 E\left[(a-\overline{a})\right]E\left[(b-\overline{b})\right] \nonumber
\end{align}
```

```{math}
:label: eq:app_sumerror

\sigma_{a \pm b}^2 = \sigma_a^2 + \sigma_b^2, 
```

because the expectation of {math}`(a - \overline{a})` is zero. The expectation {math}`E\left[(a-\overline{a})(b-\overline{b})\right]` is the covariance of {math}`a` and {math}`b`. The expectation of the product is the product of the expectations if the variables are independent samples, and therefore, the covariance of independent variables is zero.

So in linear combinations the noise adds up, even if the variables are subtracted!

(product-of-two-independent-variables)=
## Product of two independent variables

% ------------------------------------

For independent variables, the expectation of the product is the product of the expectations, so we have:

```{math}
\begin{align}
 \sigma_{ab}^2 &= E\left[\left( ab - \overline{a} \overline{b}\right)^2\right] \nonumber\\
  &= E\left[a^2b^2\right] + \overline{a}^2\overline{b}^2 - E\left[2 a b \overline{a} \overline{b}\right] \nonumber
\end{align}
```

```{math}
:label: eq:app_noise_prod1

 \sigma_{ab}^2 = E\left[a^2\right] E\left[b^2\right] - \overline{a}^2 \overline{b}^2 
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
## Any function of independent variables

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
# Central slice theorem

% =================================

This appendix gives a proof of eq ([62](#fouriertheorem)) for any angle θ. The projection {math}`q(s,\theta)` can be written as

```{math}
q(s, \theta) = \int_{-\infty}^{\infty} \lambda(s \cos\theta - r\sin\theta, 
                                s \sin\theta + r\cos\theta) dr
```

The 1D Fourier transform of {math}`q(s,\theta)` along {math}`s` equals:

```{math}
 Q_1(\nu_s, \theta) = \int_{-\infty}^{\infty} q(s, \theta) e^{-j2\pi \nu_s s} ds \nonumber
```

```{math}
:label: eq:Q1

 Q_1(\nu_s, \theta) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\lambda(s\cos\theta - r\sin\theta,  s\sin\theta + r\cos\theta)e^{-j2\pi \nu_s s} dr ds
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

Comparison with [](#eq:Q1) reveals that setting {math}`\nu_r = 0` in {math}`\Lambda` produces {math}`Q_1`:

```{math}
Q_1(\nu_s, \theta) = \Lambda(\nu_s\cos\theta, \nu_s\sin\theta )
```

A central profile through {math}`\Lambda` along θ yields the Fourier transform of the projection {math}`q(s,\theta)`.

(app:ramp)=
# The inverse Fourier transform of the ramp filter

% ========================

To compute the inverse Fourier transform of the ramp filter, it is useful to consider it as the difference between a rectangular and a triangular filter, as illustrated in [](#fig:rampapp2). In practical implementations, the ramp filter must be broken off at some point, which we will call {math}`W` in the following. The highest value of {math}`W` in a discrete implementation is the Nyquist frequency, which is the highest frequency that can be represented with pixels. It equals 0.5, meaning that its period is 0.5 pixels long: a (co)sine at the Nyquist frequence has a value of 1 in one pixel and a value of -1 in the next.

:::{figure} figs/fig_rampfilter2_app.png
:width: 500px
:name: fig:rampapp2
:align: center
:alt: The ramp filter can be computed as the difference between a rectangular and a triangular filter

*The ramp filter can be computed as the difference between a rectangular and a triangular filter*
:::

Consider the rectangular filter {math}`{\mathbb{R}}(\omega)` of [](#fig:rampapp2): its value equals {math}`W` for frequency ω between {math}`-W` and {math}`W`, and it is zero elsewhere. Its inverse Fourier transform equals:

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

Note that the rectangular filters {math}`{\mathbb{R}}_2(\omega)` and 
{math}`{\mathbb{R}}(\omega)` have a different width and amplitude.

Convolution in the Fourier transform corresponds to a product in the spatial domain, so the inverse Fourier transform of a triangular filter is the square of a sinc function. Therefore, the inverse Fourier transform of the difference between the rectangular and triangular filters, i.e. the ramp filter, equals:

```{math}
:label: eq:ramp

W \frac{\sin(2 \pi W x)}{\pi x} - \frac{\sin^2(\pi W x)}{(\pi x)^2}.
```

[](#fig:rampapp) shows a plot of [](#eq:ramp). In a discrete implementation, where one only needs the function values at integer positions {math}`x = -N, -N+1, \ldots,N`, the highest possible value for {math}`W` is 0.5, the Nyquist frequency. The red dots in the figure show these discrete function values for {math}`W = 0.5`.

:::{figure} figs/fig_rampfilter_app.png
:width: 400px
:name: fig:rampapp
:align: center
:alt: The inverse Fourier transform of the ramp filter, with a fine sampling (black curve). Also shown is the sampling of the usual discretisation (red dots).

*The inverse Fourier transform of the ramp filter, with a fine sampling (black curve). Also shown is the sampling of the usual discretisation (red dots).*
:::

(app:laplace)=
# The Laplace transform

% =========================

The Laplace transform is defined as:

```{math}
{\cal L} F(t) = f(s) = \int_0^\infty e^{-st} F(t) dt.
```



The Laplace transform is very useful in computations involving differential equations, because integrals and derivatives with respect to {math}`t` are transformed to very simple functions of {math}`s`. Some of its interesting features are listed below (most are easy to prove). The functions of the time are at the left, the corresponding Laplace transforms are at the right:

```{math}
\begin{align}
F(t)                        & \Longleftrightarrow f(s) \\
\frac{dF(t)}{dt}            & \Longleftrightarrow s f(s) - F(0) \\
e^{at} F(t)                 & \Longleftrightarrow f(s - a)\\
\int_0^t F(u) du            & \Longleftrightarrow \frac{f(s)}{s}\\
1                           & \Longleftrightarrow \frac{1}{s}
\end{align}
```

```{math}
:label: eq:lap1

\int_0^t F(u) G(t - u) du  \Longleftrightarrow f(s) g(s) 
```

```{math}
:label: eq:lap2

e^{at} \Longleftrightarrow \frac{1}{s - a} 
```

By combining [](#eq:lap1) and [](#eq:lap2) one obtains

```{math}
\begin{align}
\int_0^\infty F(u) e^{-a(t - u)} du & \Longleftrightarrow \frac{f(s)}{s-a}
\end{align}
```

