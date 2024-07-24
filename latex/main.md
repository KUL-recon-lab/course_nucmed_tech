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