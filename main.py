import cv2
import apriltag

from traffic_signs import *


detector = apriltag.Detector()

video = cv2.VideoCapture('input.mp4')

width = int(video.get(3))
height = int(video.get(4))
fps = video.get(5)
# print(width, height, fps)

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

tag_dict = {
    0: [],
    1: ['TrafficSign', Stop],
    2: ['TrafficSign', Yield],
    3: ['TrafficSign', NoRightTurn],
    4: ['TrafficSign', NoLeftTurn],
    5: ['TrafficSign', DoNotEnter],
    6: ['TrafficSign', OneWayRight],
    7: ['TrafficSign', OneWayLeft],
    8: ['TrafficSign', FourWay_Intersect],
    9: ['TrafficSign', RightT_Intersect],
    10: ['TrafficSign', LeftT_Intersect],
    11: ['TrafficSign', T_Intersect],
    12: ['TrafficSign', Pedestrian],
    13: ['TrafficSign', FourWay_Intersect],
    14: ['TrafficSign', 'FourWay_Intersect'],
    15: ['TrafficSign', 'FourWay_Intersect'],
    16: ['TrafficSign', 'FourWay_Intersect'],
    17: ['TrafficSign', 'FourWay_Intersect'],
    18: ['TrafficSign', 'FourWay_Intersect'],
    19: ['TrafficSign', 'FourWay_Intersect'],
    20: ['TrafficSign', 'Stop'],
    21: ['TrafficSign', 'Stop'],
    22: ['TrafficSign', 'Stop'],
    23: ['TrafficSign', 'Stop'],
    24: ['TrafficSign', 'Stop'],
    25: ['TrafficSign', 'Stop'],
    26: ['TrafficSign', 'Stop'],
    27: ['TrafficSign', 'Stop'],
    28: ['TrafficSign', 'Stop'],
    29: ['TrafficSign', 'Stop'],
    30: ['TrafficSign', 'Stop'],
    31: ['TrafficSign', 'Stop'],
    32: ['TrafficSign', 'Stop'],
    33: ['TrafficSign', 'Stop'],
    34: ['TrafficSign', 'Stop'],
    35: ['TrafficSign', 'Stop'],
    36: ['TrafficSign', 'Stop'],
    37: ['TrafficSign', 'Stop'],
    38: ['TrafficSign', 'Stop'],
    39: ['TrafficSign', 'Yield'],
    40: ['TrafficSign', 'NoRightTurn'],
    41: ['TrafficSign', 'NoLeftTurn'],
    42: ['TrafficSign', 'OneWayRight'],
    43: ['TrafficSign', 'OneWayLeft'],
    44: ['TrafficSign', 'FourWay_Intersect'],
    45: ['TrafficSign', 'FourWay_Intersect'],
    46: ['TrafficSign', 'FourWay_Intersect'],
    47: ['TrafficSign', 'FourWay_Intersect'],
    48: ['TrafficSign', 'FourWay_Intersect'],
    49: ['TrafficSign', 'FourWay_Intersect'],
    50: ['TrafficSign', 'FourWay_Intersect'],
    51: ['TrafficSign', 'FourWay_Intersect'],
    52: ['TrafficSign', 'FourWay_Intersect'],
    53: ['TrafficSign', 'FourWay_Intersect'],
    54: ['TrafficSign', 'FourWay_Intersect'],
    55: ['TrafficSign', 'FourWay_Intersect'],
    56: ['TrafficSign', 'FourWay_Intersect'],
    57: ['TrafficSign', 'RightT_Intersect'],
    58: ['TrafficSign', 'RightT_Intersect'],
    59: ['TrafficSign', 'RightT_Intersect'],
    60: ['TrafficSign', 'RightT_Intersect'],
    61: ['TrafficSign', 'LeftT_Intersect'],
    62: ['TrafficSign', 'LeftT_Intersect'],
    63: ['TrafficSign', 'LeftT_Intersect'],
    64: ['TrafficSign', 'LeftT_Intersect'],
    65: ['TrafficSign', 'T_Intersect'],
    66: ['TrafficSign', 'T_Intersect'],
    67: ['TrafficSign', 'T_Intersect'],
    68: ['TrafficSign', 'T_Intersect'],
    69: ['TrafficSign', 'do-not-enter'],
    70: ['TrafficSign', 'Pedestrian'],
    71: ['TrafficSign', 'Pedestrian'],
    72: ['TrafficSign', 'Pedestrian'],
    73: ['TrafficSign', 'Pedestrian'],
    74: ['TrafficSign', 'T_LightAhead'],
    75: ['TrafficSign', 'T_LightAhead'],
    76: ['TrafficSign', 'T_LightAhead'],
    77: ['TrafficSign', 'T_LightAhead'],
    78: ['TrafficSign', 'T_LightAhead'],
    79: ['TrafficSign', 'T_LightAhead'],
    80: ['TrafficSign', 'T_LightAhead'],
    81: ['TrafficSign', 'T_LightAhead'],
    82: ['TrafficSign', 'T_LightAhead'],
    83: ['TrafficSign', 'T_LightAhead'],
    84: ['TrafficSign', 'T_LightAhead'],
    85: ['TrafficSign', 'T_LightAhead'],
    86: ['TrafficSign', 'T_LightAhead'],
    87: ['TrafficSign', 'T_LightAhead'],
    88: ['TrafficSign', 'T_LightAhead'],
    89: ['TrafficSign', 'T_LightAhead'],
    90: ['TrafficSign', 'T_LightAhead'],
    91: ['TrafficSign', 'T_LightAhead'],
    92: ['TrafficSign', 'T_LightAhead'],
    93: ['TrafficSign', 'T_LightAhead'],
    94: ['TrafficSign', 'T_LightAhead'],
    95: ['TrafficSign', 'DuckCrossing'],
    96: ['TrafficSign', 'DuckCrossing'],
    97: ['TrafficSign', 'DuckCrossing'],
    98: ['TrafficSign', 'DuckCrossing'],
    99: ['TrafficSign', 'DuckCrossing'],
    100: ['TrafficSign', 'DuckCrossing'],
    101: ['TrafficSign', 'DuckCrossing'],
    102: ['TrafficSign', 'DuckCrossing'],
    103: ['TrafficSign', 'DuckCrossing'],
    104: ['TrafficSign', 'DuckCrossing'],
    105: ['TrafficSign', 'DuckCrossing'],
    106: ['TrafficSign', 'DuckCrossing'],
    107: ['TrafficSign', 'DuckCrossing'],
    108: ['TrafficSign', 'DuckCrossing'],
    109: ['TrafficSign', 'DuckCrossing'],
    110: ['TrafficSign', 'DuckCrossing'],
    111: ['TrafficSign', 'DuckCrossing'],
    112: ['TrafficSign', 'DuckCrossing'],
    113: ['TrafficSign', 'DuckCrossing'],
    114: ['TrafficSign', 'DuckCrossing'],
    115: ['TrafficSign', 'DuckCrossing'],
    116: ['TrafficSign', 'DuckCrossing'],
    117: ['TrafficSign', 'DuckCrossing'],
    118: ['TrafficSign', 'DuckCrossing'],
    119: ['TrafficSign', 'DuckCrossing'],
    120: ['TrafficSign', 'DuckCrossing'],
    121: ['TrafficSign', 'DuckCrossing'],
    122: ['TrafficSign', 'DuckCrossing'],
    123: ['TrafficSign', 'DuckCrossing'],
    124: ['TrafficSign', 'DuckCrossing'],
    125: ['TrafficSign', 'Parking'],
    126: ['TrafficSign', 'Parking'],
    127: ['TrafficSign', 'Parking'],
    128: ['TrafficSign', 'Parking'],
    129: ['TrafficSign', 'Parking'],
    130: ['TrafficSign', 'Parking'],
    131: ['TrafficSign', 'Parking'],
    132: ['TrafficSign', 'RightT_Intersect'],
    133: ['TrafficSign', 'RightT_Intersect'],
    134: ['TrafficSign', 'RightT_Intersect'],
    135: ['TrafficSign', 'RightT_Intersect'],
    136: ['TrafficSign', 'RightT_Intersect'],
    137: ['TrafficSign', 'RightT_Intersect'],
    138: ['TrafficSign', 'RightT_Intersect'],
    139: ['TrafficSign', 'RightT_Intersect'],
    140: ['TrafficSign', 'RightT_Intersect'],
    141: ['TrafficSign', 'RightT_Intersect'],
    142: ['TrafficSign', 'T_Intersect'],
    143: ['TrafficSign', 'T_Intersect'],
    144: ['TrafficSign', 'T_Intersect'],
    145: ['TrafficSign', 'T_Intersect'],
    146: ['TrafficSign', 'T_Intersect'],
    147: ['TrafficSign', 'T_Intersect'],
    148: ['TrafficSign', 'T_Intersect'],
    149: ['TrafficSign', 'T_Intersect'],
    150: ['TrafficSign', 'T_Intersect'],
    151: ['TrafficSign', 'T_Intersect'],
    152: ['TrafficSign', 'LeftT_Intersect],
    153: ['TrafficSign', 'LeftT_Intersect],
    154: ['TrafficSign', 'LeftT_Intersect],
    155: ['TrafficSign', 'LeftT_Intersect],
    156: ['TrafficSign', 'LeftT_Intersect],
    157: ['TrafficSign', 'LeftT_Intersect],
    158: ['TrafficSign', 'LeftT_Intersect],
    159: ['TrafficSign', 'LeftT_Intersect],
    160: ['TrafficSign', 'LeftT_Intersect],
    161: ['TrafficSign', 'LeftT_Intersect],
    162: ['TrafficSign', 'Stop],
    163: ['TrafficSign', 'Stop],
    164: ['TrafficSign', 'Stop],
    165: ['TrafficSign', 'Stop],
    166: ['TrafficSign', 'Stop],
    167: ['TrafficSign', 'Stop],
    168: ['TrafficSign', 'Stop],
    169: ['TrafficSign', 'Stop],
    170: ['TrafficSign', 'Stop],
    171: ['TrafficSign', 'Stop],
    172: ['TrafficSign', 'Stop],
    173: ['TrafficSign', 'Stop],
    174: ['TrafficSign', 'Stop],
    175: ['TrafficSign', 'Stop],
    176: ['TrafficSign', 'Stop],
    177: ['TrafficSign', 'Stop],
    178: ['TrafficSign', 'Stop],
    179: ['TrafficSign', 'Stop],
    180: ['TrafficSign', 'Stop],
    181: ['TrafficSign', 'Stop],
    182: ['TrafficSign', 'Stop],
    183: ['TrafficSign', 'Stop],
    184: ['TrafficSign', 'Stop],
    185: ['TrafficSign', 'Stop],
    186: ['TrafficSign', 'Stop],
    187: ['TrafficSign', 'Stop],
    188: ['TrafficSign', 'Stop],
    189: ['TrafficSign', 'Stop],
    190: ['TrafficSign', 'Stop],
    191: ['TrafficSign', 'Stop],
    192: ['TrafficSign', 'Stop],
    193: ['TrafficSign', 'Stop],
    194: ['TrafficSign', 'Stop],
    195: ['TrafficSign', 'Stop],
    196: ['TrafficSign', 'Stop],
    197: ['TrafficSign', 'FourWay_Intersect],
    198: ['TrafficSign', 'FourWay_Intersect],
    199: ['TrafficSign', 'FourWay_Intersect],
    200: ['TrafficSign', 'T_LightAhead],
    201: ['TrafficSign', 'T_LightAhead],
    202: ['TrafficSign', 'T_LightAhead],
    203: ['TrafficSign', 'T_LightAhead],
    204: ['TrafficSign', 'T_LightAhead],
    205: ['TrafficSign', 'T_LightAhead],
    206: ['TrafficSign', 'T_LightAhead],
    207: ['TrafficSign', 'T_LightAhead],
    208: ['TrafficSign', 'T_LightAhead],
    209: ['TrafficSign', 'T_LightAhead],
    210: ['TrafficSign', 'T_LightAhead],
    211: ['TrafficSign', 'T_LightAhead],
    212: ['TrafficSign', 'T_LightAhead],
    213: ['TrafficSign', 'T_LightAhead],
    214: ['TrafficSign', 'T_LightAhead],
    215: ['TrafficSign', 'T_LightAhead],
    216: ['TrafficSign', 'T_LightAhead],
    217: ['TrafficSign', 'T_LightAhead],
    218: ['TrafficSign', 'T_LightAhead],
    219: ['TrafficSign', 'T_LightAhead],
    220: ['TrafficSign', 'T_LightAhead],
    221: ['TrafficSign', 'T_LightAhead],
    222: ['TrafficSign', 'T_LightAhead],
    223: ['TrafficSign', 'T_LightAhead],
    224: ['TrafficSign', 'T_LightAhead],
    225: ['TrafficSign', 'T_LightAhead],
    226: ['TrafficSign', 'T_LightAhead],
    227: ['TrafficSign', 'T_LightAhead],
    228: ['TrafficSign', 'T_LightAhead],
    229: ['TrafficSign', 'T_LightAhead],
    230: ['T_LightAhead'],
    231: ['TrafficSign', 'FourWay_Intersect],
    232: ['TrafficSign', 'FourWay_Intersect],
    233: ['TrafficSign', 'FourWay_Intersect],
    234: ['TrafficSign', 'FourWay_Intersect],
    235: ['TrafficSign', 'RightT_Intersect],
    236: ['TrafficSign', 'T_Intersect],
    237: ['TrafficSign', 'LeftT_Intersect],
    238: ['TrafficSign', 'RightT_Intersect],
    239: ['TrafficSign', 'T_Intersect],
    240: ['TrafficSign', 'LeftT_Intersect],
    241: ['TrafficSign', 'RightT_Intersect],
    242: ['TrafficSign', 'LeftT_Intersect],
    243: ['TrafficSign', 'T_Intersect],
    244: ['TrafficSign', 'RightT_Intersect],
    245: ['TrafficSign', 'LeftT_Intersect],
    246: ['TrafficSign', 'T_Intersect],
    247: ['TrafficSign', 'T_Intersect],
    248: ['TrafficSign', 'LeftT_Intersect',
    249: ['TrafficSign', 'LeftT_Intersect],
    250: [],
    251: [],
    252: [],
    253: [],
    254: [],
    255: [],
    256: [],
    257: [],
    258: [],
    259: [],
    260: ['TrafficSign', RightT_Intersect],
    261: ['TrafficSign', RightT_Intersect],
    262: ['TrafficSign', FourWay_Intersect],
    263: ['TrafficSign', FourWay_Intersect],
    264: ['TrafficSign', FourWay_Intersect],
    265: [],
    266: [],
    267: [],
    268: [],
    269: [],
    270: [],
    271: [],
    272: [],
    273: [],
    274: [],
    275: [],
    276: [],
    277: [],
    278: [],
    279: [],
    280: [],
    281: [],
    282: [],
    283: [],
    284: [],
    285: [],
    286: [],
    287: [],
    288: [],
    289: [],
    290: [],
    291: [],
    292: [],
    293: [],
    294: [],
    295: [],
    296: [],
    297: [],
    298: [],
    299: [],
    300: ['Localization'],
    301: ['Localization'],
    302: ['Localization'],
    303: ['Localization'],
    304: ['Localization'],
    305: ['Localization'],
    306: ['Localization'],
    307: ['Localization'],
    308: ['Localization'],
    309: ['Localization'],
    310: ['Localization'],
    311: ['Localization'],
    312: ['Localization'],
    313: ['Localization'],
    314: ['Localization'],
    315: ['Localization'],
    316: ['Localization'],
    317: ['Localization'],
    318: ['Localization'],
    319: ['Localization'],
    320: ['Localization'],
    321: ['Localization'],
    322: ['Localization'],
    323: ['Localization'],
    324: ['Localization'],
    325: ['Localization'],
    326: ['Localization'],
    327: ['Localization'],
    328: ['Localization'],
    329: ['Localization'],
    330: ['Localization'],
    331: ['Localization'],
    332: ['Localization'],
    333: ['Localization'],
    334: ['Localization'],
    335: ['Localization'],
    336: ['Localization'],
    337: ['Localization'],
    338: ['Localization'],
    339: ['Localization'],
    340: ['Localization'],
    341: ['Localization'],
    342: ['Localization'],
    343: ['Localization'],
    344: ['Localization'],
    345: ['Localization'],
    346: ['Localization'],
    347: ['Localization'],
    348: ['Localization'],
    349: ['Localization'],
    350: ['Localization'],
    351: ['Localization'],
    352: ['Localization'],
    353: ['Localization'],
    354: ['Localization'],
    355: ['Localization'],
    356: ['Localization'],
    357: ['Localization'],
    358: ['Localization'],
    359: ['Localization'],
    360: ['Localization'],
    361: ['Localization'],
    362: ['Localization'],
    363: ['Localization'],
    364: ['Localization'],
    365: ['Localization'],
    366: ['Localization'],
    367: ['Localization'],
    368: ['Localization'],
    369: ['Localization'],
    370: ['Localization'],
    371: ['Localization'],
    372: ['Localization'],
    373: ['Localization'],
    374: ['Localization'],
    375: ['Localization'],
    376: ['Localization'],
    377: ['Localization'],
    378: ['Localization'],
    379: ['Localization'],
    380: ['Localization'],
    381: ['Localization'],
    382: ['Localization'],
    383: ['Localization'],
    384: ['Localization'],
    385: ['Localization'],
    386: ['Localization'],
    387: ['Localization'],
    388: ['Localization'],
    389: ['Localization'],
    390: ['Localization'],
    391: ['Localization'],
    392: ['Localization'],
    393: ['Localization'],
    394: ['Localization'],
    395: ['Localization'],
    396: ['Localization'],
    397: ['Localization'],
    398: ['Localization'],
    399: ['Localization'],
    400: ['Vehicle', 'autobot01'],
    401: ['Vehicle', 'autobot02'],
    402: ['Vehicle', 'autobot03'],
    403: ['Vehicle', 'autobot04'],
    404: ['Vehicle', 'autobot05'],
    405: ['Vehicle', 'autobot06'],
    406: ['Vehicle', 'autobot07'],
    407: ['Vehicle', 'autobot08'],
    408: ['Vehicle', 'autobot09'],
    409: ['Vehicle', 'autobot10'],
    410: ['Vehicle', 'autobot11'],
    411: ['Vehicle', 'autobot12'],
    412: ['Vehicle', 'autobot13'],
    413: ['Vehicle', 'autobot14'],
    414: ['Vehicle', 'autobot15'],
    415: ['Vehicle', 'autobot16'],
    416: ['Vehicle', 'autobot17'],
    417: ['Vehicle', 'autobot18'],
    418: ['Vehicle', 'autobot19'],
    419: ['Vehicle', 'autobot20'],
    420: ['Vehicle', 'autobot21'],
    421: ['Vehicle', 'autobot22'],
    422: ['Vehicle', 'autobot23'],
    423: ['Vehicle', 'autobot24'],
    424: ['Vehicle', 'autobot25'],
    425: ['Vehicle', 'autobot26'],
    426: ['Vehicle', 'autobot27'],
    427: ['Vehicle', 'autobot28'],
    428: ['Vehicle', 'autobot29'],
    429: ['Vehicle', 'autobot30'],
    430: ['Vehicle', 'autobot31'],
    431: ['Vehicle', 'autobot32'],
    432: ['Vehicle', 'autobot33'],
    433: ['Vehicle', 'autobot34'],
    434: ['Vehicle', 'autobot35'],
    435: ['Vehicle', 'autobot36'],
    436: ['Vehicle', 'autobot37'],
    437: ['Vehicle', 'autobot38'],
    438: ['Vehicle', 'autobot39'],
    439: ['Vehicle', 'autobot40'],
    440: ['StreetName', 'HERR AVE'],
    441: ['StreetName', 'HERR AVE'],
    442: ['StreetName', 'DUBOWSKY ST'],
    443: ['StreetName', 'DUBOWSKY ST'],
    444: ['StreetName', 'ASADA AVE'],
    445: ['StreetName', 'ASADA AVE'],
    446: ['StreetName', 'WILLIAMS ST'],
    447: ['StreetName', 'WILLIAMS ST'],
    448: ['StreetName', 'WILLIAMS ST'],
    449: ['StreetName', 'ROY AVE'],
    450: ['StreetName', 'ROY AVE'],
    451: ['StreetName', 'ROY AVE'],
    452: ['StreetName', 'HOSOI AVE'],
    453: ['StreetName', 'HOSOI AVE'],
    454: ['StreetName', 'HOSOI AVE'],
    455: ['StreetName', 'CHEN AVE'],
    456: ['StreetName', 'CHEN AVE'],
    457: ['StreetName', 'CHEN AVE'],
    458: ['StreetName', 'PERAIRE ST'],
    459: ['StreetName', 'PERAIRE ST'],
    460: ['StreetName', 'PERAIRE ST'],
    461: ['StreetName', 'KAELBLING ST'],
    462: ['StreetName', 'KAELBLING ST'],
    463: ['StreetName', 'KAELBLING ST'],
    464: ['StreetName', 'IAGNEMMA ST'],
    465: ['StreetName', 'IAGNEMMA ST'],
    466: ['StreetName', 'IAGNEMMA ST'],
    467: ['StreetName', 'BREAZEAL ST'],
    468: ['StreetName', 'BREAZEAL ST'],
    469: ['StreetName', 'BREAZEAL ST'],
    470: ['StreetName', 'TEDRAKE ST'],
    471: ['StreetName', 'TEDRAKE ST'],
    472: ['StreetName', 'TEDRAKE ST'],
    473: ['StreetName', 'FRAZZOLI ST'],
    474: ['StreetName', 'FRAZZOLI ST'],
    475: ['StreetName', 'FRAZZOLI ST'],
    476: ['StreetName', 'KARAMAN ST'],
    477: ['StreetName', 'KARAMAN ST'],
    478: ['StreetName', 'KARAMAN ST'],
    479: ['StreetName', 'KARAMAN ST'],
    480: ['StreetName', 'KARAMAN ST'],
    481: ['StreetName', 'RUS AVE'],
    482: ['StreetName', 'RUS AVE'],
    483: ['StreetName', 'RUS AVE'],
    484: ['StreetName', 'RUS AVE'],
    485: ['StreetName', 'RUS AVE'],
    486: ['StreetName', 'LEONARD ST'],
    487: ['StreetName', 'LEONARD ST'],
    488: ['StreetName', 'LEONARD ST'],
    489: ['StreetName', 'LEONARD ST'],
    490: ['StreetName', 'LEONARD ST'],
    491: ['StreetName', 'LEONARD ST'],
    492: ['StreetName', 'LEONARD ST'],
    493: ['StreetName', 'HOW AVE'],
    494: ['StreetName', 'HOW AVE'],
    495: ['StreetName', 'HOW AVE'],
    496: ['StreetName', 'HOW AVE'],
    497: ['StreetName', 'HOW AVE'],
    498: ['StreetName', 'HOW AVE'],
    499: ['StreetName', 'HOW AVE'],
    500: ['StreetName', 'FRAZZOLI ST'],
    501: ['StreetName', 'TEDRAKE ST'],
    502: ['StreetName', 'ASADA AVE'],
    503: ['StreetName', 'BREAZEAL ST'],
    504: ['StreetName', 'DUBOWSKY ST'],
    505: ['StreetName', 'HERR AVE'],
    506: ['StreetName', 'HOBURG ST'],
    507: ['StreetName', 'HOGAN AVE'],
    508: ['StreetName', 'IAGNEMMA ST'],
    509: ['StreetName', 'KAELBLING ST'],
    510: ['StreetName', 'LOZANO ST'],
    511: ['StreetName', 'KIM AVE'],
    512: ['StreetName', 'REIF AVE'],
    513: ['StreetName', 'WALTZ AVE'],
    514: ['StreetName', 'PERAIRE ST'],
    515: ['StreetName', 'CHANDRA ST'],
    516: ['StreetName', 'KASAN ST'],
    517: ['StreetName', 'MICALI ST'],
    518: ['StreetName', 'CHEN AVE'],
    519: ['StreetName', 'HOSOI AVE'],
    520: ['StreetName', 'RUS AVE'],
    521: ['StreetName', 'HOW AVE'],
    522: ['StreetName', 'ROY AVE'],
    523: ['StreetName', 'SHAH AVE'],
    524: ['StreetName', 'WILLIAMS ST'],
    525: ['StreetName', 'LEONARD ST'],
    526: ['StreetName', 'BROOKS ST'],
    527: ['StreetName', 'KARAMAN ST'],
    528: ['StreetName', 'MILFORD ST.'],
    529: ['StreetName', 'TIDOR ST.'],
    530: ['StreetName', 'BARFOOT ST.'],
    531: ['StreetName', 'DUDEK ST.'],
    532: ['StreetName', 'FORBES AVE.'],
    533: ['StreetName', 'PINEAU AVE.'],
    534: ['StreetName', 'KELLY ST.'],
    535: ['StreetName', 'URTASUN RD.'],
    536: ['StreetName', 'FIDLER ST.'],
    537: ['StreetName', 'WASLANDER AVE.'],
    538: ['StreetName', 'JENKIN AVE.'],
    539: ['StreetName', 'VAUGHAN ST.'],
    540: ['StreetName', 'BACHMAYER ST.'],
    541: ['StreetName', 'SHARF ST.'],
    542: ['StreetName', 'SHOELLIG ST.'],
    543: ['StreetName', 'SREBRO ST.'],
    544: ['StreetName', 'CHUZHOY ST.'],
    545: ['StreetName', 'GIMPEL AVE.'],
    546: ['StreetName', 'LIVNAROVIC ST.'],
    547: ['StreetName', 'MCALLESTER ST.'],
    548: ['StreetName', 'TULSIANI ST.'],
    549: ['StreetName', 'MAKARYCHEV ST.'],
    550: ['StreetName', 'BLUM ST.'],
    551: ['StreetName', 'FURUI ST.'],

}


def fill_dict(id: int) -> None:
    tag_dict[id] = ''


while True:
    ret, img = video.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        results = detector.detect(gray)

        for result in results:

            # draw the bounding box of the AprilTag detection
            points = result.corners
            points = [tuple(map(int, point)) for point in points]

            cv2.line(img, points[0], points[1], (0, 255, 0), 2)
            cv2.line(img, points[1], points[2], (0, 255, 0), 2)
            cv2.line(img, points[2], points[3], (0, 255, 0), 2)
            cv2.line(img, points[3], points[0], (0, 255, 0), 2)

            # draw the center (x, y)-coordinates of the AprilTag
            '''(cX, cY) = (int(result.center[0]), int(result.center[1]))
            cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)'''

            tag_id = result.tag_id
            # fill_dict(tag_id)

            cv2.putText(img, str(tag_id), (points[3][0], points[3][1] + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # out.write(img)
        cv2.imshow('DuckietownVideo', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# print(tag_dict)
video.release()
# out.release()
cv2.destroyAllWindows()
