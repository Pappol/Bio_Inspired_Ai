import matplotlib.pyplot as plt

gens=list(range(1,101))

best_fitness_values = [
    8.882260181819644,
    12.622245593231712,
    12.622245593231712,
    12.622245593231712,
    12.622245593231712,
    12.655643585101041,
    13.110569136175954,
    15.716465827095794,
    15.716465827095794,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.718797370659411,
    15.752087032572305,
    15.752087032572305,
    15.752087032572305,
    15.752087032572305,
    15.752087032572305,
    15.752087032572305,
    15.752087032572305,
    15.774309254687694,
    15.774309254687694,
    15.774309254687694,
    15.774309254687694,
    15.774309254687694,
    15.774309316455387,
    15.774309316455387,
    15.840975983002707,
    15.840975983002707,
    15.840975983002707,
    15.840975983002707,
    15.840975983002707,
    15.852061523072683,
    15.852061523072683,
    15.852061523072683,
    15.852061523072683,
    15.852061523072683,
    15.852087094114394,
    15.852087094114394,
    15.852087094114394,
    15.895898569503936,
    15.895898569503936,
    15.895898569503936,
    15.906984109561327,
    15.906984109561327,
    15.906984109561327,
    15.906984109561327,
    15.906984109561327,
    15.906984109561327,
    15.906984109561327,
    15.906984109561327,
    16.062355092127977,
    16.073466203239064,
    16.073466203239064,
    16.073466203239064,
    17.013349426473326,
    17.013349426473326,
    17.013349426473326,
    17.506361598941748,
    20.25079829052366,
    20.25079829052366,
    23.469294776567626,
    23.469294776567626,
    23.469294776567626,
    23.469294776567626,
    23.469294776567626,
    23.469294776567626,
    23.469294776567626,
    23.469294776567626,
    23.469294776567626,
    23.469294776567626,
    23.469294776567626,
    23.469294776567626,
    23.502612839338468,
    23.502612839338468,
    23.502612839338468,
    23.614538654652705,
    23.614538654652705,
    23.614538654652705,
    23.614538654652705,
    23.614538654652705,
    23.614538654652705,
    24.182087624103474,
    24.182087624103474,
    24.182087624103474,
    24.182087624103474,
    25.2090952655825
]

median=[
    2.1824734083526147,
    3.4760711205064343,
    3.829320614111607,
    5.641459022056724,
    4.874512567094106,
    5.114401372623407,
    6.792531541174327,
    6.383746659877843,
    6.806207367543932,
    6.7548506882825246,
    6.435519705755344,
    6.776293434313688,
    6.7548506882825246,
    7.664229508803114,
    7.103193857799505,
    8.166857509360192,
    8.085001994094235,
    7.700408370423973,
    8.440992831142678,
    8.332791948874945,
    7.80916546513018,
    8.39798583345956,
    8.124230666961305,
    8.088521654176148,
    7.122051747441702,
    8.082289064810322,
    7.370674295340558,
    7.977768234898645,
    7.829047997661931,
    8.20984588594714,
    8.11750933962394,
    8.124230666961305,
    11.825050821672473,
    8.384807789845276,
    8.095916158118387,
    8.124230666961305,
    9.732709908124502,
    10.124363229725795,
    10.06005714171156,
    8.512871517780924,
    11.681023805215723,
    9.324289671397665,
    9.408969757695917,
    9.596584726236784,
    11.707021289735302,
    10.783011073773185,
    9.641541314341259,
    11.47509133724326,
    9.956085151508592,
    8.200779339750735,
    9.859971592324273,
    9.423897974077578,
    9.889159226580865,
    9.790033024914383,
    9.502774481636866,
    8.46572910050919,
    9.600589658112057,
    10.165892329203508,
    9.910482236279607,
    9.7438210192356,
    11.428045523147151,
    11.629256243981397,
    11.488789558965252,
    8.231763260520196,
    11.708792778963389,
    10.138816730290344,
    10.138816730290344,
    13.062564059815957,
    13.045910178676802,
    13.317302073262974,
    13.12083738779466,
    13.034811853092258,
    12.457146474914023,
    12.32165927819819,
    13.43194830684142,
    8.15281231640576,
    12.87009315208018,
    12.667302073261656,
    13.328413184372769,
    13.33951153675925,
    13.686483953912159,
    13.380180745607095,
    13.443050587117547,
    13.944236991489586,
    13.43194830684142,
    14.81852912157369,
    14.85921058851849,
    15.301037202485048,
    15.097657670442132,
    16.33900687458972,
    13.526816499989115,
    16.469993714729338,
    16.667089623842596,
    16.412691010728555,
    19.102206688023738,
    19.152188509020142,
    16.661540633540863,
    18.939539426856413,
    15.622741819771875,
    17.994812607221803
]

plt.plot(gens,best_fitness_values,label="Best")
plt.plot(gens,median,label="Median")
plt.legend()
plt.grid(axis="y")
plt.show()