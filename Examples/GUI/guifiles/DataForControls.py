exampleText_2D = """\

Example 2D data for testing
Paste your own 2D data here

  X        Y
5.357    10.376
5.457    10.489
5.936    11.049
6.161    11.327 ending text is ignored
6.697    12.054
8.442    14.744
9.769    17.068
9.861    17.104
"""

exampleText_3D = """\

Example 3D data for testing
Paste your own 3D data here

    X        Y          Z
  3.017  2.175   0.0320
  2.822  2.624   0.0629
  1.784  3.144   6.570
  1.712  3.153   6.721
  2.972  2.106   0.0313
  2.719  2.542   0.0643
  2.0 2.6 4.0  ending text is ignored
  1.479  2.957   6.583
  1.387  2.963   6.744
  2.843  1.984   0.0315
  2.485  2.320   0.0639
  0.742  2.568   6.581
  0.607  2.571   6.753
"""

fittingTargetList = ['Lowest Sum Of Squared Absolute Error (SSQABS)',
                     'Lowest Sum Of Squared Log[Pred/Actual] (LNQREL)',
                     'Lowest Sum Of Squared Relative Error (SSQREL)',
                     'Lowest Sum Of Squared Orthogonal Distance (ODR)',
                     'Lowest Akaike Information Criterion (AIC)',
                     ]

exampleEquationList_2D = ['Linear Polynomial',
                          'Quadratic Polynomial',
                          'Cubic Polynomial',
                          'Witch Of Maria Agnesi A',
                          'VanDeemter Chromatography',
                          'Gamma Ray Angular Distribution (degrees) B',
                          'Exponential With Offset',
                          ]

exampleEquationList_3D = ['Linear Polynomial',
                          'Full Quadratic Polynomial',
                          'Full Cubic Polynomial',
                          'Monkey Saddle A',
                          'Gaussian Curvature Of Whitneys Umbrella A',
                          'NIST Nelson Autolog',
                          'Custom Polynomial One',
                          ]
