from units.models import Device
from users.models import Account

data = {
    "SHEET1": [
        {
            "CODE": "4Y28",
            "GROUP": "THOR",
            "NAME": "C1X-793",
            "DATETIME": "220506120412"
        },
        {
            "CODE": "4Y2B",
            "GROUP": "RENTANOR",
            "NAME": "T9X-802",
            "DATETIME": "220506120315"
        },
        {
            "CODE": "4Y2D",
            "GROUP": "MAD.JUNI",
            "NAME": "C2Y-991",
            "DATETIME": "220506093645"
        },
        {
            "CODE": "4Y2E",
            "GROUP": "RENTING",
            "NAME": "BKT-645",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "4Y2J",
            "GROUP": "THOR",
            "NAME": "C5X-763",
            "DATETIME": "220506114024"
        },
        {
            "CODE": "4Y2K",
            "GROUP": "MAFISA",
            "NAME": "AUI-782",
            "DATETIME": "220425084830"
        },
        {
            "CODE": "4Y2L",
            "GROUP": "HILARIO",
            "NAME": "BER-783",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "4Y37",
            "GROUP": "JVL",
            "NAME": "T9C-997",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "4Y38",
            "GROUP": "T.SANTOS",
            "NAME": "BKM-849",
            "DATETIME": "220506114809"
        },
        {
            "CODE": "4Y39",
            "GROUP": "REDISE",
            "NAME": "D4M-903",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "4Y51",
            "GROUP": "MANDUJAN",
            "NAME": "F7Q-985",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "4Y57",
            "GROUP": "SELGAS",
            "NAME": "AAY-861",
            "DATETIME": "220506120039"
        },
        {
            "CODE": "4Y5A",
            "GROUP": "TICLAVIL",
            "NAME": "AFN-933",
            "DATETIME": "220506120115"
        },
        {
            "CODE": "4Y5C",
            "GROUP": "FAMESA",
            "NAME": "AVX-918",
            "DATETIME": "220405102548"
        },
        {
            "CODE": "4Y5E",
            "GROUP": "VILCA",
            "NAME": "F2T-826",
            "DATETIME": "220506120206"
        },
        {
            "CODE": "4Y5F",
            "GROUP": "NEGERIB",
            "NAME": "AUZ-798",
            "DATETIME": "220506120318"
        },
        {
            "CODE": "4Y5H",
            "GROUP": "HERMES",
            "NAME": "BMA-737",
            "DATETIME": "220506105433"
        },
        {
            "CODE": "4Y5P",
            "GROUP": "THOR",
            "NAME": "D4D-812",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "4Y5Q",
            "GROUP": "AYBAR",
            "NAME": "BAW-942",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "4Y5V",
            "GROUP": "T.VICKY",
            "NAME": "BJL-851",
            "DATETIME": "220506115327"
        },
        {
            "CODE": "4Y64",
            "GROUP": "SAN MART",
            "NAME": "C-92",
            "DATETIME": "220506114315"
        },
        {
            "CODE": "4Y67",
            "GROUP": "VILCA",
            "NAME": "C1V-764",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "4Y6A",
            "GROUP": "THOR",
            "NAME": "B7E-815",
            "DATETIME": "220506115512"
        },
        {
            "CODE": "4Y6C",
            "GROUP": "SERVINSA",
            "NAME": "APR-608",
            "DATETIME": "220506113854"
        },
        {
            "CODE": "5MR9",
            "GROUP": "T.VICKYV",
            "NAME": "AZY-789",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "5MRB",
            "GROUP": "RENPA",
            "NAME": "AVU-765",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "5MRD",
            "GROUP": "MYI GLO",
            "NAME": "T2J-937",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "5MRE",
            "GROUP": "A&J",
            "NAME": "BAG-844",
            "DATETIME": "220505195024"
        },
        {
            "CODE": "5MRF",
            "GROUP": "CASTRO",
            "NAME": "BDK-670",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "5MRG",
            "GROUP": "A&J",
            "NAME": "BAH-847",
            "DATETIME": "220506083827"
        },
        {
            "CODE": "5MRM",
            "GROUP": "A&J",
            "NAME": "BAG-923",
            "DATETIME": "220506113524"
        },
        {
            "CODE": "5MRS",
            "GROUP": "PROCARGO",
            "NAME": "F5N-719",
            "DATETIME": "220506115745"
        },
        {
            "CODE": "5MRT",
            "GROUP": "TEIROJAS",
            "NAME": "BAI-800",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "5MRU",
            "GROUP": "ENERLETR",
            "NAME": "BAB-907",
            "DATETIME": "220506113039"
        },
        {
            "CODE": "5MRW",
            "GROUP": "ENERLETR",
            "NAME": "BAC-772",
            "DATETIME": "220506120100"
        },
        {
            "CODE": "5MRX",
            "GROUP": "ENERLETR",
            "NAME": "BAB-900",
            "DATETIME": "220506120224"
        },
        {
            "CODE": "5MRY",
            "GROUP": "ENERLETR",
            "NAME": "BAC-830",
            "DATETIME": "220502200409"
        },
        {
            "CODE": "5MS0",
            "GROUP": "ENERLETR",
            "NAME": "BAC-805",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "5MS1",
            "GROUP": "ENERLETR",
            "NAME": "BAB-923",
            "DATETIME": "220506101424"
        },
        {
            "CODE": "5MS3",
            "GROUP": "ENERLETR",
            "NAME": "BAB-922",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "5MS6",
            "GROUP": "ENERLETR",
            "NAME": "BAC-773",
            "DATETIME": "220419185336"
        },
        {
            "CODE": "5MS7",
            "GROUP": "ENERLETR",
            "NAME": "BAC-933",
            "DATETIME": "220506120309"
        },
        {
            "CODE": "5MS8",
            "GROUP": "MOVIL.GA",
            "NAME": "D0Z-922",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "5MSA",
            "GROUP": "TICLAVIL",
            "NAME": "ALD-974",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "5MSB",
            "GROUP": "ENERLETR",
            "NAME": "BAC-854",
            "DATETIME": "220506120412"
        },
        {
            "CODE": "5MSC",
            "GROUP": "ENERLETR",
            "NAME": "BAC-886",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "5MSD",
            "GROUP": "A&J",
            "NAME": "BAH-732",
            "DATETIME": "220506034651"
        },
        {
            "CODE": "5MSE",
            "GROUP": "A&J",
            "NAME": "BAH-803",
            "DATETIME": "220506120121"
        },
        {
            "CODE": "5MSG",
            "GROUP": "ENERLETR",
            "NAME": "BAB-947",
            "DATETIME": "220327165033"
        },
        {
            "CODE": "5MSH",
            "GROUP": "A&J",
            "NAME": "BAG-800",
            "DATETIME": "220506043918"
        },
        {
            "CODE": "5MSJ",
            "GROUP": "A&J",
            "NAME": "BAH-866",
            "DATETIME": "220106095400"
        },
        {
            "CODE": "5MSM",
            "GROUP": "ENERLETR",
            "NAME": "BAC-887",
            "DATETIME": "220505125612"
        },
        {
            "CODE": "5MSP",
            "GROUP": "ENERLETR",
            "NAME": "BAC-759",
            "DATETIME": "220506094727"
        },
        {
            "CODE": "5MSS",
            "GROUP": "ENERLETR",
            "NAME": "BJT-176",
            "DATETIME": "220505132406"
        },
        {
            "CODE": "5MSU",
            "GROUP": "ENERLETR",
            "NAME": "BAC-803",
            "DATETIME": "220506091524"
        },
        {
            "CODE": "5MSY",
            "GROUP": "ENERLETR",
            "NAME": "BAD-719",
            "DATETIME": "220428120351"
        },
        {
            "CODE": "5MSZ",
            "GROUP": "TICLAVIL",
            "NAME": "AZP-812",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "5MT0",
            "GROUP": "ENERLETR",
            "NAME": "BAC-760",
            "DATETIME": "220506120127"
        },
        {
            "CODE": "5MT3",
            "GROUP": "ENERLETR",
            "NAME": "BAC-806",
            "DATETIME": "220506120115"
        },
        {
            "CODE": "5MT4",
            "GROUP": "MAINQUI",
            "NAME": "AZX-903",
            "DATETIME": "220506113000"
        },
        {
            "CODE": "5MTB",
            "GROUP": "ENERLETR",
            "NAME": "BAC-831",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "5MTC",
            "GROUP": "ENERLETR",
            "NAME": "BAC-829",
            "DATETIME": "220505123157"
        },
        {
            "CODE": "5MTE",
            "GROUP": "ENERLETR",
            "NAME": "BAB-906",
            "DATETIME": "220506120324"
        },
        {
            "CODE": "5MTL",
            "GROUP": "FAMESA",
            "NAME": "AZW-718",
            "DATETIME": "220420135821"
        },
        {
            "CODE": "5MTV",
            "GROUP": "LINCUNA",
            "NAME": "AZU-722",
            "DATETIME": "220506061139"
        },
        {
            "CODE": "5MTY",
            "GROUP": "GILDEMEI",
            "NAME": "AXC-593",
            "DATETIME": "220506113845"
        },
        {
            "CODE": "5MU0",
            "GROUP": "FAMESA",
            "NAME": "AFZ-890",
            "DATETIME": "220506102436"
        },
        {
            "CODE": "5MU3",
            "GROUP": "FAMESA",
            "NAME": "ABU-884",
            "DATETIME": "220422161718"
        },
        {
            "CODE": "5RK8",
            "GROUP": "SALCEDO",
            "NAME": "D8I-814",
            "DATETIME": "220505170754"
        },
        {
            "CODE": "5RKB",
            "GROUP": "STA-ROSA",
            "NAME": "ANR-997",
            "DATETIME": "220506095042"
        },
        {
            "CODE": "5RKC",
            "GROUP": "TELRED",
            "NAME": "IMVS9",
            "DATETIME": "220331095709"
        },
        {
            "CODE": "5RKL",
            "GROUP": "ABAD",
            "NAME": "B4C-984",
            "DATETIME": "220423165100"
        },
        {
            "CODE": "5RKM",
            "GROUP": "SMIGUELG",
            "NAME": "V0B-700",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "5RKS",
            "GROUP": "MACROSIG",
            "NAME": "BAC-852",
            "DATETIME": "220506091548"
        },
        {
            "CODE": "5RKT",
            "GROUP": "STA-ROSA",
            "NAME": "ANS-972",
            "DATETIME": "220506110103"
        },
        {
            "CODE": "5RKY",
            "GROUP": "NOR OIL",
            "NAME": "T4U-845",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "5RKZ",
            "GROUP": "SAN MART",
            "NAME": "B4F-833",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "5RL1",
            "GROUP": "SAN MART",
            "NAME": "T3R-808",
            "DATETIME": "220505190136"
        },
        {
            "CODE": "5RL5",
            "GROUP": "RENTINLE",
            "NAME": "BLM-565",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "5RL9",
            "GROUP": "CORINSER",
            "NAME": "A5X-296",
            "DATETIME": "220506110500"
        },
        {
            "CODE": "5RLA",
            "GROUP": "RENTINLE",
            "NAME": "BLM-098",
            "DATETIME": "220506120348"
        },
        {
            "CODE": "5RLD",
            "GROUP": "MACROSIG",
            "NAME": "ASZ-700",
            "DATETIME": "220506112815"
        },
        {
            "CODE": "5RLE",
            "GROUP": "SAN MART",
            "NAME": "BDT-938 ",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "5RLF",
            "GROUP": "RENTINLE",
            "NAME": "BLL-312",
            "DATETIME": "220506100927"
        },
        {
            "CODE": "5RLG",
            "GROUP": "CARTER",
            "NAME": "BJI-828",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "5RLR",
            "GROUP": "BIDDLE",
            "NAME": "BDW-862",
            "DATETIME": "220506112336"
        },
        {
            "CODE": "5RLS",
            "GROUP": "RENTINLE",
            "NAME": "BLM-099",
            "DATETIME": "220506113742"
        },
        {
            "CODE": "5RLT",
            "GROUP": "RENTINLE",
            "NAME": "BLL-344",
            "DATETIME": "220506071133"
        },
        {
            "CODE": "5RLU",
            "GROUP": "RENTINLE",
            "NAME": "BLK-672",
            "DATETIME": "220506111342"
        },
        {
            "CODE": "5RLX",
            "GROUP": "RENTINLE",
            "NAME": "BLK-458",
            "DATETIME": "220506115024"
        },
        {
            "CODE": "5RM1",
            "GROUP": "LISTOTAX",
            "NAME": "BEH-289",
            "DATETIME": "220506113642"
        },
        {
            "CODE": "5RM2",
            "GROUP": "RENTINLE",
            "NAME": "BLK-460",
            "DATETIME": "220506091109"
        },
        {
            "CODE": "5RM5",
            "GROUP": "SMIGUELG",
            "NAME": "V8Z-933",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "5RM7",
            "GROUP": "RENTINLE",
            "NAME": "BLM-576",
            "DATETIME": "220506093703"
        },
        {
            "CODE": "5RMA",
            "GROUP": "LISTOTAX",
            "NAME": "BLB-552",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "5RMB",
            "GROUP": "LISTOTAX",
            "NAME": "BEI-084",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "5RMD",
            "GROUP": "RENTINLE",
            "NAME": "BLN-032",
            "DATETIME": "220506022057"
        },
        {
            "CODE": "5RMF",
            "GROUP": "SISSA",
            "NAME": "BAN-892",
            "DATETIME": "220427163145"
        },
        {
            "CODE": "5RMH",
            "GROUP": "SISSA",
            "NAME": "BBF-948",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "5RMJ",
            "GROUP": "RENTINLE",
            "NAME": "BLN-029",
            "DATETIME": "220506113521"
        },
        {
            "CODE": "5RMN",
            "GROUP": "LISTOTAX",
            "NAME": "BEH-285",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "5RMP",
            "GROUP": "A&S OPER",
            "NAME": "POSEIDON",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "5RMQ",
            "GROUP": "LISTOTAX",
            "NAME": "BLL-106",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "5RMR",
            "GROUP": "RENTINLE",
            "NAME": "BLK-459",
            "DATETIME": "220506115818"
        },
        {
            "CODE": "5RMS",
            "GROUP": "SOLHYM",
            "NAME": "BFH-832",
            "DATETIME": "220506114818"
        },
        {
            "CODE": "5RMT",
            "GROUP": "LISTOTAX",
            "NAME": "BEH-374",
            "DATETIME": "220102104436"
        },
        {
            "CODE": "5RMU",
            "GROUP": "RENTINLE",
            "NAME": "BLL-659",
            "DATETIME": "220506094106"
        },
        {
            "CODE": "5RMZ",
            "GROUP": "RENTINLE",
            "NAME": "BLM-566",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "5RN0",
            "GROUP": "RENTINLE",
            "NAME": "BLK-679",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "5RN3",
            "GROUP": "OROGAS",
            "NAME": "F0R-999",
            "DATETIME": "220504194633"
        },
        {
            "CODE": "5RN4",
            "GROUP": "HERACLIO",
            "NAME": "C9A-456",
            "DATETIME": "220505214709"
        },
        {
            "CODE": "5RN6",
            "GROUP": "RENTINLE",
            "NAME": "BHA-543",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "5RN9",
            "GROUP": "REPARTO",
            "NAME": "BAP-842",
            "DATETIME": "220506003939"
        },
        {
            "CODE": "5RNA",
            "GROUP": "RENTANOR",
            "NAME": "T8M-803",
            "DATETIME": "220425161518"
        },
        {
            "CODE": "5RNG",
            "GROUP": "RENTINLE",
            "NAME": "BHA-248",
            "DATETIME": "220303092624"
        },
        {
            "CODE": "5RNH",
            "GROUP": "REPARTO",
            "NAME": "BAO-854",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "5RNL",
            "GROUP": "ORBIS",
            "NAME": "BAQ-948",
            "DATETIME": "220506120300"
        },
        {
            "CODE": "5RNP",
            "GROUP": "REPARTO",
            "NAME": "BAP-821",
            "DATETIME": "220331140515"
        },
        {
            "CODE": "5RNQ",
            "GROUP": "REPARTO",
            "NAME": "BAO-893",
            "DATETIME": "220329004742"
        },
        {
            "CODE": "5RNT",
            "GROUP": "RENTINLE",
            "NAME": "BHB-113",
            "DATETIME": "220506034948"
        },
        {
            "CODE": "5RNU",
            "GROUP": "VILCA",
            "NAME": "BAP-809",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "5RNW",
            "GROUP": "FERREYRO",
            "NAME": "S01015",
            "DATETIME": "220506112721"
        },
        {
            "CODE": "5RNY",
            "GROUP": "SLI",
            "NAME": "ACB-836",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "5RNZ",
            "GROUP": "SMIGUELG",
            "NAME": "APX-981",
            "DATETIME": "220506120121"
        },
        {
            "CODE": "5RP7",
            "GROUP": "T.BALDEO",
            "NAME": "F4F-960",
            "DATETIME": "220506113557"
        },
        {
            "CODE": "5RP9",
            "GROUP": "SOUTHERN",
            "NAME": "A0I-919",
            "DATETIME": "220506113657"
        },
        {
            "CODE": "5RPA",
            "GROUP": "T.SANTAM",
            "NAME": "B9N-880",
            "DATETIME": "220506115248"
        },
        {
            "CODE": "5RPB",
            "GROUP": "REPARTO",
            "NAME": "BAO-892",
            "DATETIME": "220506114430"
        },
        {
            "CODE": "5RPC",
            "GROUP": "MOVILGAS",
            "NAME": "W3R-987",
            "DATETIME": "220506002024"
        },
        {
            "CODE": "5RPE",
            "GROUP": "MAD.JUNI",
            "NAME": "AHC-948",
            "DATETIME": "220506114827"
        },
        {
            "CODE": "5RPG",
            "GROUP": "MOVILGAS",
            "NAME": "BAB-830",
            "DATETIME": "220506114339"
        },
        {
            "CODE": "5RPL",
            "GROUP": "REPARTO",
            "NAME": "BAO-786",
            "DATETIME": "220506114957"
        },
        {
            "CODE": "5RPM",
            "GROUP": "MACAVAL",
            "NAME": "AMP-792",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "5RPT",
            "GROUP": "RENTINLE",
            "NAME": "BLL-311",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "5RPW",
            "GROUP": "RENTINLE",
            "NAME": "BLN-030",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "5RPY",
            "GROUP": "COMASUR",
            "NAME": "D3R-908",
            "DATETIME": "220505184003"
        },
        {
            "CODE": "5RPZ",
            "GROUP": "RENTINLE",
            "NAME": "BLL-542",
            "DATETIME": "220506112542"
        },
        {
            "CODE": "5RQ1",
            "GROUP": "COMASUR",
            "NAME": "C7T-797",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "5RQ2",
            "GROUP": "COMASUR",
            "NAME": "BBG-817",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "5RQ3",
            "GROUP": "SELGAS",
            "NAME": "F3C-975",
            "DATETIME": "220506094642"
        },
        {
            "CODE": "5RQ6",
            "GROUP": "LINCUNA",
            "NAME": "BBA-750",
            "DATETIME": "220506090615"
        },
        {
            "CODE": "5RQ8",
            "GROUP": "LINCUNA",
            "NAME": "BAZ-932",
            "DATETIME": "220401054136"
        },
        {
            "CODE": "5RQ9",
            "GROUP": "LINCUNA",
            "NAME": "BAZ-779",
            "DATETIME": "220506114412"
        },
        {
            "CODE": "5RQA",
            "GROUP": "MINERA",
            "NAME": "BCV-818",
            "DATETIME": "220506031651"
        },
        {
            "CODE": "5RQB",
            "GROUP": "LINCUNA",
            "NAME": "BAZ-862",
            "DATETIME": "220316173924"
        },
        {
            "CODE": "5RQC",
            "GROUP": "CALEXA",
            "NAME": "C5E-831",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "5RQD",
            "GROUP": "LINCUNA",
            "NAME": "BAY-864",
            "DATETIME": "220506104312"
        },
        {
            "CODE": "5RQF",
            "GROUP": "RENTINLE",
            "NAME": "BHA-690",
            "DATETIME": "220506114033"
        },
        {
            "CODE": "5RQG",
            "GROUP": "GILDEMEI",
            "NAME": "BDC-253",
            "DATETIME": "220505144200"
        },
        {
            "CODE": "5RQH",
            "GROUP": "LINCUNA",
            "NAME": "BAZ-933",
            "DATETIME": "220506115500"
        },
        {
            "CODE": "5RQK",
            "GROUP": "RENTINLE",
            "NAME": "BHA-244",
            "DATETIME": "220506113930"
        },
        {
            "CODE": "5RQN",
            "GROUP": "LINCUNA",
            "NAME": "BAZ-772",
            "DATETIME": "220506115645"
        },
        {
            "CODE": "5RQP",
            "GROUP": "RENTINLE",
            "NAME": "BHD-355",
            "DATETIME": "220416203854"
        },
        {
            "CODE": "5RQQ",
            "GROUP": "LINCUNA",
            "NAME": "BAZ-889",
            "DATETIME": "220506111921"
        },
        {
            "CODE": "5RQS",
            "GROUP": "CASTRO",
            "NAME": "BNL-153",
            "DATETIME": "220505175606"
        },
        {
            "CODE": "5RQW",
            "GROUP": "RENTINLE",
            "NAME": "BHA-542",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "5RQX",
            "GROUP": "SISSA",
            "NAME": "BDB-741",
            "DATETIME": "220506102045"
        },
        {
            "CODE": "5RQZ",
            "GROUP": "RENTINLE",
            "NAME": "BHA-679",
            "DATETIME": "220506115633"
        },
        {
            "CODE": "5RR1",
            "GROUP": "RENTINLE",
            "NAME": "BHA-688",
            "DATETIME": "220506074036"
        },
        {
            "CODE": "5RR3",
            "GROUP": "LINCUNA",
            "NAME": "BAZ-896",
            "DATETIME": "220506103300"
        },
        {
            "CODE": "GCJ4",
            "GROUP": "SOUTHERN",
            "NAME": "AJL-836",
            "DATETIME": "220506115630"
        },
        {
            "CODE": "GCPM",
            "GROUP": "SOUTHERN",
            "NAME": "F2R-732",
            "DATETIME": "220506120127"
        },
        {
            "CODE": "GED3",
            "GROUP": "INLAND",
            "NAME": "C9A-771",
            "DATETIME": "220506111857"
        },
        {
            "CODE": "GED5",
            "GROUP": "SUNARP",
            "NAME": "10088",
            "DATETIME": "220506120435"
        },
        {
            "CODE": "GEDG",
            "GROUP": "SUNARP",
            "NAME": "600277",
            "DATETIME": "220506120359"
        },
        {
            "CODE": "GENS",
            "GROUP": "PACIFICO",
            "NAME": "D2S-426",
            "DATETIME": "220505132301"
        },
        {
            "CODE": "GEQL",
            "GROUP": "P & M",
            "NAME": "D6R-856",
            "DATETIME": "220505130545"
        },
        {
            "CODE": "GEYL",
            "GROUP": "PACIFICO",
            "NAME": "D4N-008",
            "DATETIME": "220506091230"
        },
        {
            "CODE": "GF3Q",
            "GROUP": "PACIFICO",
            "NAME": "D6J-222",
            "DATETIME": "220422210912"
        },
        {
            "CODE": "JQT8",
            "GROUP": "GILDEMEI",
            "NAME": "AVO-373",
            "DATETIME": "220506115706"
        },
        {
            "CODE": "K0AJ",
            "GROUP": "IMC.INMO",
            "NAME": "ANF-885",
            "DATETIME": "220506083022"
        },
        {
            "CODE": "K0BB",
            "GROUP": "ANDINAPL",
            "NAME": "D2R-015",
            "DATETIME": "220506080954"
        },
        {
            "CODE": "K0CN",
            "GROUP": "LOAYZA",
            "NAME": "A7I-473",
            "DATETIME": "220506120235"
        },
        {
            "CODE": "K0ES",
            "GROUP": "ENERLETR",
            "NAME": "W5G-896",
            "DATETIME": "220505091445"
        },
        {
            "CODE": "K0ET",
            "GROUP": "NASHIRO",
            "NAME": "F8C-747",
            "DATETIME": "220506120320"
        },
        {
            "CODE": "K0EU",
            "GROUP": "LA PAZ",
            "NAME": "ABI-869",
            "DATETIME": "220506120321"
        },
        {
            "CODE": "K0EV",
            "GROUP": "EUROSHOP",
            "NAME": "ATK-731",
            "DATETIME": "220506072756"
        },
        {
            "CODE": "K0G2",
            "GROUP": "FIERRO",
            "NAME": "AZB-839",
            "DATETIME": "220506120417"
        },
        {
            "CODE": "K0G4",
            "GROUP": "FLORENTI",
            "NAME": "C4I-778",
            "DATETIME": "220506120526"
        },
        {
            "CODE": "K0GX",
            "GROUP": "INDUVAL",
            "NAME": "B7L-866",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K0H7",
            "GROUP": "JAIPLAST",
            "NAME": "D5Z-887",
            "DATETIME": "220506120447"
        },
        {
            "CODE": "K0H9",
            "GROUP": "JAIPLAST",
            "NAME": "F1J-817",
            "DATETIME": "220506120508"
        },
        {
            "CODE": "K0HA",
            "GROUP": "JAIPLAST",
            "NAME": "B8S-763",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K0HB",
            "GROUP": "JAIPLAST",
            "NAME": "F1N-889",
            "DATETIME": "220408163702"
        },
        {
            "CODE": "K0HC",
            "GROUP": "JAIPLAST",
            "NAME": "AAN-894",
            "DATETIME": "220506120511"
        },
        {
            "CODE": "K0HG",
            "GROUP": "KYAM",
            "NAME": "F0H-856",
            "DATETIME": "220506120444"
        },
        {
            "CODE": "K0HO",
            "GROUP": "ARONES.H",
            "NAME": "CGL-320",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "K0HP",
            "GROUP": "MARIADEL",
            "NAME": "A4G-947",
            "DATETIME": "220505132627"
        },
        {
            "CODE": "K0HQ",
            "GROUP": "MCACHAY",
            "NAME": "AFF-741",
            "DATETIME": "220506120223"
        },
        {
            "CODE": "K0IC",
            "GROUP": "ORBIS",
            "NAME": "C4Z-948",
            "DATETIME": "220506110752"
        },
        {
            "CODE": "K0IE",
            "GROUP": "ORBIS",
            "NAME": "ACL-786",
            "DATETIME": "220506120526"
        },
        {
            "CODE": "K0IF",
            "GROUP": "ORBIS",
            "NAME": "ABI-848",
            "DATETIME": "220506092741"
        },
        {
            "CODE": "K0J2",
            "GROUP": "PVISUAL",
            "NAME": "B3Y-917",
            "DATETIME": "220506072557"
        },
        {
            "CODE": "K0J4",
            "GROUP": "PVISUAL",
            "NAME": "B5U-893",
            "DATETIME": "220506120410"
        },
        {
            "CODE": "K0J7",
            "GROUP": "PVISUAL",
            "NAME": "B3Y-916",
            "DATETIME": "220506120446"
        },
        {
            "CODE": "K0J8",
            "GROUP": "PVISUAL",
            "NAME": "B3Y-918",
            "DATETIME": "220506120319"
        },
        {
            "CODE": "K0JB",
            "GROUP": "PVISUAL",
            "NAME": "B8S-912",
            "DATETIME": "220506115554"
        },
        {
            "CODE": "K0JD",
            "GROUP": "PVISUAL",
            "NAME": "C1N-915",
            "DATETIME": "220505061403"
        },
        {
            "CODE": "K0JE",
            "GROUP": "PVISUAL",
            "NAME": "D9A-364",
            "DATETIME": "220506120429"
        },
        {
            "CODE": "K0JJ",
            "GROUP": "PVISUAL",
            "NAME": "D1L-941",
            "DATETIME": "220506103537"
        },
        {
            "CODE": "K0JM",
            "GROUP": "PVISUAL",
            "NAME": "AEA-088",
            "DATETIME": "220506114258"
        },
        {
            "CODE": "K0JO",
            "GROUP": "PVISUAL",
            "NAME": "F5J-271",
            "DATETIME": "220506105406"
        },
        {
            "CODE": "K0JP",
            "GROUP": "PVISUAL",
            "NAME": "AHB-757",
            "DATETIME": "220506104421"
        },
        {
            "CODE": "K0JR",
            "GROUP": "PVISUAL",
            "NAME": "AHE-946",
            "DATETIME": "220506120323"
        },
        {
            "CODE": "K0K7",
            "GROUP": "OLATI",
            "NAME": "BFU-916",
            "DATETIME": "220506120347"
        },
        {
            "CODE": "K0KZ",
            "GROUP": "P.VISUAL",
            "NAME": "B9F-806",
            "DATETIME": "220505154036"
        },
        {
            "CODE": "K0L4",
            "GROUP": "ANDINAPL",
            "NAME": "D2P-726",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "K0M4",
            "GROUP": "FERYMAR",
            "NAME": "C2D-916",
            "DATETIME": "220506115532"
        },
        {
            "CODE": "K0M7",
            "GROUP": "BETSLYN",
            "NAME": "B4V-897",
            "DATETIME": "220505163528"
        },
        {
            "CODE": "K0MP",
            "GROUP": "ORBIS",
            "NAME": "C8G-931",
            "DATETIME": "220506110659"
        },
        {
            "CODE": "K0NM",
            "GROUP": "TRADESUR",
            "NAME": "AKU-894",
            "DATETIME": "220506120528"
        },
        {
            "CODE": "K0NN",
            "GROUP": "SISSA",
            "NAME": "B4T-897",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "K0NO",
            "GROUP": "SISSA",
            "NAME": "AYG-921",
            "DATETIME": "220506095736"
        },
        {
            "CODE": "K0NP",
            "GROUP": "SISSA",
            "NAME": "AYG-846",
            "DATETIME": "220506120328"
        },
        {
            "CODE": "K0NU",
            "GROUP": "SISSA",
            "NAME": "B5N-821",
            "DATETIME": "220506083659"
        },
        {
            "CODE": "K0NV",
            "GROUP": "SISSA",
            "NAME": "D7B-759",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "K0NY",
            "GROUP": "SOLTRAK",
            "NAME": "D2K-722",
            "DATETIME": "220506115109"
        },
        {
            "CODE": "K0O8",
            "GROUP": "TRANSJB",
            "NAME": "ACG-826",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "K0P5",
            "GROUP": "TRADESUR",
            "NAME": "ADE-712",
            "DATETIME": "220506060536"
        },
        {
            "CODE": "K0P7",
            "GROUP": "TRADESUR",
            "NAME": "ACV-796",
            "DATETIME": "220506112522"
        },
        {
            "CODE": "K0PC",
            "GROUP": "FERMINA",
            "NAME": "AME-760",
            "DATETIME": "220506112117"
        },
        {
            "CODE": "K0PD",
            "GROUP": "BASILIO",
            "NAME": "D1X-946",
            "DATETIME": "220504125716"
        },
        {
            "CODE": "K0PV",
            "GROUP": "PASTOR",
            "NAME": "D4F-993",
            "DATETIME": "220506120403"
        },
        {
            "CODE": "K0PW",
            "GROUP": "FERMINA",
            "NAME": "ADX-726",
            "DATETIME": "220506120403"
        },
        {
            "CODE": "K0PX",
            "GROUP": "FERMINA",
            "NAME": "ADZ-702",
            "DATETIME": "220506120259"
        },
        {
            "CODE": "K0PY",
            "GROUP": "FERMINA",
            "NAME": "AJY-913",
            "DATETIME": "220506113805"
        },
        {
            "CODE": "K0QD",
            "GROUP": "SALEM",
            "NAME": "D7V-942",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K0QK",
            "GROUP": "PART BET",
            "NAME": "BVV-185",
            "DATETIME": "220506115920"
        },
        {
            "CODE": "K0QP",
            "GROUP": "ICP",
            "NAME": "AXQ-772",
            "DATETIME": "220506115958"
        },
        {
            "CODE": "K0QQ",
            "GROUP": "SOLGASTR",
            "NAME": "C4V-990",
            "DATETIME": "220506120407"
        },
        {
            "CODE": "K0QT",
            "GROUP": "MAPFRE",
            "NAME": "BED-553",
            "DATETIME": "220308173122"
        },
        {
            "CODE": "K0QW",
            "GROUP": "S&R",
            "NAME": "BKH-846",
            "DATETIME": "220506120420"
        },
        {
            "CODE": "K0R1",
            "GROUP": "PART BET",
            "NAME": "BWI-428",
            "DATETIME": "220506115633"
        },
        {
            "CODE": "K0R7",
            "GROUP": "PART BET",
            "NAME": "BCC-936",
            "DATETIME": "220506115216"
        },
        {
            "CODE": "K0RA",
            "GROUP": "ICP",
            "NAME": "ATF-856",
            "DATETIME": "220506120456"
        },
        {
            "CODE": "K0RB",
            "GROUP": "OLATI",
            "NAME": "AXN-844",
            "DATETIME": "220506113435"
        },
        {
            "CODE": "K0RE",
            "GROUP": "PART BET",
            "NAME": "BMS-491",
            "DATETIME": "220506115251"
        },
        {
            "CODE": "K0RK",
            "GROUP": "TAXI AH",
            "NAME": "ANX-500",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K0RL",
            "GROUP": "PART BET",
            "NAME": "18295",
            "DATETIME": "220506120022"
        },
        {
            "CODE": "K0RT",
            "GROUP": "PART BET",
            "NAME": "363892",
            "DATETIME": "220506120420"
        },
        {
            "CODE": "K0RW",
            "GROUP": "GILDEMEI",
            "NAME": "BEC-591",
            "DATETIME": "220504131106"
        },
        {
            "CODE": "K0RZ",
            "GROUP": "DATHISA",
            "NAME": "BLO-787",
            "DATETIME": "220506120352"
        },
        {
            "CODE": "K0S1",
            "GROUP": "ANELSA",
            "NAME": "BKT-884",
            "DATETIME": "220506120102"
        },
        {
            "CODE": "K0S2",
            "GROUP": "SANTAINE",
            "NAME": "APP-744",
            "DATETIME": "220210062126"
        },
        {
            "CODE": "K0S6",
            "GROUP": "SOLGASTR",
            "NAME": "B7C-975",
            "DATETIME": "220506115349"
        },
        {
            "CODE": "K0S8",
            "GROUP": "RENTING",
            "NAME": "BHB-357",
            "DATETIME": "220506115737"
        },
        {
            "CODE": "K0SC",
            "GROUP": "PART BET",
            "NAME": "BKF-731",
            "DATETIME": "220506115836"
        },
        {
            "CODE": "K0SG",
            "GROUP": "QUICORNA",
            "NAME": "M5A-834",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K0SL",
            "GROUP": "LUQCEL",
            "NAME": "AEY-906",
            "DATETIME": "220506115911"
        },
        {
            "CODE": "K0SS",
            "GROUP": "PROCARGO",
            "NAME": "B7B-766",
            "DATETIME": "220506115822"
        },
        {
            "CODE": "K0ST",
            "GROUP": "JAIPLAST",
            "NAME": "AXK-799",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "K0SU",
            "GROUP": "PART BET",
            "NAME": "BWN-443",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "K0SY",
            "GROUP": "PART BET",
            "NAME": "A7I-567",
            "DATETIME": "220506115446"
        },
        {
            "CODE": "K0TA",
            "GROUP": "PART BET",
            "NAME": "AJY-749",
            "DATETIME": "220506120208"
        },
        {
            "CODE": "K0TJ",
            "GROUP": "SOLGASTR",
            "NAME": "F6A-990",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "K0TM",
            "GROUP": "INTERSEN",
            "NAME": "BED-874",
            "DATETIME": "220506115408"
        },
        {
            "CODE": "K0TX",
            "GROUP": "PERUCONT",
            "NAME": "C0X-439",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "K0U2",
            "GROUP": "SANTAINE",
            "NAME": "D8P-895",
            "DATETIME": "220506115646"
        },
        {
            "CODE": "K0U5",
            "GROUP": "MODIHU",
            "NAME": "AMG-598",
            "DATETIME": "220506120356"
        },
        {
            "CODE": "K0UD",
            "GROUP": "NOR OIL",
            "NAME": "T4S-090",
            "DATETIME": "220506120132"
        },
        {
            "CODE": "K0UF",
            "GROUP": "TERAN",
            "NAME": "D4C-933",
            "DATETIME": "220506115739"
        },
        {
            "CODE": "K0UY",
            "GROUP": "SOUTHER",
            "NAME": "2936-5C",
            "DATETIME": "220408174526"
        },
        {
            "CODE": "K0VP",
            "GROUP": "TEIROJAS",
            "NAME": "P2R-855",
            "DATETIME": "220506113503"
        },
        {
            "CODE": "K0VZ",
            "GROUP": "CASTRO",
            "NAME": "BCB-026",
            "DATETIME": "220425001008"
        },
        {
            "CODE": "K0W1",
            "GROUP": "PRUEBASL",
            "NAME": "K0W19999",
            "DATETIME": "220118084557"
        },
        {
            "CODE": "K0W8",
            "GROUP": "T.BALDEO",
            "NAME": "D5B-958",
            "DATETIME": "220506115326"
        },
        {
            "CODE": "K0WC",
            "GROUP": "PART BET",
            "NAME": "T5W-517",
            "DATETIME": "220506115923"
        },
        {
            "CODE": "K0WE",
            "GROUP": "GRAMA",
            "NAME": "GATOR",
            "DATETIME": "220506085426"
        },
        {
            "CODE": "K0WG",
            "GROUP": "PART BET",
            "NAME": "BWM-261",
            "DATETIME": "220506115339"
        },
        {
            "CODE": "K0WH",
            "GROUP": "YUPUPUPU",
            "NAME": "T4I-824",
            "DATETIME": "220506115628"
        },
        {
            "CODE": "K0WK",
            "GROUP": "PART BET",
            "NAME": "BKN-888",
            "DATETIME": "220506120153"
        },
        {
            "CODE": "K0WP",
            "GROUP": "FIERRO",
            "NAME": "A8U-945",
            "DATETIME": "220506102045"
        },
        {
            "CODE": "K0WQ",
            "GROUP": "A&J",
            "NAME": "W4G-757",
            "DATETIME": "220208182358"
        },
        {
            "CODE": "K0WS",
            "GROUP": "ESPAR",
            "NAME": "AVM-042",
            "DATETIME": "220506120403"
        },
        {
            "CODE": "K0WY",
            "GROUP": "AGRO",
            "NAME": "D8L-763B",
            "DATETIME": "220506120323"
        },
        {
            "CODE": "K0X1",
            "GROUP": "GILDEMEI",
            "NAME": "BDC-109",
            "DATETIME": "220506115325"
        },
        {
            "CODE": "K0X8",
            "GROUP": "RENTING",
            "NAME": "BHA-243",
            "DATETIME": "220506115650"
        },
        {
            "CODE": "K0XD",
            "GROUP": "ORBIS",
            "NAME": "B9G-752",
            "DATETIME": "220301043252"
        },
        {
            "CODE": "K0XE",
            "GROUP": "JG3 CONS",
            "NAME": "BJB-866",
            "DATETIME": "220506115243"
        },
        {
            "CODE": "K0XF",
            "GROUP": "SOLGASTR",
            "NAME": "D1K-976",
            "DATETIME": "220506111003"
        },
        {
            "CODE": "K0XG",
            "GROUP": "FERREYRO",
            "NAME": "22985",
            "DATETIME": "220506120036"
        },
        {
            "CODE": "K0XI",
            "GROUP": "FERREMAQ",
            "NAME": "305222",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K0XR",
            "GROUP": "QUICORNA",
            "NAME": "M5R-780",
            "DATETIME": "220506115507"
        },
        {
            "CODE": "K0XW",
            "GROUP": "SOLGASTR",
            "NAME": "C4U-994",
            "DATETIME": "220506115358"
        },
        {
            "CODE": "K0XZ",
            "GROUP": "PEREZ",
            "NAME": "AWN-185",
            "DATETIME": "220506001452"
        },
        {
            "CODE": "K0YN",
            "GROUP": "PART BET",
            "NAME": "BWU-682",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "K0YP",
            "GROUP": "PART BET",
            "NAME": "W6U-891",
            "DATETIME": "220506115508"
        },
        {
            "CODE": "K0YS",
            "GROUP": "SOLGASTR",
            "NAME": "D2Q-994",
            "DATETIME": "220505175028"
        },
        {
            "CODE": "K0YV",
            "GROUP": "FCG",
            "NAME": "C6B-775",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "K0YW",
            "GROUP": "CYTCORP",
            "NAME": "D2V-870",
            "DATETIME": "220506115839"
        },
        {
            "CODE": "K0YZ",
            "GROUP": "SOLGASTR",
            "NAME": "D1J-993",
            "DATETIME": "220506115539"
        },
        {
            "CODE": "K0Z5",
            "GROUP": "PART BET",
            "NAME": "BYK-564",
            "DATETIME": "220506120511"
        },
        {
            "CODE": "K0Z6",
            "GROUP": "SOLGASTR",
            "NAME": "C4V-992",
            "DATETIME": "220506115824"
        },
        {
            "CODE": "K0Z7",
            "GROUP": "FERMINA",
            "NAME": "D0X-896",
            "DATETIME": "220404122523"
        },
        {
            "CODE": "K0Z8",
            "GROUP": "FERMINA",
            "NAME": "A9B-835",
            "DATETIME": "220506115301"
        },
        {
            "CODE": "K0Z9",
            "GROUP": "SOLGASTR",
            "NAME": "A9A-979",
            "DATETIME": "220506115734"
        },
        {
            "CODE": "K0ZE",
            "GROUP": "JAI PLAS",
            "NAME": "C8F-894",
            "DATETIME": "220506115338"
        },
        {
            "CODE": "K0ZF",
            "GROUP": "GEMEVA",
            "NAME": "TAE-825",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K0ZG",
            "GROUP": "ICP",
            "NAME": "ANV-888",
            "DATETIME": "220506120429"
        },
        {
            "CODE": "K0ZH",
            "GROUP": "POSITIVA",
            "NAME": "M6I-795",
            "DATETIME": "220506115433"
        },
        {
            "CODE": "K10G",
            "GROUP": "SALUD",
            "NAME": "BUE-002",
            "DATETIME": "220506120247"
        },
        {
            "CODE": "K10H",
            "GROUP": "OIL",
            "NAME": "A2I-870",
            "DATETIME": "220506113807"
        },
        {
            "CODE": "K10I",
            "GROUP": "ACOSTA",
            "NAME": "F6N-769",
            "DATETIME": "220506115101"
        },
        {
            "CODE": "K10O",
            "GROUP": "PART BET",
            "NAME": "ATG-248",
            "DATETIME": "220506115517"
        },
        {
            "CODE": "K10W",
            "GROUP": "GILDEMEI",
            "NAME": "BEM-298",
            "DATETIME": "220506081240"
        },
        {
            "CODE": "K10Y",
            "GROUP": "PART BET",
            "NAME": "0410-QB",
            "DATETIME": "220506120510"
        },
        {
            "CODE": "K10Z",
            "GROUP": "PART BET",
            "NAME": "BVV-399",
            "DATETIME": "220506120411"
        },
        {
            "CODE": "K110",
            "GROUP": "PART BET",
            "NAME": "AKC-516",
            "DATETIME": "220506115749"
        },
        {
            "CODE": "K112",
            "GROUP": "SLI ",
            "NAME": "AFX-849",
            "DATETIME": "220506071854"
        },
        {
            "CODE": "K117",
            "GROUP": "SOLGASTR",
            "NAME": "A7Z-979",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K118",
            "GROUP": "FCG",
            "NAME": "BKL-820",
            "DATETIME": "220506120410"
        },
        {
            "CODE": "K11B",
            "GROUP": "LINCUNA",
            "NAME": "H3B-868",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K11H",
            "GROUP": "EYF SAC",
            "NAME": "AXR-730",
            "DATETIME": "220506120514"
        },
        {
            "CODE": "K11U",
            "GROUP": "PART BET",
            "NAME": "BWO-261",
            "DATETIME": "220506120153"
        },
        {
            "CODE": "K11V",
            "GROUP": "LEPSA",
            "NAME": "BLO-897",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K127",
            "GROUP": "MAPFRE",
            "NAME": "ASN-332",
            "DATETIME": "220506120449"
        },
        {
            "CODE": "K129",
            "GROUP": "GILDEMEI",
            "NAME": "AWT-433",
            "DATETIME": "220506120410"
        },
        {
            "CODE": "K12H",
            "GROUP": "ICP",
            "NAME": "AXQ-868",
            "DATETIME": "220506113543"
        },
        {
            "CODE": "K12I",
            "GROUP": "GILDEMEI",
            "NAME": "BEK-481",
            "DATETIME": "220506113951"
        },
        {
            "CODE": "K12K",
            "GROUP": "PART BET",
            "NAME": "AJF-342",
            "DATETIME": "220506083913"
        },
        {
            "CODE": "K12M",
            "GROUP": "NOR OIL",
            "NAME": "M3N-719",
            "DATETIME": "220506115906"
        },
        {
            "CODE": "K12O",
            "GROUP": "O.LOGIST",
            "NAME": "BCH-754",
            "DATETIME": "220506120353"
        },
        {
            "CODE": "K12U",
            "GROUP": "PAR BET",
            "NAME": "EMI-35B",
            "DATETIME": "220506115624"
        },
        {
            "CODE": "K130",
            "GROUP": "SIREB ",
            "NAME": "ERP-028",
            "DATETIME": "220506104723"
        },
        {
            "CODE": "K132",
            "GROUP": "S&R",
            "NAME": "BKS-703",
            "DATETIME": "220506115804"
        },
        {
            "CODE": "K137",
            "GROUP": "TRADESUR",
            "NAME": "C3B-745",
            "DATETIME": "220506113545"
        },
        {
            "CODE": "K139",
            "GROUP": "RENTINLE",
            "NAME": "BER-101",
            "DATETIME": "220411160656"
        },
        {
            "CODE": "K13E",
            "GROUP": "PACIFICO",
            "NAME": "BFE-485",
            "DATETIME": "220506120419"
        },
        {
            "CODE": "K13F",
            "GROUP": "FERMINA",
            "NAME": "B0N-778",
            "DATETIME": "220506113243"
        },
        {
            "CODE": "K13H",
            "GROUP": "TRADESUR",
            "NAME": "AZQ-880",
            "DATETIME": "220506114002"
        },
        {
            "CODE": "K13I",
            "GROUP": "PART BET",
            "NAME": "BWM-638",
            "DATETIME": "220506120015"
        },
        {
            "CODE": "K13J",
            "GROUP": "MINERA",
            "NAME": "AXL-886",
            "DATETIME": "220505101858"
        },
        {
            "CODE": "K13L",
            "GROUP": "PART BET",
            "NAME": "BCZ-506",
            "DATETIME": "220506115039"
        },
        {
            "CODE": "K13O",
            "GROUP": "PART BET",
            "NAME": "BMC-120",
            "DATETIME": "220506115919"
        },
        {
            "CODE": "K13Q",
            "GROUP": "SOLTRAK",
            "NAME": "AFI-938",
            "DATETIME": "220503194737"
        },
        {
            "CODE": "K13S",
            "GROUP": "GILDEMEI",
            "NAME": "BEI-324",
            "DATETIME": "220506114745"
        },
        {
            "CODE": "K13U",
            "GROUP": "LINCUNA",
            "NAME": "H3B-871",
            "DATETIME": "220506115326"
        },
        {
            "CODE": "K13V",
            "GROUP": "PERUVIAN",
            "NAME": "AVL-870",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K13W",
            "GROUP": "S&R",
            "NAME": "BKH-808",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "K13X",
            "GROUP": "JAIPLAST",
            "NAME": "ATD-822",
            "DATETIME": "220506104427"
        },
        {
            "CODE": "K13Z",
            "GROUP": "PART BET",
            "NAME": "16038",
            "DATETIME": "220506120112"
        },
        {
            "CODE": "K140",
            "GROUP": "SOUTHERN",
            "NAME": "9503-5F",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K141",
            "GROUP": "GILDEMEI",
            "NAME": "BEJ-308",
            "DATETIME": "220506105604"
        },
        {
            "CODE": "K146",
            "GROUP": "NOR OIL",
            "NAME": "T4S-113",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "K148",
            "GROUP": "CORMEI",
            "NAME": "D5O-736",
            "DATETIME": "220506120230"
        },
        {
            "CODE": "K149",
            "GROUP": "TRADESUR",
            "NAME": "C0F-851",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K14B",
            "GROUP": "TRADESUR",
            "NAME": "AXD-874",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "K14C",
            "GROUP": "PART-BET",
            "NAME": "803325",
            "DATETIME": "220506120123"
        },
        {
            "CODE": "K14D",
            "GROUP": "T.ROCHA",
            "NAME": "A5E-826",
            "DATETIME": "220506105230"
        },
        {
            "CODE": "K14E",
            "GROUP": "T-PRESTA",
            "NAME": "ADN-394",
            "DATETIME": "220506120241"
        },
        {
            "CODE": "K14H",
            "GROUP": "PART BET",
            "NAME": "BCL-937",
            "DATETIME": "220506114726"
        },
        {
            "CODE": "K14I",
            "GROUP": "CYTCORP",
            "NAME": "B6O-761",
            "DATETIME": "220506120101"
        },
        {
            "CODE": "K14M",
            "GROUP": "PANIBRA",
            "NAME": "ACB-772",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "K14S",
            "GROUP": "T-PRESTA",
            "NAME": "C3I-025",
            "DATETIME": "220506115745"
        },
        {
            "CODE": "K14Z",
            "GROUP": "STA ROSA",
            "NAME": "BAW-773",
            "DATETIME": "220506115511"
        },
        {
            "CODE": "K152",
            "GROUP": "PART BET",
            "NAME": "410071",
            "DATETIME": "220506115212"
        },
        {
            "CODE": "K156",
            "GROUP": "PART BET",
            "NAME": "18353",
            "DATETIME": "220506120032"
        },
        {
            "CODE": "K157",
            "GROUP": "PART BET",
            "NAME": "BHT-697",
            "DATETIME": "220506115848"
        },
        {
            "CODE": "K15C",
            "GROUP": "KAMITAL",
            "NAME": "BLE-911",
            "DATETIME": "220506115922"
        },
        {
            "CODE": "K15O",
            "GROUP": "SUEROS",
            "NAME": "V9K-723",
            "DATETIME": "220506120520"
        },
        {
            "CODE": "K16K",
            "GROUP": "TMC",
            "NAME": "ATL-918",
            "DATETIME": "220506115702"
        },
        {
            "CODE": "K16M",
            "GROUP": "MAPFRE",
            "NAME": "P2X-519",
            "DATETIME": "220506120258"
        },
        {
            "CODE": "K16N",
            "GROUP": "SPORTWAG",
            "NAME": "BBN-692",
            "DATETIME": "220506115247"
        },
        {
            "CODE": "K16O",
            "GROUP": "JAI PLAS",
            "NAME": "F1J-853",
            "DATETIME": "220506120428"
        },
        {
            "CODE": "K16S",
            "GROUP": "MAPFRE",
            "NAME": "ACG-250",
            "DATETIME": "220506120227"
        },
        {
            "CODE": "K16U",
            "GROUP": "TRADESUR",
            "NAME": "AEO-704",
            "DATETIME": "220506120450"
        },
        {
            "CODE": "K16W",
            "GROUP": "PART BET",
            "NAME": "BWM-157",
            "DATETIME": "220403121430"
        },
        {
            "CODE": "K16X",
            "GROUP": "CRISPETR",
            "NAME": "AHH-943",
            "DATETIME": "220504101354"
        },
        {
            "CODE": "K16Y",
            "GROUP": "PORRAS",
            "NAME": "AFF-762",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K171",
            "GROUP": "O LOGIST",
            "NAME": "ALV-788",
            "DATETIME": "220506115352"
        },
        {
            "CODE": "K172",
            "GROUP": "PART BET",
            "NAME": "T5X-147",
            "DATETIME": "220506115938"
        },
        {
            "CODE": "K17A",
            "GROUP": "COMTRATE",
            "NAME": "AAE-905",
            "DATETIME": "220505202547"
        },
        {
            "CODE": "K17D",
            "GROUP": "T.BALDEO",
            "NAME": "C5P-950",
            "DATETIME": "220506115848"
        },
        {
            "CODE": "K17F",
            "GROUP": "MOLINOPA",
            "NAME": "T0S-888",
            "DATETIME": "220506120347"
        },
        {
            "CODE": "K17H",
            "GROUP": "RODUL",
            "NAME": "BRO-124",
            "DATETIME": "220506115255"
        },
        {
            "CODE": "K17J",
            "GROUP": "PART BET",
            "NAME": "BVM-655",
            "DATETIME": "220506111759"
        },
        {
            "CODE": "K17N",
            "GROUP": "A&J",
            "NAME": "W4G-754",
            "DATETIME": "220506115802"
        },
        {
            "CODE": "K17S",
            "GROUP": "JEVARO",
            "NAME": "BCO-875",
            "DATETIME": "220506120450"
        },
        {
            "CODE": "K17U",
            "GROUP": "OSEX",
            "NAME": "AMK-894",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K182",
            "GROUP": "SOLGASTR",
            "NAME": "C4V-995",
            "DATETIME": "220506115302"
        },
        {
            "CODE": "K188",
            "GROUP": "SOLGASTR",
            "NAME": "C4U-995",
            "DATETIME": "220506115822"
        },
        {
            "CODE": "K18A",
            "GROUP": "FERTILIZ",
            "NAME": "P3S-853",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K18B",
            "GROUP": "T.BALDEO",
            "NAME": "C8E-954",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "K18D",
            "GROUP": "PART BET",
            "NAME": "BFT-442",
            "DATETIME": "220506120232"
        },
        {
            "CODE": "K18G",
            "GROUP": "ESCRIBEN",
            "NAME": "D0R-211",
            "DATETIME": "220506115452"
        },
        {
            "CODE": "K18I",
            "GROUP": "SOLGASTR",
            "NAME": "ATG-992",
            "DATETIME": "220506115526"
        },
        {
            "CODE": "K18L",
            "GROUP": "PART BET",
            "NAME": "BAP-331",
            "DATETIME": "220506120351"
        },
        {
            "CODE": "K18O",
            "GROUP": "INTERSEN",
            "NAME": "C4S-700",
            "DATETIME": "220501132048"
        },
        {
            "CODE": "K18P",
            "GROUP": "PART BET",
            "NAME": "AVT-152",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K18R",
            "GROUP": "MAHU",
            "NAME": "C9K-895",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K18T",
            "GROUP": "S&R",
            "NAME": "AZR-794",
            "DATETIME": "220506120202"
        },
        {
            "CODE": "K18U",
            "GROUP": "PART BET",
            "NAME": "ACV-621",
            "DATETIME": "220506115836"
        },
        {
            "CODE": "K18W",
            "GROUP": "QUICORNA",
            "NAME": "M5P-854",
            "DATETIME": "220506113010"
        },
        {
            "CODE": "K18Y",
            "GROUP": "CASTRO",
            "NAME": "AYD-613",
            "DATETIME": "220506120012"
        },
        {
            "CODE": "K18Z",
            "GROUP": "INTERSEN",
            "NAME": "B3C-857",
            "DATETIME": "220506120259"
        },
        {
            "CODE": "K191",
            "GROUP": "AGAD OL",
            "NAME": "AMI-899",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "K192",
            "GROUP": "GEMEVA",
            "NAME": "TAE-861",
            "DATETIME": "220505135626"
        },
        {
            "CODE": "K194",
            "GROUP": "PART BET",
            "NAME": "F9R-141",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K195",
            "GROUP": "SVS",
            "NAME": "V8W-830",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K197",
            "GROUP": "T-PRESTA",
            "NAME": "AWU-696",
            "DATETIME": "220506120307"
        },
        {
            "CODE": "K198",
            "GROUP": "LEPSA",
            "NAME": "BLS-701",
            "DATETIME": "220506115846"
        },
        {
            "CODE": "K19O",
            "GROUP": "SVS TRAN",
            "NAME": "VAX-857",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K19Q",
            "GROUP": "PART BET",
            "NAME": "ATJ-748",
            "DATETIME": "220119205715"
        },
        {
            "CODE": "K19S",
            "GROUP": "T DAIJO",
            "NAME": "B1Q-807",
            "DATETIME": "220506115643"
        },
        {
            "CODE": "K1A2",
            "GROUP": "NOR OIL",
            "NAME": "T9S-874",
            "DATETIME": "220506120259"
        },
        {
            "CODE": "K1AA",
            "GROUP": "SOLGASTR",
            "NAME": "D2P-993",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K1AF",
            "GROUP": "FERREMAQ",
            "NAME": "2046",
            "DATETIME": "220506114525"
        },
        {
            "CODE": "K1AG",
            "GROUP": "PART BET",
            "NAME": "BCA-061",
            "DATETIME": "220506115644"
        },
        {
            "CODE": "K1AH",
            "GROUP": "T.SANTOS",
            "NAME": "BLI-702",
            "DATETIME": "220506115904"
        },
        {
            "CODE": "K1AK",
            "GROUP": "PART BET",
            "NAME": "BLR-889",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "K1AP",
            "GROUP": "QUICORNA",
            "NAME": "M5A-820",
            "DATETIME": "220506120132"
        },
        {
            "CODE": "K1AQ",
            "GROUP": "TRUCKTEA",
            "NAME": "V9E-141",
            "DATETIME": "220506115954"
        },
        {
            "CODE": "K1AT",
            "GROUP": "JAI PLAS",
            "NAME": "F1G-763",
            "DATETIME": "220506120335"
        },
        {
            "CODE": "K1AX",
            "GROUP": "PART BET",
            "NAME": "18093",
            "DATETIME": "220506115501"
        },
        {
            "CODE": "K1B2",
            "GROUP": "GILDEMEI",
            "NAME": "BDL-445",
            "DATETIME": "220506114042"
        },
        {
            "CODE": "K1B8",
            "GROUP": "MBA",
            "NAME": "C2S-702",
            "DATETIME": "220506115814"
        },
        {
            "CODE": "K1B9",
            "GROUP": "ALPISTE",
            "NAME": "ARM-709",
            "DATETIME": "220506115837"
        },
        {
            "CODE": "K1BB",
            "GROUP": "PART BET",
            "NAME": "BNM-320",
            "DATETIME": "220506120458"
        },
        {
            "CODE": "K1BD",
            "GROUP": "SOLGASTR",
            "NAME": "C7I-996",
            "DATETIME": "220506120425"
        },
        {
            "CODE": "K1BF",
            "GROUP": "GILDEMEI",
            "NAME": "BDJ-573",
            "DATETIME": "220506114714"
        },
        {
            "CODE": "K1BI",
            "GROUP": "GILDEMEI",
            "NAME": "BDE-314",
            "DATETIME": "220417011253"
        },
        {
            "CODE": "K1BN",
            "GROUP": "GILDEMEI",
            "NAME": "BDG-005",
            "DATETIME": "220506111816"
        },
        {
            "CODE": "K1BP",
            "GROUP": "PART BET",
            "NAME": "BMM-331",
            "DATETIME": "220506120437"
        },
        {
            "CODE": "K1BV",
            "GROUP": "AXELS",
            "NAME": "Z7A-717",
            "DATETIME": "220506093403"
        },
        {
            "CODE": "K1C2",
            "GROUP": "PART BET",
            "NAME": "BWL-461",
            "DATETIME": "220506115541"
        },
        {
            "CODE": "K1C4",
            "GROUP": "MACHA",
            "NAME": "BBJ-763",
            "DATETIME": "220506115812"
        },
        {
            "CODE": "K1C7",
            "GROUP": "AUTOMAYO",
            "NAME": "BDH-683",
            "DATETIME": "220326041719"
        },
        {
            "CODE": "K1CC",
            "GROUP": "GILDEMEI",
            "NAME": "BDE-628",
            "DATETIME": "220501165846"
        },
        {
            "CODE": "K1CE",
            "GROUP": "T DAIJO",
            "NAME": "F1U-749",
            "DATETIME": "220506115835"
        },
        {
            "CODE": "K1CF",
            "GROUP": "T.BALDEO",
            "NAME": "D5A-966",
            "DATETIME": "220506115221"
        },
        {
            "CODE": "K1CG",
            "GROUP": "GILDEMEI",
            "NAME": "BFN-652",
            "DATETIME": "220506115442"
        },
        {
            "CODE": "K1CM",
            "GROUP": "S BARTOL",
            "NAME": "115829",
            "DATETIME": "220506115847"
        },
        {
            "CODE": "K1CT",
            "GROUP": "GILDEMEI",
            "NAME": "BDN-103",
            "DATETIME": "220502130816"
        },
        {
            "CODE": "K1DG",
            "GROUP": "GRAMA",
            "NAME": "BLN-506",
            "DATETIME": "220506120012"
        },
        {
            "CODE": "K1DL",
            "GROUP": "GILDEMEI",
            "NAME": "BDO-374",
            "DATETIME": "220506114552"
        },
        {
            "CODE": "K1DR",
            "GROUP": "PART BET",
            "NAME": "F0A-837",
            "DATETIME": "220127153255"
        },
        {
            "CODE": "K1E8",
            "GROUP": "PART BET",
            "NAME": "BWG-012",
            "DATETIME": "220506115749"
        },
        {
            "CODE": "K1EP",
            "GROUP": "SOLGASTR",
            "NAME": "F6A-991",
            "DATETIME": "220506120510"
        },
        {
            "CODE": "K1ER",
            "GROUP": "LINCUNA",
            "NAME": "BNC-791",
            "DATETIME": "220506113032"
        },
        {
            "CODE": "K1F1",
            "GROUP": "SOUTHERN",
            "NAME": "9621-CA",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "K1K9",
            "GROUP": "SANTAINE",
            "NAME": "D8Q-712",
            "DATETIME": "220506114312"
        },
        {
            "CODE": "K1MK",
            "GROUP": "JERLISSA",
            "NAME": "B6B-721",
            "DATETIME": "220506103513"
        },
        {
            "CODE": "K1O4",
            "GROUP": "DAYANA",
            "NAME": "W3F-996",
            "DATETIME": "220506120137"
        },
        {
            "CODE": "K1PI",
            "GROUP": "ANDINAPL",
            "NAME": "V4I-750",
            "DATETIME": "220506004230"
        },
        {
            "CODE": "K1PJ",
            "GROUP": "A&J",
            "NAME": "W4G-755",
            "DATETIME": "220506120316"
        },
        {
            "CODE": "K1PV",
            "GROUP": "JAIPLAST",
            "NAME": "C6P-825",
            "DATETIME": "220506113116"
        },
        {
            "CODE": "K1QA",
            "GROUP": "CALEXA",
            "NAME": "ASI-866",
            "DATETIME": "220506120450"
        },
        {
            "CODE": "K1QB",
            "GROUP": "CALEXA",
            "NAME": "D0D-759",
            "DATETIME": "220506120326"
        },
        {
            "CODE": "K1QE",
            "GROUP": "NASHIRO",
            "NAME": "D3Z-871",
            "DATETIME": "220506120434"
        },
        {
            "CODE": "K1QW",
            "GROUP": "GUERRERO",
            "NAME": "AHO-737",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "K1RP",
            "GROUP": "PVISUAL",
            "NAME": "D8T-883",
            "DATETIME": "220506120355"
        },
        {
            "CODE": "K1RY",
            "GROUP": "T.HUERTA",
            "NAME": "ATK-856",
            "DATETIME": "220506095125"
        },
        {
            "CODE": "K1T4",
            "GROUP": "TRADESUR",
            "NAME": "AHO-744",
            "DATETIME": "220506120517"
        },
        {
            "CODE": "K1T6",
            "GROUP": "TRADESUR",
            "NAME": "AJK-837",
            "DATETIME": "220506120245"
        },
        {
            "CODE": "K1T8",
            "GROUP": "VIDITEK",
            "NAME": "471968",
            "DATETIME": "220330142132"
        },
        {
            "CODE": "K1T9",
            "GROUP": "IMC.INMO",
            "NAME": "ANF-882",
            "DATETIME": "220506115648"
        },
        {
            "CODE": "K1TA",
            "GROUP": "IMC.INMO",
            "NAME": "ANF-940",
            "DATETIME": "220506115046"
        },
        {
            "CODE": "K1TK",
            "GROUP": "FABRICAC",
            "NAME": "AHG-894",
            "DATETIME": "220506120502"
        },
        {
            "CODE": "K1TL",
            "GROUP": "FABRICAC",
            "NAME": "ASX-828",
            "DATETIME": "220506120514"
        },
        {
            "CODE": "K1TM",
            "GROUP": "ACOSTA.L",
            "NAME": "AHI-721",
            "DATETIME": "220329152005"
        },
        {
            "CODE": "K1TN",
            "GROUP": "ACOSTA.L",
            "NAME": "APL-798",
            "DATETIME": "220506115518"
        },
        {
            "CODE": "K1UD",
            "GROUP": "GZ AIR",
            "NAME": "AKS-846",
            "DATETIME": "220506120333"
        },
        {
            "CODE": "K1UG",
            "GROUP": "GRAMA",
            "NAME": "ALX-803",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K1UI",
            "GROUP": "PVISUAL",
            "NAME": "C8E-822",
            "DATETIME": "220506120409"
        },
        {
            "CODE": "K1UU",
            "GROUP": "A&J",
            "NAME": "W5G-898",
            "DATETIME": "220506120301"
        },
        {
            "CODE": "K1UV",
            "GROUP": "A&J",
            "NAME": "W4G-756",
            "DATETIME": "220506115339"
        },
        {
            "CODE": "K1V2",
            "GROUP": "ANYELO",
            "NAME": "D9B-768",
            "DATETIME": "220506120437"
        },
        {
            "CODE": "K1V3",
            "GROUP": "ANYELO",
            "NAME": "B0W-736",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K1V5",
            "GROUP": "REAL CLU",
            "NAME": "C9N-952",
            "DATETIME": "220430210719"
        },
        {
            "CODE": "K1VD",
            "GROUP": "BEST POR",
            "NAME": "AKY-891",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "K1VE",
            "GROUP": "BACHET ",
            "NAME": "F5T-701",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "K1VG",
            "GROUP": "BABYPLAZ",
            "NAME": "ALW-917",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K1VV",
            "GROUP": "SOLTRAK",
            "NAME": "AMB-757",
            "DATETIME": "220506103644"
        },
        {
            "CODE": "K1W9",
            "GROUP": "CEYESA",
            "NAME": "C9I-726",
            "DATETIME": "220506120501"
        },
        {
            "CODE": "K1WA",
            "GROUP": "CEYESA",
            "NAME": "A7Q-922",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "K1WC",
            "GROUP": "CIA.COME",
            "NAME": "ALJ-891",
            "DATETIME": "220506120416"
        },
        {
            "CODE": "K1WD",
            "GROUP": "TRATAR",
            "NAME": "AWS-798",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "K1WM",
            "GROUP": "LINCUNA",
            "NAME": "AUD-865",
            "DATETIME": "220506120313"
        },
        {
            "CODE": "K1WN",
            "GROUP": "LINCUNA",
            "NAME": "AUD-939",
            "DATETIME": "220506075042"
        },
        {
            "CODE": "K1WO",
            "GROUP": "LINCUNA",
            "NAME": "AUD-880",
            "DATETIME": "220411064920"
        },
        {
            "CODE": "K1XM",
            "GROUP": "UEZU",
            "NAME": "F8G-831",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "K1Y2",
            "GROUP": "DIAG.UAL",
            "NAME": "ARC-361",
            "DATETIME": "220311180652"
        },
        {
            "CODE": "K1Y9",
            "GROUP": "DMZ",
            "NAME": "ASH-742",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K1YA",
            "GROUP": "DMZ",
            "NAME": "ANC-887",
            "DATETIME": "220506120250"
        },
        {
            "CODE": "K1YX",
            "GROUP": "ARSI",
            "NAME": "AKF-803",
            "DATETIME": "220504101907"
        },
        {
            "CODE": "K1Z0",
            "GROUP": "ENERLETR",
            "NAME": "ALR-842",
            "DATETIME": "220506120526"
        },
        {
            "CODE": "K229",
            "GROUP": "FIERRO",
            "NAME": "ASN-719",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "K22A",
            "GROUP": "FIERRO",
            "NAME": "ASM-752",
            "DATETIME": "220506120307"
        },
        {
            "CODE": "K22L",
            "GROUP": "GUERRERO",
            "NAME": "B0N-908",
            "DATETIME": "220506120318"
        },
        {
            "CODE": "K22M",
            "GROUP": "GUERRERO",
            "NAME": "ASN-898",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "K22N",
            "GROUP": "GZ AIR",
            "NAME": "ARZ-736",
            "DATETIME": "220506120438"
        },
        {
            "CODE": "K22P",
            "GROUP": "HILARIO",
            "NAME": "C2E-831",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K22Q",
            "GROUP": "HILARIO",
            "NAME": "D3J-863",
            "DATETIME": "220506120359"
        },
        {
            "CODE": "K22R",
            "GROUP": "HILARIO",
            "NAME": "D3J-913",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "K22T",
            "GROUP": "HUASCAR",
            "NAME": "AFB-865",
            "DATETIME": "220506103248"
        },
        {
            "CODE": "K23H",
            "GROUP": "SAGA",
            "NAME": "B8Z-714",
            "DATETIME": "220506115350"
        },
        {
            "CODE": "K23Q",
            "GROUP": "J LOPEZ ",
            "NAME": "W4R-742",
            "DATETIME": "220506114128"
        },
        {
            "CODE": "K23R",
            "GROUP": "J LOPEZ ",
            "NAME": "V5U-711",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "K23S",
            "GROUP": "DIAZALVA",
            "NAME": "D5F-932",
            "DATETIME": "220506120217"
        },
        {
            "CODE": "K23T",
            "GROUP": "KMC",
            "NAME": "ANU-760",
            "DATETIME": "220506120346"
        },
        {
            "CODE": "K23U",
            "GROUP": "KMC",
            "NAME": "F1L-807",
            "DATETIME": "220506120316"
        },
        {
            "CODE": "K23V",
            "GROUP": "KMC",
            "NAME": "F7I-835",
            "DATETIME": "220506120323"
        },
        {
            "CODE": "K23X",
            "GROUP": "KMC",
            "NAME": "ANX-836",
            "DATETIME": "220506120332"
        },
        {
            "CODE": "K252",
            "GROUP": "LIMA RES",
            "NAME": "ANY-703",
            "DATETIME": "220506120453"
        },
        {
            "CODE": "K259",
            "GROUP": "ALPISTE",
            "NAME": "F8R-878",
            "DATETIME": "220427152721"
        },
        {
            "CODE": "K25A",
            "GROUP": "CAMA RIO",
            "NAME": "F9L-922",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "K25C",
            "GROUP": "MACC-HER",
            "NAME": "APJ-889",
            "DATETIME": "220506120248"
        },
        {
            "CODE": "K25D",
            "GROUP": "MACC-HER",
            "NAME": "API-942",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "K25E",
            "GROUP": "NUEVAERA",
            "NAME": "C0M-943",
            "DATETIME": "220506120425"
        },
        {
            "CODE": "K25F",
            "GROUP": "NUEVAERA",
            "NAME": "C5I-919",
            "DATETIME": "220506120431"
        },
        {
            "CODE": "K26K",
            "GROUP": "ORBIS",
            "NAME": "AHE-749",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K26O",
            "GROUP": "PINOQUIM",
            "NAME": "C4N-886",
            "DATETIME": "220504174710"
        },
        {
            "CODE": "K26P",
            "GROUP": "PINOQUIM",
            "NAME": "F2U-729",
            "DATETIME": "220506120002"
        },
        {
            "CODE": "K26R",
            "GROUP": "PISCIFAC",
            "NAME": "F3L-712",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "K26T",
            "GROUP": "PISCIFAC",
            "NAME": "F3D-910",
            "DATETIME": "220506120257"
        },
        {
            "CODE": "K27M",
            "GROUP": "MODEPSA",
            "NAME": "C2H-849",
            "DATETIME": "220506120423"
        },
        {
            "CODE": "K27S",
            "GROUP": "PVISUAL",
            "NAME": "AHA-925",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "K27T",
            "GROUP": "PVISUAL",
            "NAME": "AHB-837",
            "DATETIME": "220324224829"
        },
        {
            "CODE": "K27U",
            "GROUP": "PVISUAL",
            "NAME": "AHB-930",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "K27Z",
            "GROUP": "RAGEN",
            "NAME": "APN-902",
            "DATETIME": "220506112438"
        },
        {
            "CODE": "K28I",
            "GROUP": "RENTINGP",
            "NAME": "ARL-407",
            "DATETIME": "220505171926"
        },
        {
            "CODE": "K28J",
            "GROUP": "RENTINGP",
            "NAME": "ARL-552",
            "DATETIME": "220506072803"
        },
        {
            "CODE": "K28U",
            "GROUP": "T ACOSTA",
            "NAME": "F6M-768",
            "DATETIME": "220331150831"
        },
        {
            "CODE": "K28V",
            "GROUP": "BIDDLE",
            "NAME": "B8F-343",
            "DATETIME": "220428151219"
        },
        {
            "CODE": "K298",
            "GROUP": "BIDDLE",
            "NAME": "BDE-411",
            "DATETIME": "220330095328"
        },
        {
            "CODE": "K299",
            "GROUP": "BIDDLE",
            "NAME": "A6D-759",
            "DATETIME": "220506022111"
        },
        {
            "CODE": "K29Q",
            "GROUP": "BIDDLE",
            "NAME": "A6D-758",
            "DATETIME": "220505142651"
        },
        {
            "CODE": "K2A2",
            "GROUP": "BIDDLE",
            "NAME": "C0Z-575",
            "DATETIME": "220428090014"
        },
        {
            "CODE": "K2AZ",
            "GROUP": "JERLISSA",
            "NAME": "B5V-794",
            "DATETIME": "220505153646"
        },
        {
            "CODE": "K2B9",
            "GROUP": "SOLTRAK",
            "NAME": "AUE-946",
            "DATETIME": "220506120507"
        },
        {
            "CODE": "K2BE",
            "GROUP": "MBA",
            "NAME": "B8Y-784",
            "DATETIME": "220302222223"
        },
        {
            "CODE": "K2BS",
            "GROUP": "RENTINGP",
            "NAME": "ASM-807",
            "DATETIME": "220506105922"
        },
        {
            "CODE": "K2C8",
            "GROUP": "DURAND",
            "NAME": "ATE-902",
            "DATETIME": "220506120152"
        },
        {
            "CODE": "K2CC",
            "GROUP": "DURAND",
            "NAME": "AAQ-314",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "K2D2",
            "GROUP": "TRADESUR",
            "NAME": "AVL-922",
            "DATETIME": "220506120330"
        },
        {
            "CODE": "K2DI",
            "GROUP": "BERTASOL",
            "NAME": "C5N-765",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "K2DL",
            "GROUP": "T.CAMILA",
            "NAME": "AKU-768",
            "DATETIME": "220506120302"
        },
        {
            "CODE": "K2DS",
            "GROUP": "SLI",
            "NAME": "AKP-906",
            "DATETIME": "220506120435"
        },
        {
            "CODE": "K2DT",
            "GROUP": "SLI",
            "NAME": "AKG-782",
            "DATETIME": "220503151328"
        },
        {
            "CODE": "K2DX",
            "GROUP": "SILICE",
            "NAME": "C1W-945",
            "DATETIME": "220506094131"
        },
        {
            "CODE": "K2DY",
            "GROUP": "SILICE",
            "NAME": "L150-D",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K2EC",
            "GROUP": "SOLTRAK",
            "NAME": "AFI-882",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K2EG",
            "GROUP": "S.MODA",
            "NAME": "COD-088",
            "DATETIME": "220506120422"
        },
        {
            "CODE": "K2FJ",
            "GROUP": "TRANSITA",
            "NAME": "D6K-726C",
            "DATETIME": "220505210431"
        },
        {
            "CODE": "K2FK",
            "GROUP": "TRANSITA",
            "NAME": "D6L-701C",
            "DATETIME": "220506120450"
        },
        {
            "CODE": "K2FL",
            "GROUP": "TRANSITA",
            "NAME": "D6M-728F",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "K2FM",
            "GROUP": "TRANSITA",
            "NAME": "D6M-747F",
            "DATETIME": "220506092424"
        },
        {
            "CODE": "K2FN",
            "GROUP": "TRANSITA",
            "NAME": "D6P-710",
            "DATETIME": "220506115300"
        },
        {
            "CODE": "K2FO",
            "GROUP": "TRANSITA",
            "NAME": "D6K-726F",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "K2FR",
            "GROUP": "TRANSITA",
            "NAME": "C5A-977",
            "DATETIME": "220506111203"
        },
        {
            "CODE": "K2FS",
            "GROUP": "TRANSOIL",
            "NAME": "ARE-914",
            "DATETIME": "220506120514"
        },
        {
            "CODE": "K2FY",
            "GROUP": "POCHITO",
            "NAME": "A9N-907",
            "DATETIME": "220506120449"
        },
        {
            "CODE": "K2FZ",
            "GROUP": "POCHITO",
            "NAME": "A4K-840",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "K2G0",
            "GROUP": "POCHITO",
            "NAME": "A1M-817",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "K2G2",
            "GROUP": "T.J.LEON",
            "NAME": "C8D-851",
            "DATETIME": "220506120251"
        },
        {
            "CODE": "K2G4",
            "GROUP": "T.J.LEON",
            "NAME": "L120-C",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K2G7",
            "GROUP": "ONCOY",
            "NAME": "B6O-898",
            "DATETIME": "220315182102"
        },
        {
            "CODE": "K2G8",
            "GROUP": "ONCOY",
            "NAME": "F8P-801",
            "DATETIME": "220506115316"
        },
        {
            "CODE": "K2GB",
            "GROUP": "T ACOSTA",
            "NAME": "D7S-841",
            "DATETIME": "220418145031"
        },
        {
            "CODE": "K2GC",
            "GROUP": "T ACOSTA",
            "NAME": "D7S-764",
            "DATETIME": "220504113810"
        },
        {
            "CODE": "K2GH",
            "GROUP": "TRADESUR",
            "NAME": "C2Z-754",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "K2GK",
            "GROUP": "FERMINA",
            "NAME": "AKS-702",
            "DATETIME": "220506120319"
        },
        {
            "CODE": "K2GL",
            "GROUP": "FERMINA",
            "NAME": "ATY-848",
            "DATETIME": "220506120403"
        },
        {
            "CODE": "K2GM",
            "GROUP": "FERMINA",
            "NAME": "AUE-814",
            "DATETIME": "220506120307"
        },
        {
            "CODE": "K2GP",
            "GROUP": "GIANSANT",
            "NAME": "AKB-821",
            "DATETIME": "220506120456"
        },
        {
            "CODE": "K2GQ",
            "GROUP": "GIANSANT",
            "NAME": "D9W-797",
            "DATETIME": "220506120316"
        },
        {
            "CODE": "K2GR",
            "GROUP": "GIANSANT",
            "NAME": "F4R-770",
            "DATETIME": "220506120320"
        },
        {
            "CODE": "K2GS",
            "GROUP": "GIANSANT",
            "NAME": "F2B-769",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "K2GT",
            "GROUP": "GIANSANT",
            "NAME": "ADS-902",
            "DATETIME": "220506120446"
        },
        {
            "CODE": "K2GU",
            "GROUP": "GIANSANT",
            "NAME": "F4M-756",
            "DATETIME": "220506120253"
        },
        {
            "CODE": "K2GV",
            "GROUP": "GIANSANT",
            "NAME": "F4M-854",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K2GW",
            "GROUP": "GIANSANT",
            "NAME": "F1M-795",
            "DATETIME": "220506120255"
        },
        {
            "CODE": "K2GX",
            "GROUP": "T ACOSTA",
            "NAME": "ARJ-704",
            "DATETIME": "220506120415"
        },
        {
            "CODE": "K2GY",
            "GROUP": "T ACOSTA",
            "NAME": "ARJ-719",
            "DATETIME": "220506120333"
        },
        {
            "CODE": "K2GZ",
            "GROUP": "T.HUERTA",
            "NAME": "C1R-903",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "K2HU",
            "GROUP": "MOLLENDO",
            "NAME": "VBC-773",
            "DATETIME": "220506120304"
        },
        {
            "CODE": "K2HZ",
            "GROUP": "TRECA",
            "NAME": "ACD-936",
            "DATETIME": "220506120258"
        },
        {
            "CODE": "K2IE",
            "GROUP": "JERLISSA",
            "NAME": "B6I-727",
            "DATETIME": "220506120517"
        },
        {
            "CODE": "K2JV",
            "GROUP": "U.P.A.L",
            "NAME": "AMG-362",
            "DATETIME": "220506120313"
        },
        {
            "CODE": "K2LT",
            "GROUP": "RENTINGP",
            "NAME": "ARI-373",
            "DATETIME": "220506114812"
        },
        {
            "CODE": "K2MU",
            "GROUP": "LINCUNA",
            "NAME": "AHM-944",
            "DATETIME": "220506120234"
        },
        {
            "CODE": "K2MX",
            "GROUP": "ENERLETR",
            "NAME": "D5N-776",
            "DATETIME": "220506120405"
        },
        {
            "CODE": "K2MY",
            "GROUP": "ENERLETR",
            "NAME": "W5O-802",
            "DATETIME": "220128125240"
        },
        {
            "CODE": "K2MZ",
            "GROUP": "ENERLETR",
            "NAME": "W5O-813",
            "DATETIME": "220506120250"
        },
        {
            "CODE": "K2N0",
            "GROUP": "ENERLETR",
            "NAME": "W5O-796",
            "DATETIME": "220506120357"
        },
        {
            "CODE": "K2N2",
            "GROUP": "ENERLETR",
            "NAME": "W5O-797",
            "DATETIME": "220506120513"
        },
        {
            "CODE": "K2N3",
            "GROUP": "ENERLETR",
            "NAME": "W5O-801",
            "DATETIME": "220420134753"
        },
        {
            "CODE": "K2N5",
            "GROUP": "ENERLETR",
            "NAME": "W5G-897",
            "DATETIME": "220506120319"
        },
        {
            "CODE": "K2OL",
            "GROUP": "RAGEN",
            "NAME": "B3K-891",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "K2RD",
            "GROUP": "CONCYSSA",
            "NAME": "AXM-767",
            "DATETIME": "220113055017"
        },
        {
            "CODE": "K2S1",
            "GROUP": "S.A.P.C",
            "NAME": "ATB-873",
            "DATETIME": "220215180515"
        },
        {
            "CODE": "K2S2",
            "GROUP": "SAGA",
            "NAME": "ATA-840",
            "DATETIME": "220506111227"
        },
        {
            "CODE": "K2S3",
            "GROUP": "SAGA",
            "NAME": "ASY-935",
            "DATETIME": "220506114617"
        },
        {
            "CODE": "K2S4",
            "GROUP": "SAGA",
            "NAME": "ASY-884",
            "DATETIME": "220506082519"
        },
        {
            "CODE": "K2S5",
            "GROUP": "SAGA",
            "NAME": "ASY-809",
            "DATETIME": "220506112224"
        },
        {
            "CODE": "K2S8",
            "GROUP": "BERECHE",
            "NAME": "5011",
            "DATETIME": "220506114018"
        },
        {
            "CODE": "K2SX",
            "GROUP": "IN.USHNU",
            "NAME": "F2N-844",
            "DATETIME": "220506114552"
        },
        {
            "CODE": "K2T0",
            "GROUP": "ANDEANA",
            "NAME": "C9E-813",
            "DATETIME": "220506120341"
        },
        {
            "CODE": "K2TH",
            "GROUP": "PART BET",
            "NAME": "F7V-863",
            "DATETIME": "220506114138"
        },
        {
            "CODE": "K2TI",
            "GROUP": "CIA.COME",
            "NAME": "BDY-793",
            "DATETIME": "220506114520"
        },
        {
            "CODE": "K2TJ",
            "GROUP": "LANDEO.P",
            "NAME": "A5U-911",
            "DATETIME": "220503172843"
        },
        {
            "CODE": "K2UL",
            "GROUP": "CONCYSSA",
            "NAME": "772858",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "K2VB",
            "GROUP": "LEXICOM",
            "NAME": "AWS-233",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "K2VC",
            "GROUP": "LEXICOM",
            "NAME": "D8G-483",
            "DATETIME": "220506120351"
        },
        {
            "CODE": "K2VD",
            "GROUP": "LEXICOM",
            "NAME": "AWR-413",
            "DATETIME": "220506120517"
        },
        {
            "CODE": "K2W7",
            "GROUP": "FULL SER",
            "NAME": "D9Q-784",
            "DATETIME": "220506115033"
        },
        {
            "CODE": "K2W8",
            "GROUP": "GEOINSIT",
            "NAME": "C9C-924",
            "DATETIME": "220506110859"
        },
        {
            "CODE": "K2W9",
            "GROUP": "GEOINSIT",
            "NAME": "F9S-164",
            "DATETIME": "220506113733"
        },
        {
            "CODE": "K2WA",
            "GROUP": "GEOINSIT",
            "NAME": "F3J-008",
            "DATETIME": "220506115820"
        },
        {
            "CODE": "K2WB",
            "GROUP": "GEOINSIT",
            "NAME": "ANO-074",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "K2WQ",
            "GROUP": "INCA TOP",
            "NAME": "V8U-860",
            "DATETIME": "220506111230"
        },
        {
            "CODE": "K2WR",
            "GROUP": "INCA TOP",
            "NAME": "V8U-794",
            "DATETIME": "220506111023"
        },
        {
            "CODE": "K2WS",
            "GROUP": "INCA TOP",
            "NAME": "V1B-821P",
            "DATETIME": "220506115405"
        },
        {
            "CODE": "K2WT",
            "GROUP": "INCA TOP",
            "NAME": "V5T-935",
            "DATETIME": "220506120240"
        },
        {
            "CODE": "K2WV",
            "GROUP": "BALLAHAN",
            "NAME": "ASN-825",
            "DATETIME": "220506115102"
        },
        {
            "CODE": "K2X6",
            "GROUP": "JG3 CONS",
            "NAME": "ATL-919",
            "DATETIME": "220506115449"
        },
        {
            "CODE": "K2X7",
            "GROUP": "JG3 CONS",
            "NAME": "ADD-813",
            "DATETIME": "220506115151"
        },
        {
            "CODE": "K2XB",
            "GROUP": "INV.NEGO",
            "NAME": "C3T-896",
            "DATETIME": "220506120029"
        },
        {
            "CODE": "K2XC",
            "GROUP": "INV.NEGO",
            "NAME": "C4A-750",
            "DATETIME": "220506113118"
        },
        {
            "CODE": "K2XF",
            "GROUP": "MAININ",
            "NAME": "AWL-826",
            "DATETIME": "220506115558"
        },
        {
            "CODE": "K2XH",
            "GROUP": "LOGIST.E",
            "NAME": "W3M-835",
            "DATETIME": "220506120354"
        },
        {
            "CODE": "K2XU",
            "GROUP": "OLIVOS S",
            "NAME": "AUC-797",
            "DATETIME": "220506120450"
        },
        {
            "CODE": "K2Y6",
            "GROUP": "MODEPSA",
            "NAME": "ASH-721",
            "DATETIME": "220506114947"
        },
        {
            "CODE": "K2Y7",
            "GROUP": "Q.ANDERS",
            "NAME": "C0Z-762",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "K2Z3",
            "GROUP": "RENTINGP",
            "NAME": "ATG-801",
            "DATETIME": "220321141036"
        },
        {
            "CODE": "K2Z8",
            "GROUP": "RENTINGP",
            "NAME": "ATJ-925",
            "DATETIME": "220506115440"
        },
        {
            "CODE": "K2ZI",
            "GROUP": "RENTINGP",
            "NAME": "ATT-823",
            "DATETIME": "220321142012"
        },
        {
            "CODE": "K2ZS",
            "GROUP": "RENTINGP",
            "NAME": "AUY-763",
            "DATETIME": "220506115316"
        },
        {
            "CODE": "K300",
            "GROUP": "SETECMER",
            "NAME": "D7X-766",
            "DATETIME": "220506113554"
        },
        {
            "CODE": "K301",
            "GROUP": "SETECMER",
            "NAME": "ASQ-916",
            "DATETIME": "220506120443"
        },
        {
            "CODE": "K302",
            "GROUP": "BERTASOL",
            "NAME": "AUN-775",
            "DATETIME": "220506120449"
        },
        {
            "CODE": "K30U",
            "GROUP": "T.J.LEON",
            "NAME": "AWF-062",
            "DATETIME": "220506120229"
        },
        {
            "CODE": "K315",
            "GROUP": "TRADESUR",
            "NAME": "C0F-850",
            "DATETIME": "220506113511"
        },
        {
            "CODE": "K316",
            "GROUP": "TRADESUR",
            "NAME": "D1E-852",
            "DATETIME": "220506115427"
        },
        {
            "CODE": "K317",
            "GROUP": "TRADESUR",
            "NAME": "C8Q-741",
            "DATETIME": "220506112334"
        },
        {
            "CODE": "K318",
            "GROUP": "TRADESUR",
            "NAME": "ATH-722",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "K319",
            "GROUP": "TRADESUR",
            "NAME": "ATP-728",
            "DATETIME": "220506111020"
        },
        {
            "CODE": "K31A",
            "GROUP": "T.FAZIO",
            "NAME": "PIW-524",
            "DATETIME": "220506114218"
        },
        {
            "CODE": "K31B",
            "GROUP": "FUENCARR",
            "NAME": "ATL-887",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "K32U",
            "GROUP": "LOAYZA",
            "NAME": "BBE-147",
            "DATETIME": "220506120321"
        },
        {
            "CODE": "K32Y",
            "GROUP": "ROJAS.G",
            "NAME": "AVI-913",
            "DATETIME": "220506120516"
        },
        {
            "CODE": "K335",
            "GROUP": "T.LORE",
            "NAME": "D6W-956",
            "DATETIME": "220506115950"
        },
        {
            "CODE": "K33D",
            "GROUP": "CONDORVA",
            "NAME": "ACS-776",
            "DATETIME": "220506113346"
        },
        {
            "CODE": "K33F",
            "GROUP": "PART BET",
            "NAME": "F3L-735",
            "DATETIME": "220503111548"
        },
        {
            "CODE": "K33K",
            "GROUP": "LOAYZA",
            "NAME": "D5C-350",
            "DATETIME": "220506120009"
        },
        {
            "CODE": "K33P",
            "GROUP": "ECEMA",
            "NAME": "F8S-920",
            "DATETIME": "220506080217"
        },
        {
            "CODE": "K33R",
            "GROUP": "MODIHU",
            "NAME": "ARP-277",
            "DATETIME": "220506112657"
        },
        {
            "CODE": "K353",
            "GROUP": "MARIADEL",
            "NAME": "D4P-843",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "K35U",
            "GROUP": "FERMINA",
            "NAME": "F3W-919",
            "DATETIME": "220506115816"
        },
        {
            "CODE": "K3CT",
            "GROUP": "REP.MART",
            "NAME": "C8O-744",
            "DATETIME": "220506114510"
        },
        {
            "CODE": "K3CU",
            "GROUP": "REP.MART",
            "NAME": "D4A-944",
            "DATETIME": "220506113157"
        },
        {
            "CODE": "K3GL",
            "GROUP": "ASZTRANS",
            "NAME": "B8C-835",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "K3H4",
            "GROUP": "C.C.ALEM",
            "NAME": "D6Z-970",
            "DATETIME": "220506120320"
        },
        {
            "CODE": "K3H7",
            "GROUP": "LOAYZA",
            "NAME": "A6V-138",
            "DATETIME": "220506102443"
        },
        {
            "CODE": "K3H8",
            "GROUP": "LOAYZA",
            "NAME": "AHS-325",
            "DATETIME": "220506115804"
        },
        {
            "CODE": "K3HC",
            "GROUP": "S.ANITA",
            "NAME": "AVQ-903",
            "DATETIME": "220506104541"
        },
        {
            "CODE": "K3HR",
            "GROUP": "DIAZTRAN",
            "NAME": "ASH-802",
            "DATETIME": "220506120235"
        },
        {
            "CODE": "K3I6",
            "GROUP": "SURCANO",
            "NAME": "B1J-848",
            "DATETIME": "220504152101"
        },
        {
            "CODE": "K3IF",
            "GROUP": "SMPORRAS",
            "NAME": "B9C-744",
            "DATETIME": "220506120253"
        },
        {
            "CODE": "K3IL",
            "GROUP": "ENERLETR",
            "NAME": "D5J-775",
            "DATETIME": "220428142601"
        },
        {
            "CODE": "K3IN",
            "GROUP": "ENERLETR",
            "NAME": "D5L-790",
            "DATETIME": "220506084144"
        },
        {
            "CODE": "K3IX",
            "GROUP": "ORBIS",
            "NAME": "AHE-775",
            "DATETIME": "220506120437"
        },
        {
            "CODE": "K3JK",
            "GROUP": "FERYMAR",
            "NAME": "D7B-238",
            "DATETIME": "220506111144"
        },
        {
            "CODE": "K3JM",
            "GROUP": "F.ARONI",
            "NAME": "C5M-917",
            "DATETIME": "220506120142"
        },
        {
            "CODE": "K3JN",
            "GROUP": "FLORENTI",
            "NAME": "AKA-912",
            "DATETIME": "220506110016"
        },
        {
            "CODE": "K3JP",
            "GROUP": "GH MAQUI",
            "NAME": "A5X-299",
            "DATETIME": "220506111203"
        },
        {
            "CODE": "K3KA",
            "GROUP": "ANDINAPL",
            "NAME": "C1V-841",
            "DATETIME": "220506120407"
        },
        {
            "CODE": "K3LH",
            "GROUP": "JERLISSA",
            "NAME": "B6I-709",
            "DATETIME": "220505190315"
        },
        {
            "CODE": "K3LM",
            "GROUP": "NOVARCON",
            "NAME": "F6V-901",
            "DATETIME": "220505213115"
        },
        {
            "CODE": "K3LP",
            "GROUP": "MODEPSA",
            "NAME": "D2W-853",
            "DATETIME": "220506120432"
        },
        {
            "CODE": "K3LQ",
            "GROUP": "MODEPSA",
            "NAME": "D2W-854",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "K3LR",
            "GROUP": "MODEPSA",
            "NAME": "D3L-804",
            "DATETIME": "220504173447"
        },
        {
            "CODE": "K3LS",
            "GROUP": "MODEPSA",
            "NAME": "D4Y-935",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "K3LT",
            "GROUP": "MODEPSA",
            "NAME": "AFK-844",
            "DATETIME": "220506103250"
        },
        {
            "CODE": "K3MV",
            "GROUP": "REP.MART",
            "NAME": "D4A-826",
            "DATETIME": "220506111201"
        },
        {
            "CODE": "K3MY",
            "GROUP": "ANDINAPL",
            "NAME": "D2S-723",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K3MZ",
            "GROUP": "SOLTRAK",
            "NAME": "C5B-756",
            "DATETIME": "220506120407"
        },
        {
            "CODE": "K3NQ",
            "GROUP": "RONISH",
            "NAME": "B4S-901",
            "DATETIME": "220506081659"
        },
        {
            "CODE": "K3NY",
            "GROUP": "BRX",
            "NAME": "D8Q-713",
            "DATETIME": "220506120407"
        },
        {
            "CODE": "K3OP",
            "GROUP": "ANDERS",
            "NAME": "F3Y-841",
            "DATETIME": "220506120052"
        },
        {
            "CODE": "K3P2",
            "GROUP": "COPERO",
            "NAME": "D7Q-738",
            "DATETIME": "220416091715"
        },
        {
            "CODE": "K3Q6",
            "GROUP": "FERYMAR",
            "NAME": "ANF-898",
            "DATETIME": "220506120237"
        },
        {
            "CODE": "K3QC",
            "GROUP": "MACC-HER",
            "NAME": "D1Y-705",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "K3QH",
            "GROUP": "PVISUAL",
            "NAME": "ACG-336",
            "DATETIME": "220506120510"
        },
        {
            "CODE": "K3QI",
            "GROUP": "Q.ANDERS",
            "NAME": "F4C-875",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "K3QM",
            "GROUP": "FERYMAR",
            "NAME": "F5X-397",
            "DATETIME": "220506114801"
        },
        {
            "CODE": "K3QY",
            "GROUP": "LOAYZA",
            "NAME": "A6U-588",
            "DATETIME": "220421111303"
        },
        {
            "CODE": "K3RD",
            "GROUP": "RENTINGP",
            "NAME": "AWG-403",
            "DATETIME": "220421154410"
        },
        {
            "CODE": "K3RY",
            "GROUP": "T. LUCKY",
            "NAME": "C9X-841",
            "DATETIME": "220506120513"
        },
        {
            "CODE": "K3RZ",
            "GROUP": "T. LUCKY",
            "NAME": "W3R-762",
            "DATETIME": "220506084002"
        },
        {
            "CODE": "K3S3",
            "GROUP": "TRANSOIL",
            "NAME": "D7M-822",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "K3S4",
            "GROUP": "TRANSOIL",
            "NAME": "A6H-812",
            "DATETIME": "220506120343"
        },
        {
            "CODE": "K3S5",
            "GROUP": "TRANSOIL",
            "NAME": "A6H-817",
            "DATETIME": "220506111420"
        },
        {
            "CODE": "K3S6",
            "GROUP": "TRANSOIL",
            "NAME": "AXB-814",
            "DATETIME": "220506120510"
        },
        {
            "CODE": "K3S8",
            "GROUP": "T ACOSTA",
            "NAME": "ARV-771",
            "DATETIME": "220506120513"
        },
        {
            "CODE": "K3U2",
            "GROUP": "T.ARELLA",
            "NAME": "573341",
            "DATETIME": "220406154024"
        },
        {
            "CODE": "K3UE",
            "GROUP": "J LOPEZ",
            "NAME": "F9V-867",
            "DATETIME": "220506120414"
        },
        {
            "CODE": "K3YB",
            "GROUP": "TRUCK SE",
            "NAME": "C4S-937",
            "DATETIME": "220506120322"
        },
        {
            "CODE": "K3ZB",
            "GROUP": "COLQUI",
            "NAME": "B5J-730",
            "DATETIME": "220506120438"
        },
        {
            "CODE": "K3ZG",
            "GROUP": "SLI",
            "NAME": "D2Z-943",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K3ZR",
            "GROUP": "MARYORIC",
            "NAME": "A6X-909",
            "DATETIME": "220506120329"
        },
        {
            "CODE": "K3ZU",
            "GROUP": "ASENCIOS",
            "NAME": "B2M-001",
            "DATETIME": "220506120317"
        },
        {
            "CODE": "K3ZX",
            "GROUP": "SLI",
            "NAME": "AFQ-846",
            "DATETIME": "220506120334"
        },
        {
            "CODE": "K405",
            "GROUP": "UEZU",
            "NAME": "AVV-878",
            "DATETIME": "220506120437"
        },
        {
            "CODE": "K43Y",
            "GROUP": "ANYELO",
            "NAME": "B6E-862",
            "DATETIME": "220505065457"
        },
        {
            "CODE": "K450",
            "GROUP": "SLI",
            "NAME": "A7V-856",
            "DATETIME": "220506120340"
        },
        {
            "CODE": "K451",
            "GROUP": "SLI",
            "NAME": "D2U-770",
            "DATETIME": "220506120458"
        },
        {
            "CODE": "K45E",
            "GROUP": "BACHET",
            "NAME": "D9L-806",
            "DATETIME": "220506120345"
        },
        {
            "CODE": "K45I",
            "GROUP": "SLI",
            "NAME": "F2C-818",
            "DATETIME": "220506115333"
        },
        {
            "CODE": "K46L",
            "GROUP": "FERMINA",
            "NAME": "AVD-777",
            "DATETIME": "220506120229"
        },
        {
            "CODE": "K46V",
            "GROUP": "AXON",
            "NAME": "V1A-871",
            "DATETIME": "220506120510"
        },
        {
            "CODE": "K46Z",
            "GROUP": "S.ANITA",
            "NAME": "B1C-923",
            "DATETIME": "220506114116"
        },
        {
            "CODE": "K47L",
            "GROUP": "FERMINA",
            "NAME": "C4F-867",
            "DATETIME": "220506115254"
        },
        {
            "CODE": "K47M",
            "GROUP": "T.DARONI",
            "NAME": "AWG-901",
            "DATETIME": "220506114820"
        },
        {
            "CODE": "K47Z",
            "GROUP": "SANTAINE",
            "NAME": "D8O-876",
            "DATETIME": "220506111947"
        },
        {
            "CODE": "K482",
            "GROUP": "SANTAINE",
            "NAME": "D8P-927",
            "DATETIME": "220209133500"
        },
        {
            "CODE": "K487",
            "GROUP": "FIERRO",
            "NAME": "AVH-798",
            "DATETIME": "220506120425"
        },
        {
            "CODE": "K489",
            "GROUP": "JAIPLAST",
            "NAME": "WGE-728",
            "DATETIME": "220506120108"
        },
        {
            "CODE": "K49E",
            "GROUP": "GONZALES",
            "NAME": "AVN-936",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "K49G",
            "GROUP": "ONCOY",
            "NAME": "D6T-847",
            "DATETIME": "220506110541"
        },
        {
            "CODE": "K4AY",
            "GROUP": "PVISUAL",
            "NAME": "B3Y-871",
            "DATETIME": "220506103749"
        },
        {
            "CODE": "K4B0",
            "GROUP": "ALPISTE",
            "NAME": "AMO-741",
            "DATETIME": "220506120453"
        },
        {
            "CODE": "K4B8",
            "GROUP": "MOTORED",
            "NAME": "IV-2486",
            "DATETIME": "220429171530"
        },
        {
            "CODE": "K4B9",
            "GROUP": "MOTORED",
            "NAME": "IV-2444",
            "DATETIME": "220429175102"
        },
        {
            "CODE": "K4BB",
            "GROUP": "TRANSITA",
            "NAME": "ABL-814",
            "DATETIME": "220506112901"
        },
        {
            "CODE": "K4BD",
            "GROUP": "FERYMAR",
            "NAME": "B4P-704",
            "DATETIME": "220506111010"
        },
        {
            "CODE": "K4BG",
            "GROUP": "FERYMAR",
            "NAME": "C5D-923",
            "DATETIME": "220506120447"
        },
        {
            "CODE": "K4BH",
            "GROUP": "FERYMAR",
            "NAME": "C5Q-806",
            "DATETIME": "220506105053"
        },
        {
            "CODE": "K4BI",
            "GROUP": "FERYMAR",
            "NAME": "C5M-899",
            "DATETIME": "220207081602"
        },
        {
            "CODE": "K4BW",
            "GROUP": "SAGA",
            "NAME": "B1M-287",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K4BX",
            "GROUP": "SIREB",
            "NAME": "D7X-879",
            "DATETIME": "220506072625"
        },
        {
            "CODE": "K4C0",
            "GROUP": "TMORALES",
            "NAME": "C5S-822",
            "DATETIME": "220506110937"
        },
        {
            "CODE": "K4C1",
            "GROUP": "SOLHYM",
            "NAME": "BFR-780",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "K4C9",
            "GROUP": "FERREMAQ",
            "NAME": "6064",
            "DATETIME": "220506120446"
        },
        {
            "CODE": "K4CE",
            "GROUP": "PACIFICO",
            "NAME": "BHJ-644",
            "DATETIME": "220506114403"
        },
        {
            "CODE": "K4CF",
            "GROUP": "T-PRESTA",
            "NAME": "AFX-599",
            "DATETIME": "220506120429"
        },
        {
            "CODE": "K4CG",
            "GROUP": "FERMINA",
            "NAME": "C0I-875",
            "DATETIME": "220404184747"
        },
        {
            "CODE": "K4CJ",
            "GROUP": "SOLHYM",
            "NAME": "T6I-936",
            "DATETIME": "220506120246"
        },
        {
            "CODE": "K4CO",
            "GROUP": "TAXI AH",
            "NAME": "F8E-498",
            "DATETIME": "220506120344"
        },
        {
            "CODE": "K4CP",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-267",
            "DATETIME": "220506115434"
        },
        {
            "CODE": "K4D6",
            "GROUP": "GILDEMEI",
            "NAME": "BFK-100",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "K4DE",
            "GROUP": "RUALTOUR",
            "NAME": "D3A-954",
            "DATETIME": "220506114341"
        },
        {
            "CODE": "K4DQ",
            "GROUP": "SANTAINE",
            "NAME": "ANQ-715",
            "DATETIME": "220503102709"
        },
        {
            "CODE": "K4DV",
            "GROUP": "GILDEMEI",
            "NAME": "BFO-607",
            "DATETIME": "220506112917"
        },
        {
            "CODE": "K4DX",
            "GROUP": "ORBIS",
            "NAME": "B9G-750",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K4E0",
            "GROUP": "PART BET",
            "NAME": "BYU-055",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K4EB",
            "GROUP": "LIMA RES",
            "NAME": "AYO-757",
            "DATETIME": "220506115412"
        },
        {
            "CODE": "K4EC",
            "GROUP": "FAMAI",
            "NAME": "C0C-801",
            "DATETIME": "220506115953"
        },
        {
            "CODE": "K4EH",
            "GROUP": "FAMAI",
            "NAME": "V9V-900",
            "DATETIME": "220506064506"
        },
        {
            "CODE": "K4EL",
            "GROUP": "PART BET",
            "NAME": "BFY-462",
            "DATETIME": "220506115051"
        },
        {
            "CODE": "K4EN",
            "GROUP": "TIM",
            "NAME": "BMC-466",
            "DATETIME": "220506120516"
        },
        {
            "CODE": "K4EW",
            "GROUP": "INLAND",
            "NAME": "C9D-961",
            "DATETIME": "220506120510"
        },
        {
            "CODE": "K4EZ",
            "GROUP": "RENTING",
            "NAME": "BEQ-269",
            "DATETIME": "220408115024"
        },
        {
            "CODE": "K4F0",
            "GROUP": "STA INES",
            "NAME": "AWR-874",
            "DATETIME": "220506120426"
        },
        {
            "CODE": "K4F2",
            "GROUP": "GILDEMEI",
            "NAME": "BHE-297",
            "DATETIME": "220506100853"
        },
        {
            "CODE": "K4F3",
            "GROUP": "FERMINA",
            "NAME": "D7D-773",
            "DATETIME": "220506115400"
        },
        {
            "CODE": "K4F4",
            "GROUP": "FERREMAQ",
            "NAME": "537139",
            "DATETIME": "220506120438"
        },
        {
            "CODE": "K4F7",
            "GROUP": "T.BALDEO",
            "NAME": "C6O-961",
            "DATETIME": "220506115249"
        },
        {
            "CODE": "K4FE",
            "GROUP": "DRAEWON",
            "NAME": "P2H-959",
            "DATETIME": "220506114713"
        },
        {
            "CODE": "K4FF",
            "GROUP": "INTERSEN",
            "NAME": "C5E-707",
            "DATETIME": "220506083654"
        },
        {
            "CODE": "K4FI",
            "GROUP": "ELECTRO",
            "NAME": "BEZ-259",
            "DATETIME": "220506120038"
        },
        {
            "CODE": "K4FO",
            "GROUP": "GILDEMEI",
            "NAME": "BHD-003",
            "DATETIME": "220506115355"
        },
        {
            "CODE": "K4FP",
            "GROUP": "FAMAI",
            "NAME": "V9W-705",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "K4FQ",
            "GROUP": "SOLHYM",
            "NAME": "BFK-913",
            "DATETIME": "220506120428"
        },
        {
            "CODE": "K4FR",
            "GROUP": "SOLGASTR",
            "NAME": "AWC-992",
            "DATETIME": "220504172906"
        },
        {
            "CODE": "K4FS",
            "GROUP": "S.BARTOL",
            "NAME": "500115",
            "DATETIME": "220420120017"
        },
        {
            "CODE": "K4FV",
            "GROUP": "GILDEMEI",
            "NAME": "BFX-535",
            "DATETIME": "220506114751"
        },
        {
            "CODE": "K4G5",
            "GROUP": "POSITIVA",
            "NAME": "AHW-366",
            "DATETIME": "220506120059"
        },
        {
            "CODE": "K4G6",
            "GROUP": "SINCONVE",
            "NAME": "B7H-744",
            "DATETIME": "220506080008"
        },
        {
            "CODE": "K4G9",
            "GROUP": "MULTIMOD",
            "NAME": "BNH-752",
            "DATETIME": "220506115422"
        },
        {
            "CODE": "K4GA",
            "GROUP": "TRADESUR",
            "NAME": "BMI-818",
            "DATETIME": "220506120502"
        },
        {
            "CODE": "K4GH",
            "GROUP": "DRAEWON",
            "NAME": "P2H-956",
            "DATETIME": "220506114036"
        },
        {
            "CODE": "K4GK",
            "GROUP": "GILDEMEI",
            "NAME": "BHG-069",
            "DATETIME": "220506114056"
        },
        {
            "CODE": "K4GO",
            "GROUP": "VALMONT",
            "NAME": "D9T-875",
            "DATETIME": "220506092625"
        },
        {
            "CODE": "K4GR",
            "GROUP": "ORBIS",
            "NAME": "B8D-714",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "K4GU",
            "GROUP": "FERREYRO",
            "NAME": "622381",
            "DATETIME": "220506120453"
        },
        {
            "CODE": "K4GY",
            "GROUP": "ICP",
            "NAME": "ANV-934",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K4H0",
            "GROUP": "ICP",
            "NAME": "ANV-825",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "K4H9",
            "GROUP": "S BARTOL",
            "NAME": "825431",
            "DATETIME": "220506115944"
        },
        {
            "CODE": "K4HC",
            "GROUP": "PART-BET",
            "NAME": "P3I-947",
            "DATETIME": "220506114404"
        },
        {
            "CODE": "K4HD",
            "GROUP": "T.BALDEO",
            "NAME": "F4V-951",
            "DATETIME": "220506115612"
        },
        {
            "CODE": "K4HE",
            "GROUP": "ELEC JM",
            "NAME": "BBV-906",
            "DATETIME": "220506113504"
        },
        {
            "CODE": "K4HH",
            "GROUP": "T.WDJC",
            "NAME": "C4A-900",
            "DATETIME": "220506114303"
        },
        {
            "CODE": "K4HK",
            "GROUP": "VALMONT",
            "NAME": "AWP-848",
            "DATETIME": "220506082933"
        },
        {
            "CODE": "K4HQ",
            "GROUP": "NOR OIL",
            "NAME": "P2W-895",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K4HT",
            "GROUP": "PART BET",
            "NAME": "F5X-087",
            "DATETIME": "220506112852"
        },
        {
            "CODE": "K4HW",
            "GROUP": "PART BET",
            "NAME": "X4O-776",
            "DATETIME": "220506115149"
        },
        {
            "CODE": "K4HY",
            "GROUP": "V.CASTRO",
            "NAME": "AVG-278",
            "DATETIME": "220506120123"
        },
        {
            "CODE": "K4HZ",
            "GROUP": "FAZIO",
            "NAME": "F2Z-724",
            "DATETIME": "220506115757"
        },
        {
            "CODE": "K4I1",
            "GROUP": "PARTICUL",
            "NAME": "C0Q-240",
            "DATETIME": "220506113828"
        },
        {
            "CODE": "K4I4",
            "GROUP": "MACC-HER",
            "NAME": "7243-OB",
            "DATETIME": "220429093120"
        },
        {
            "CODE": "K4I6",
            "GROUP": "TICLAVIL",
            "NAME": "ATE-870",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K4I9",
            "GROUP": "MAPFRE",
            "NAME": "V0S-877",
            "DATETIME": "220506114152"
        },
        {
            "CODE": "K4IA",
            "GROUP": "S BARTOL",
            "NAME": "500036",
            "DATETIME": "220506120119"
        },
        {
            "CODE": "K4IH",
            "GROUP": "ICP",
            "NAME": "ANV-827",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "K4IR",
            "GROUP": "PART BET",
            "NAME": "M6P-711",
            "DATETIME": "220506115114"
        },
        {
            "CODE": "K4IS",
            "GROUP": "JAIPLAST",
            "NAME": "AVV-839",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K4IT",
            "GROUP": "PART BET",
            "NAME": "Z6Q-033",
            "DATETIME": "220506120441"
        },
        {
            "CODE": "K4IU",
            "GROUP": "VALSAGAS",
            "NAME": "F9L-973",
            "DATETIME": "220506115808"
        },
        {
            "CODE": "K4IV",
            "GROUP": "LISTOTAX",
            "NAME": "BYP-325",
            "DATETIME": "220506115408"
        },
        {
            "CODE": "K4IX",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-279",
            "DATETIME": "220506115652"
        },
        {
            "CODE": "K4IY",
            "GROUP": "PROV NAC",
            "NAME": "EGQ-178",
            "DATETIME": "220426175740"
        },
        {
            "CODE": "K4J2",
            "GROUP": "CIVA",
            "NAME": "BYT-346",
            "DATETIME": "220303111723"
        },
        {
            "CODE": "K4J4",
            "GROUP": "AUTOESPA",
            "NAME": "BHM-170",
            "DATETIME": "220506112332"
        },
        {
            "CODE": "K4J5",
            "GROUP": "SANTAINE",
            "NAME": "D8O-898",
            "DATETIME": "220110150156"
        },
        {
            "CODE": "K4JB",
            "GROUP": "AUTOESPA",
            "NAME": "BHN-650",
            "DATETIME": "220506113255"
        },
        {
            "CODE": "K4JG",
            "GROUP": "ASEGURAD",
            "NAME": "BJM-693",
            "DATETIME": "220430201719"
        },
        {
            "CODE": "K4JK",
            "GROUP": "IPANAQUE",
            "NAME": "BJN-658",
            "DATETIME": "220506113438"
        },
        {
            "CODE": "K4JU",
            "GROUP": "ONCOY",
            "NAME": "AVW-722",
            "DATETIME": "220506115858"
        },
        {
            "CODE": "K4JV",
            "GROUP": "PART BET",
            "NAME": "BHY-110",
            "DATETIME": "220506114443"
        },
        {
            "CODE": "K4JX",
            "GROUP": "HILARIO",
            "NAME": "D7U-744",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K4JZ",
            "GROUP": "MIGUEL",
            "NAME": "V0W-788",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K4K0",
            "GROUP": "S&R",
            "NAME": "BKG-731",
            "DATETIME": "220506120516"
        },
        {
            "CODE": "K4K2",
            "GROUP": "TCARRANZ",
            "NAME": "AJR-833",
            "DATETIME": "220506114407"
        },
        {
            "CODE": "K4K5",
            "GROUP": "PART BET",
            "NAME": "BSW-125",
            "DATETIME": "220506115931"
        },
        {
            "CODE": "K4K7",
            "GROUP": "T-PRESTA",
            "NAME": "ARG-538",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "K4KA",
            "GROUP": "SAN MART",
            "NAME": "D4O-948",
            "DATETIME": "220506115648"
        },
        {
            "CODE": "K4KJ",
            "GROUP": "GILDEMEI",
            "NAME": "BFX-315",
            "DATETIME": "220506115647"
        },
        {
            "CODE": "K4KP",
            "GROUP": "GILDEMEI",
            "NAME": "BFX-638",
            "DATETIME": "220506114447"
        },
        {
            "CODE": "K4KR",
            "GROUP": "SOLGASTR",
            "NAME": "F1L-972",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "K4KS",
            "GROUP": "GILDEMEI",
            "NAME": "BFV-273",
            "DATETIME": "220506113443"
        },
        {
            "CODE": "K4KW",
            "GROUP": "POSITIVA",
            "NAME": "BKX-085",
            "DATETIME": "220506113813"
        },
        {
            "CODE": "K4KX",
            "GROUP": "PART BET",
            "NAME": "AZF-087",
            "DATETIME": "220506112714"
        },
        {
            "CODE": "K4KY",
            "GROUP": "PART BET",
            "NAME": "BUO-556",
            "DATETIME": "220506120002"
        },
        {
            "CODE": "K4L6",
            "GROUP": "RENTING",
            "NAME": "BDT-635",
            "DATETIME": "220505182023"
        },
        {
            "CODE": "K4L9",
            "GROUP": "MACAVAL",
            "NAME": "AEB-924",
            "DATETIME": "220506115518"
        },
        {
            "CODE": "K4LA",
            "GROUP": "RIMAC",
            "NAME": "BKW-079",
            "DATETIME": "220506115145"
        },
        {
            "CODE": "K4LC",
            "GROUP": "SONIC",
            "NAME": "AZS-003",
            "DATETIME": "220409060951"
        },
        {
            "CODE": "K4LG",
            "GROUP": "COCHARCA",
            "NAME": "ATW-973",
            "DATETIME": "220501100750"
        },
        {
            "CODE": "K4LJ",
            "GROUP": "SINCONVE",
            "NAME": "BLR-248",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K4LK",
            "GROUP": "TMC",
            "NAME": "ATN-750",
            "DATETIME": "220506115550"
        },
        {
            "CODE": "K4LP",
            "GROUP": "GILDEMEI",
            "NAME": "BEM-030",
            "DATETIME": "220506115813"
        },
        {
            "CODE": "K4LR",
            "GROUP": "FERREMAQ",
            "NAME": "2001",
            "DATETIME": "220506113836"
        },
        {
            "CODE": "K4LV",
            "GROUP": "SAGA",
            "NAME": "A8X-110",
            "DATETIME": "220506113104"
        },
        {
            "CODE": "K4LX",
            "GROUP": "SOLHYM",
            "NAME": "F6T-779",
            "DATETIME": "220506120313"
        },
        {
            "CODE": "K4LZ",
            "GROUP": "UCELLI",
            "NAME": "AEW-354",
            "DATETIME": "220506113138"
        },
        {
            "CODE": "K4M3",
            "GROUP": "S.BARTOL",
            "NAME": "500042",
            "DATETIME": "220506115003"
        },
        {
            "CODE": "K4M6",
            "GROUP": "RIMAC",
            "NAME": "BFZ-323",
            "DATETIME": "220506115842"
        },
        {
            "CODE": "K4M7",
            "GROUP": "SAFETY",
            "NAME": "M3A-705",
            "DATETIME": "220506115302"
        },
        {
            "CODE": "K4M9",
            "GROUP": "ORBIS",
            "NAME": "ACD-753",
            "DATETIME": "220506120450"
        },
        {
            "CODE": "K4ME",
            "GROUP": "ICP",
            "NAME": "AXQ-800",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "K4MF",
            "GROUP": "PART BET",
            "NAME": "AWS-935",
            "DATETIME": "220506112952"
        },
        {
            "CODE": "K4MG",
            "GROUP": "SOLHYM",
            "NAME": "AYH-846",
            "DATETIME": "220506111349"
        },
        {
            "CODE": "K4MK",
            "GROUP": "YUPUPUPU",
            "NAME": "M6M-916",
            "DATETIME": "220506115602"
        },
        {
            "CODE": "K4ML",
            "GROUP": "ASEGURAD",
            "NAME": "AYI-241",
            "DATETIME": "220506113724"
        },
        {
            "CODE": "K4MN",
            "GROUP": "SOLGASTR",
            "NAME": "F3V-983",
            "DATETIME": "220506115242"
        },
        {
            "CODE": "K4MO",
            "GROUP": "COLI",
            "NAME": "BKV-543",
            "DATETIME": "220506115232"
        },
        {
            "CODE": "K4MV",
            "GROUP": "GIANT",
            "NAME": "BBG-933",
            "DATETIME": "220505132549"
        },
        {
            "CODE": "K4MX",
            "GROUP": "T-PRESTA",
            "NAME": "APK-164",
            "DATETIME": "220403032859"
        },
        {
            "CODE": "K4MY",
            "GROUP": "C.SONIC",
            "NAME": "AMV-402",
            "DATETIME": "220504225533"
        },
        {
            "CODE": "K4MZ",
            "GROUP": "NOR OIL",
            "NAME": "W6B-876",
            "DATETIME": "220506115638"
        },
        {
            "CODE": "K4N3",
            "GROUP": "T.VICKY",
            "NAME": "AVP-992",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K4N4",
            "GROUP": "GIANT",
            "NAME": "BBH-833",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K4N5",
            "GROUP": "FRIO IMP",
            "NAME": "F5L-751",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "K4N6",
            "GROUP": "PART BET",
            "NAME": "BLS-724",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "K4N7",
            "GROUP": "SOLGASER",
            "NAME": "C4V-987",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K4NA",
            "GROUP": "POLMART",
            "NAME": "AXX-976",
            "DATETIME": "220506115601"
        },
        {
            "CODE": "K4NC",
            "GROUP": "OBRAS CI",
            "NAME": "D7V-583",
            "DATETIME": "220506115538"
        },
        {
            "CODE": "K4ND",
            "GROUP": "LAUVIDAL",
            "NAME": "D2K-929",
            "DATETIME": "220506120218"
        },
        {
            "CODE": "K4NE",
            "GROUP": "PART BET",
            "NAME": "BBO-364",
            "DATETIME": "220506115106"
        },
        {
            "CODE": "K4NF",
            "GROUP": "LAUVIDAL",
            "NAME": "A7J-899",
            "DATETIME": "220506120514"
        },
        {
            "CODE": "K4NH",
            "GROUP": "FUENTES",
            "NAME": "BWZ-309",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K4NJ",
            "GROUP": "ORBIS",
            "NAME": "ARE-749",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K4NK",
            "GROUP": "LAUVIDAL",
            "NAME": "BFG-854",
            "DATETIME": "220506120008"
        },
        {
            "CODE": "K4NM",
            "GROUP": "S.MARTIN",
            "NAME": "M6O-865 ",
            "DATETIME": "220506120232"
        },
        {
            "CODE": "K4NP",
            "GROUP": "LAUVIDAL",
            "NAME": "BFG-860",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "K4NR",
            "GROUP": "LAUVIDAL",
            "NAME": "C4V-706",
            "DATETIME": "220502113719"
        },
        {
            "CODE": "K4NS",
            "GROUP": "LAUVIDAL",
            "NAME": "C5U-331",
            "DATETIME": "220506115851"
        },
        {
            "CODE": "K4NT",
            "GROUP": "LAUVIDAL",
            "NAME": "AED-101",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "K4NU",
            "GROUP": "LAUVIDAL",
            "NAME": "A4T-189",
            "DATETIME": "220506115137"
        },
        {
            "CODE": "K4NW",
            "GROUP": "PART BET",
            "NAME": "BJC-048",
            "DATETIME": "220506114119"
        },
        {
            "CODE": "K4NY",
            "GROUP": "LAUVIDAL",
            "NAME": "F1O-293",
            "DATETIME": "220506115719"
        },
        {
            "CODE": "K4NZ",
            "GROUP": "GRAMA",
            "NAME": "AEN-702",
            "DATETIME": "220506115933"
        },
        {
            "CODE": "K4O1",
            "GROUP": "LAUVIDAL",
            "NAME": "A3T-343",
            "DATETIME": "220506120511"
        },
        {
            "CODE": "K4O2",
            "GROUP": "GILDEMEI",
            "NAME": "AVU-436",
            "DATETIME": "220506120505"
        },
        {
            "CODE": "K4O3",
            "GROUP": "GZ AIR",
            "NAME": "AZK-713",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K4O6",
            "GROUP": "GILDEMEI",
            "NAME": "BYZ-353",
            "DATETIME": "220506115319"
        },
        {
            "CODE": "K4O8",
            "GROUP": "LAUVIDAL",
            "NAME": "ADC-469",
            "DATETIME": "220506120200"
        },
        {
            "CODE": "K4OA",
            "GROUP": "LAUVIDAL",
            "NAME": "C0J-030",
            "DATETIME": "220506115305"
        },
        {
            "CODE": "K4OB",
            "GROUP": "T.BALDEO",
            "NAME": "C8J-959",
            "DATETIME": "220506115443"
        },
        {
            "CODE": "K4OD",
            "GROUP": "SEÑUELO",
            "NAME": "BFJ-881S",
            "DATETIME": "220506115533"
        },
        {
            "CODE": "K4OG",
            "GROUP": "IWANCO",
            "NAME": "BEB-899",
            "DATETIME": "220506120220"
        },
        {
            "CODE": "K4OH",
            "GROUP": "GILDEMEI",
            "NAME": "BFV-076",
            "DATETIME": "220506120435"
        },
        {
            "CODE": "K4OJ",
            "GROUP": "POS SOLU",
            "NAME": "AKT-921",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "K4OK",
            "GROUP": "PART BET",
            "NAME": "BCA-625",
            "DATETIME": "220506115852"
        },
        {
            "CODE": "K4ON",
            "GROUP": "AGRONEGO",
            "NAME": "C7P-781",
            "DATETIME": "220506120411"
        },
        {
            "CODE": "K4OP",
            "GROUP": "SALUD",
            "NAME": "EUG-988",
            "DATETIME": "220506120009"
        },
        {
            "CODE": "K4OT",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-265",
            "DATETIME": "220506120118"
        },
        {
            "CODE": "K4OX",
            "GROUP": "GILDEMEI",
            "NAME": "BFS-251",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K4OY",
            "GROUP": "INTERSEN",
            "NAME": "AWC-705",
            "DATETIME": "220506120422"
        },
        {
            "CODE": "K4OZ",
            "GROUP": "SAGA",
            "NAME": "BMZ-830",
            "DATETIME": "220506120333"
        },
        {
            "CODE": "K4P5",
            "GROUP": "PART BET",
            "NAME": "BKD-149",
            "DATETIME": "220506104228"
        },
        {
            "CODE": "K4PD",
            "GROUP": "QUICORNA",
            "NAME": "M4W-452",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K4PF",
            "GROUP": "SOLGASTR",
            "NAME": "AWI-971",
            "DATETIME": "220430151326"
        },
        {
            "CODE": "K4PN",
            "GROUP": "EMANUEL",
            "NAME": "F9R-985",
            "DATETIME": "220504181041"
        },
        {
            "CODE": "K4PP",
            "GROUP": "GILDEMEI",
            "NAME": "BCU-392",
            "DATETIME": "220506115609"
        },
        {
            "CODE": "K4PQ",
            "GROUP": "PACIFICO",
            "NAME": "S1W-801",
            "DATETIME": "220506120349"
        },
        {
            "CODE": "K4PT",
            "GROUP": "SANTAINE",
            "NAME": "D6W-839",
            "DATETIME": "220506115446"
        },
        {
            "CODE": "K4PX",
            "GROUP": "JSINVERS",
            "NAME": "D1U-796",
            "DATETIME": "220506080703"
        },
        {
            "CODE": "K4Q0",
            "GROUP": "GILDEMEI",
            "NAME": "BFA-525",
            "DATETIME": "220505161625"
        },
        {
            "CODE": "K4Q5",
            "GROUP": "T.WEIGHT",
            "NAME": "BZJ-029",
            "DATETIME": "220506114946"
        },
        {
            "CODE": "K4Q7",
            "GROUP": "GILDEMEI",
            "NAME": "BEZ-173",
            "DATETIME": "220506102413"
        },
        {
            "CODE": "K4QE",
            "GROUP": "CHAVEZPA",
            "NAME": "F3J-947",
            "DATETIME": "220506115230"
        },
        {
            "CODE": "K4QG",
            "GROUP": "PART BET",
            "NAME": "H2V-821",
            "DATETIME": "220506115028"
        },
        {
            "CODE": "K4QH",
            "GROUP": "YUPUPUPU",
            "NAME": "V8Z-200",
            "DATETIME": "220506115934"
        },
        {
            "CODE": "K4QQ",
            "GROUP": "A&J",
            "NAME": "BNE-725",
            "DATETIME": "220506115835"
        },
        {
            "CODE": "K4QR",
            "GROUP": "GILDEMEI",
            "NAME": "AYD-886",
            "DATETIME": "220506114342"
        },
        {
            "CODE": "K4QS",
            "GROUP": "T.CAMILA",
            "NAME": "F3C-974",
            "DATETIME": "220112190121"
        },
        {
            "CODE": "K4QY",
            "GROUP": "FAZIO",
            "NAME": "C5Z-755",
            "DATETIME": "220504190751"
        },
        {
            "CODE": "K4R3",
            "GROUP": "GRAMA",
            "NAME": "1983-HA",
            "DATETIME": "220506093359"
        },
        {
            "CODE": "K4R7",
            "GROUP": "ING.Y.EM",
            "NAME": "BFB-609",
            "DATETIME": "220506114455"
        },
        {
            "CODE": "K4R8",
            "GROUP": "Q.P.R",
            "NAME": "BNL-845",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "K4R9",
            "GROUP": "STA-ROSA",
            "NAME": "AXW-798",
            "DATETIME": "220506120405"
        },
        {
            "CODE": "K4RA",
            "GROUP": "SOLGASTR",
            "NAME": "F3Z-994",
            "DATETIME": "220428171912"
        },
        {
            "CODE": "K4RF",
            "GROUP": "PART BET",
            "NAME": "BFU-540",
            "DATETIME": "220505202807"
        },
        {
            "CODE": "K4RH",
            "GROUP": "GILDEMEI",
            "NAME": "BEV-531",
            "DATETIME": "220506113916"
        },
        {
            "CODE": "K4RP",
            "GROUP": "POSITIVA",
            "NAME": "ANP-870",
            "DATETIME": "220506114229"
        },
        {
            "CODE": "K4RU",
            "GROUP": "ANDERS",
            "NAME": "C7O-897",
            "DATETIME": "220506115753"
        },
        {
            "CODE": "K4RX",
            "GROUP": "YUPUPUPU",
            "NAME": "T4I-898",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "K4S0",
            "GROUP": "OLIVARES",
            "NAME": "AAG-880",
            "DATETIME": "220506120455"
        },
        {
            "CODE": "K4S4",
            "GROUP": "TAXISATE",
            "NAME": "BEW-316",
            "DATETIME": "220506113729"
        },
        {
            "CODE": "K4S6",
            "GROUP": "LISTOTAX",
            "NAME": "BYN-343",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K4S7",
            "GROUP": "PAR BETA",
            "NAME": "BWY-250",
            "DATETIME": "220506120122"
        },
        {
            "CODE": "K4SA",
            "GROUP": "GOO TRIP",
            "NAME": "V0Q-803",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K4SC",
            "GROUP": "EYON",
            "NAME": "AAL-809",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K4SD",
            "GROUP": "EYON",
            "NAME": "AAZ-916",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "K4SE",
            "GROUP": "SINCONVE",
            "NAME": "AYV-800",
            "DATETIME": "220506112533"
        },
        {
            "CODE": "K4SI",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-505",
            "DATETIME": "220506115223"
        },
        {
            "CODE": "K4SJ",
            "GROUP": "PACIFICO",
            "NAME": "BDJ-640",
            "DATETIME": "220506113822"
        },
        {
            "CODE": "K4SR",
            "GROUP": "VALMONT",
            "NAME": "AUP-719",
            "DATETIME": "220502232416"
        },
        {
            "CODE": "K4SS",
            "GROUP": "PART BET",
            "NAME": "BFG-386",
            "DATETIME": "220506115622"
        },
        {
            "CODE": "K4SX",
            "GROUP": "GRAÑA",
            "NAME": "T6L-923",
            "DATETIME": "220506120458"
        },
        {
            "CODE": "K4SY",
            "GROUP": "SINCONVE",
            "NAME": "X4Q-845",
            "DATETIME": "220506114918"
        },
        {
            "CODE": "K4T2",
            "GROUP": "V.CASTRO",
            "NAME": "B2G-525",
            "DATETIME": "220506120527"
        },
        {
            "CODE": "K4T4",
            "GROUP": "LISTO",
            "NAME": "BXY-065",
            "DATETIME": "220506120507"
        },
        {
            "CODE": "K4TB",
            "GROUP": "VIA FOOD",
            "NAME": "BAC-740",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K4TE",
            "GROUP": "MAPFRE",
            "NAME": "BFG-064",
            "DATETIME": "220506120341"
        },
        {
            "CODE": "K4TH",
            "GROUP": "FERREMAQ",
            "NAME": "4030",
            "DATETIME": "220506113111"
        },
        {
            "CODE": "K4TQ",
            "GROUP": "PART BET",
            "NAME": "AMU-217",
            "DATETIME": "220506112840"
        },
        {
            "CODE": "K4TT",
            "GROUP": "MAPFRE",
            "NAME": "BAM-907",
            "DATETIME": "220506115455"
        },
        {
            "CODE": "K4U1",
            "GROUP": "TICLAVIL",
            "NAME": "ABK-971",
            "DATETIME": "220506120105"
        },
        {
            "CODE": "K4U2",
            "GROUP": "SINCONVE",
            "NAME": "BCP-372",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "K4U3",
            "GROUP": "OLATI",
            "NAME": "BNF-764",
            "DATETIME": "220504105902"
        },
        {
            "CODE": "K4U8",
            "GROUP": "ARBECO",
            "NAME": "W5M-780",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "K4V1",
            "GROUP": "T.SANTOS",
            "NAME": "BBU-823",
            "DATETIME": "220505153300"
        },
        {
            "CODE": "K4VD",
            "GROUP": "GILDEMEI",
            "NAME": "BFC-176",
            "DATETIME": "220506071035"
        },
        {
            "CODE": "K4VF",
            "GROUP": "MAFISA",
            "NAME": "XBL-966",
            "DATETIME": "220506115452"
        },
        {
            "CODE": "K4VM",
            "GROUP": "TEMBLADE",
            "NAME": "F8G-814",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "K4VT",
            "GROUP": "FERMINA",
            "NAME": "AZK-701",
            "DATETIME": "220506113716"
        },
        {
            "CODE": "K4VV",
            "GROUP": "NETZSCH",
            "NAME": "AYE-949",
            "DATETIME": "220506102653"
        },
        {
            "CODE": "K4VW",
            "GROUP": "NETZSCH",
            "NAME": "AYE-945",
            "DATETIME": "220506110119"
        },
        {
            "CODE": "K4W3",
            "GROUP": "VALMONT",
            "NAME": "M1Q-907",
            "DATETIME": "220506095744"
        },
        {
            "CODE": "K4W7",
            "GROUP": "T.SANTOS",
            "NAME": "F9H-760",
            "DATETIME": "220506120416"
        },
        {
            "CODE": "K4WJ",
            "GROUP": "GRAÑA",
            "NAME": "17028",
            "DATETIME": "220506120154"
        },
        {
            "CODE": "K4WL",
            "GROUP": "GRAÑA",
            "NAME": "AKT-930",
            "DATETIME": "220506114650"
        },
        {
            "CODE": "K4WN",
            "GROUP": "A&J",
            "NAME": "BND-818",
            "DATETIME": "220411083103"
        },
        {
            "CODE": "K4WR",
            "GROUP": "BONALIS",
            "NAME": "BBS-665",
            "DATETIME": "220506115610"
        },
        {
            "CODE": "K4WT",
            "GROUP": "LYM",
            "NAME": "AYT-748",
            "DATETIME": "220506115608"
        },
        {
            "CODE": "K4WW",
            "GROUP": "GRAÑA",
            "NAME": "F0A-907",
            "DATETIME": "220309104150"
        },
        {
            "CODE": "K4X0",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-434",
            "DATETIME": "220506115706"
        },
        {
            "CODE": "K4X1",
            "GROUP": "SINCONVE",
            "NAME": "AZX-928",
            "DATETIME": "220506114825"
        },
        {
            "CODE": "K4X5",
            "GROUP": "A&J",
            "NAME": "BND-878",
            "DATETIME": "220330101551"
        },
        {
            "CODE": "K4X8",
            "GROUP": "Q.P.R",
            "NAME": "BNM-794",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K4XB",
            "GROUP": "BONALIS",
            "NAME": "F3H-946",
            "DATETIME": "220506120059"
        },
        {
            "CODE": "K4XC",
            "GROUP": "JDM",
            "NAME": "VBD-902",
            "DATETIME": "220506115226"
        },
        {
            "CODE": "K4XE",
            "GROUP": "GRAÑA",
            "NAME": "17029",
            "DATETIME": "220506120220"
        },
        {
            "CODE": "K4XI",
            "GROUP": "LISTOTAX",
            "NAME": "BYQ-209",
            "DATETIME": "220506120423"
        },
        {
            "CODE": "K4XL",
            "GROUP": "HERCON",
            "NAME": "A0R-841",
            "DATETIME": "220425211412"
        },
        {
            "CODE": "K4XN",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-112",
            "DATETIME": "220506115416"
        },
        {
            "CODE": "K4XQ",
            "GROUP": "AGAD OL",
            "NAME": "AMH-910",
            "DATETIME": "220506120404"
        },
        {
            "CODE": "K4XS",
            "GROUP": "IMARK",
            "NAME": "AZM-939",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "K4XX",
            "GROUP": "LISTOTAX",
            "NAME": "BYP-326",
            "DATETIME": "220506120118"
        },
        {
            "CODE": "K4XY",
            "GROUP": "IMARK",
            "NAME": "AZL-778",
            "DATETIME": "220506114310"
        },
        {
            "CODE": "K4XZ",
            "GROUP": "PART BET",
            "NAME": "AZX-807",
            "DATETIME": "220506120438"
        },
        {
            "CODE": "K4Y1",
            "GROUP": "GILDEMEI",
            "NAME": "F1Y-968",
            "DATETIME": "220506120103"
        },
        {
            "CODE": "K4Y2",
            "GROUP": "NOR OIL",
            "NAME": "T0F-886",
            "DATETIME": "220506120516"
        },
        {
            "CODE": "K4Y6",
            "GROUP": "RIMAC",
            "NAME": "BHZ-225",
            "DATETIME": "220506100555"
        },
        {
            "CODE": "K4YB",
            "GROUP": "PART BET",
            "NAME": "AZV-780",
            "DATETIME": "220405084748"
        },
        {
            "CODE": "K4YL",
            "GROUP": "AUTOESPA",
            "NAME": "BHM-330",
            "DATETIME": "220506115129"
        },
        {
            "CODE": "K4YM",
            "GROUP": "RENTING",
            "NAME": "BHC-273",
            "DATETIME": "220506114401"
        },
        {
            "CODE": "K4YV",
            "GROUP": "PART BET",
            "NAME": "BLO-344",
            "DATETIME": "220506120331"
        },
        {
            "CODE": "K4YW",
            "GROUP": "GILDEMEI",
            "NAME": "BEX-694",
            "DATETIME": "220506120517"
        },
        {
            "CODE": "K4YX",
            "GROUP": "QUICORNA",
            "NAME": "M5P-861",
            "DATETIME": "220506120505"
        },
        {
            "CODE": "K4Z0",
            "GROUP": "AGRO",
            "NAME": "BCD-786",
            "DATETIME": "220506113745"
        },
        {
            "CODE": "K4Z5",
            "GROUP": "PART BET",
            "NAME": "AXM-720",
            "DATETIME": "220506120323"
        },
        {
            "CODE": "K4Z6",
            "GROUP": "TRADESUR",
            "NAME": "B8O-835",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K4Z9",
            "GROUP": "AGRO",
            "NAME": "BCD-786A",
            "DATETIME": "220506114359"
        },
        {
            "CODE": "K4ZB",
            "GROUP": "SINCONVE",
            "NAME": "BMD-653",
            "DATETIME": "220506114934"
        },
        {
            "CODE": "K4ZD",
            "GROUP": "LISTOTAX",
            "NAME": "BYP-246",
            "DATETIME": "220506115930"
        },
        {
            "CODE": "K4ZE",
            "GROUP": "CALERA",
            "NAME": "AMN-762",
            "DATETIME": "220506120122"
        },
        {
            "CODE": "K4ZH",
            "GROUP": "GILDEMEI",
            "NAME": "BEB-148",
            "DATETIME": "220506112823"
        },
        {
            "CODE": "K4ZI",
            "GROUP": "PART BET",
            "NAME": "BMF-268",
            "DATETIME": "220506114457"
        },
        {
            "CODE": "K4ZJ",
            "GROUP": "GILDEMEI",
            "NAME": "BLY-550",
            "DATETIME": "220506114319"
        },
        {
            "CODE": "K4ZN",
            "GROUP": "PISCIFAC",
            "NAME": "BCF-718",
            "DATETIME": "220506120352"
        },
        {
            "CODE": "K4ZO",
            "GROUP": "FERREYRO",
            "NAME": "87008",
            "DATETIME": "220506120408"
        },
        {
            "CODE": "K4ZS",
            "GROUP": "SINCONVE",
            "NAME": "W4I-567",
            "DATETIME": "220506114355"
        },
        {
            "CODE": "K4ZT",
            "GROUP": "AGRO INK",
            "NAME": "AZE-804",
            "DATETIME": "220505184213"
        },
        {
            "CODE": "K4ZU",
            "GROUP": "LISTOTAX",
            "NAME": "F2E-070",
            "DATETIME": "220506115302"
        },
        {
            "CODE": "K4ZV",
            "GROUP": "SOLHYM",
            "NAME": "BHT-794",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K505",
            "GROUP": "OBRAS CI",
            "NAME": "BLG-593",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K508",
            "GROUP": "GILDEMEI",
            "NAME": "BFS-566",
            "DATETIME": "220506114328"
        },
        {
            "CODE": "K50B",
            "GROUP": "RAGEN",
            "NAME": "F3D-824",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "K50E",
            "GROUP": "SINCONVE",
            "NAME": "AYE-220",
            "DATETIME": "220506113959"
        },
        {
            "CODE": "K50J",
            "GROUP": "PART BET",
            "NAME": "F3Z-961",
            "DATETIME": "220506114600"
        },
        {
            "CODE": "K50K",
            "GROUP": "JDM",
            "NAME": "VBC-929",
            "DATETIME": "220506120305"
        },
        {
            "CODE": "K50P",
            "GROUP": "YUCRA",
            "NAME": "V7S-839",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "K50R",
            "GROUP": "LISTOTAX",
            "NAME": "BYQ-024",
            "DATETIME": "220506115253"
        },
        {
            "CODE": "K50T",
            "GROUP": "FAMAI",
            "NAME": "V9M-924",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K514",
            "GROUP": "PART BET",
            "NAME": "114400",
            "DATETIME": "220506120514"
        },
        {
            "CODE": "K51B",
            "GROUP": "EYON",
            "NAME": "ADK-904",
            "DATETIME": "220506114318"
        },
        {
            "CODE": "K51C",
            "GROUP": "FAMAI",
            "NAME": "VET-965",
            "DATETIME": "220506114608"
        },
        {
            "CODE": "K51K",
            "GROUP": "PART BET",
            "NAME": "T0D-865",
            "DATETIME": "220506115827"
        },
        {
            "CODE": "K51L",
            "GROUP": "PART BET",
            "NAME": "B2K-136",
            "DATETIME": "220427205817"
        },
        {
            "CODE": "K51V",
            "GROUP": "SOLHYM",
            "NAME": "ANY-853",
            "DATETIME": "220506120501"
        },
        {
            "CODE": "K51X",
            "GROUP": "RENPA",
            "NAME": "AZG-709",
            "DATETIME": "220506115537"
        },
        {
            "CODE": "K520",
            "GROUP": "JG3 CONS",
            "NAME": "BHX-776",
            "DATETIME": "220506120119"
        },
        {
            "CODE": "K522",
            "GROUP": "PART BET",
            "NAME": "C1H-780",
            "DATETIME": "220506115852"
        },
        {
            "CODE": "K52A",
            "GROUP": "LINCUNA",
            "NAME": "AHN-887",
            "DATETIME": "220506113124"
        },
        {
            "CODE": "K52E",
            "GROUP": "VALMONT",
            "NAME": "M1Q-913",
            "DATETIME": "220506111119"
        },
        {
            "CODE": "K52F",
            "GROUP": "ALCIDESF",
            "NAME": "AMK-327",
            "DATETIME": "220506120407"
        },
        {
            "CODE": "K52H",
            "GROUP": "PART BET",
            "NAME": "C6Z-155",
            "DATETIME": "220503174210"
        },
        {
            "CODE": "K52I",
            "GROUP": "A&J",
            "NAME": "BND-927",
            "DATETIME": "220506114009"
        },
        {
            "CODE": "K52J",
            "GROUP": "SAN DIEG",
            "NAME": "D8G-708",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K52M",
            "GROUP": "PART BET",
            "NAME": "BRS-047",
            "DATETIME": "220506063658"
        },
        {
            "CODE": "K52O",
            "GROUP": "LISTOTAX",
            "NAME": "BYQ-448",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "K52Q",
            "GROUP": "CARTONES",
            "NAME": "BNQ-703",
            "DATETIME": "220506115208"
        },
        {
            "CODE": "K52T",
            "GROUP": "QUICORNA",
            "NAME": "M6M-826",
            "DATETIME": "220506120359"
        },
        {
            "CODE": "K52Z",
            "GROUP": "ICP",
            "NAME": "AXQ-882",
            "DATETIME": "220412023109"
        },
        {
            "CODE": "K530",
            "GROUP": "SONYC",
            "NAME": "F1N-388",
            "DATETIME": "220506113648"
        },
        {
            "CODE": "K535",
            "GROUP": "PLAZAT",
            "NAME": "C0Y-722",
            "DATETIME": "220506115816"
        },
        {
            "CODE": "K536",
            "GROUP": "S.MARTIN",
            "NAME": "M7G-934",
            "DATETIME": "220506120447"
        },
        {
            "CODE": "K53B",
            "GROUP": "SINCONVE",
            "NAME": "ARN-122",
            "DATETIME": "220506085353"
        },
        {
            "CODE": "K53E",
            "GROUP": "ORO GAS",
            "NAME": "APL-975",
            "DATETIME": "220407195226"
        },
        {
            "CODE": "K53G",
            "GROUP": "JSINVERS",
            "NAME": "ATQ-875",
            "DATETIME": "220506061920"
        },
        {
            "CODE": "K55P",
            "GROUP": "FERREMAQ",
            "NAME": "MF7747",
            "DATETIME": "220404115630"
        },
        {
            "CODE": "K56Y",
            "GROUP": "RENTANOR",
            "NAME": "T9W-898",
            "DATETIME": "220413110841"
        },
        {
            "CODE": "K570",
            "GROUP": "LISTO",
            "NAME": "BYN-345",
            "DATETIME": "220506115325"
        },
        {
            "CODE": "K573",
            "GROUP": "ARBECO",
            "NAME": "ANB-904",
            "DATETIME": "220506120510"
        },
        {
            "CODE": "K574",
            "GROUP": "PART BET",
            "NAME": "AZW-811",
            "DATETIME": "220506115909"
        },
        {
            "CODE": "K575",
            "GROUP": "A&P",
            "NAME": "B2K-941",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "K576",
            "GROUP": "PART BET",
            "NAME": "225671",
            "DATETIME": "220506115756"
        },
        {
            "CODE": "K577",
            "GROUP": "S&R",
            "NAME": "AMW-870",
            "DATETIME": "220506115530"
        },
        {
            "CODE": "K578",
            "GROUP": "SOLGASTR",
            "NAME": "D3Q-987",
            "DATETIME": "220506120248"
        },
        {
            "CODE": "K579",
            "GROUP": "PART BET",
            "NAME": "804209",
            "DATETIME": "220506115311"
        },
        {
            "CODE": "K57A",
            "GROUP": "PART BET",
            "NAME": "BLK-704",
            "DATETIME": "220506120321"
        },
        {
            "CODE": "K57B",
            "GROUP": "PART BET",
            "NAME": "BWG-251",
            "DATETIME": "220506120158"
        },
        {
            "CODE": "K57C",
            "GROUP": "S&R",
            "NAME": "AWL-816",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K57E",
            "GROUP": "SOLGASER",
            "NAME": "C4U-993",
            "DATETIME": "220506115742"
        },
        {
            "CODE": "K57H",
            "GROUP": "PART-BET",
            "NAME": "BLF-908",
            "DATETIME": "220506115631"
        },
        {
            "CODE": "K57L",
            "GROUP": "TRANS.JD",
            "NAME": "D6F-802",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "K57M",
            "GROUP": "LINCUNA",
            "NAME": "BLB-926",
            "DATETIME": "220506115934"
        },
        {
            "CODE": "K57O",
            "GROUP": "LINCUNA",
            "NAME": "BLC-737",
            "DATETIME": "220506075500"
        },
        {
            "CODE": "K57Q",
            "GROUP": "RODRIGUE",
            "NAME": "TAC-927",
            "DATETIME": "220506120526"
        },
        {
            "CODE": "K57R",
            "GROUP": "LINCUNA",
            "NAME": "BLC-711",
            "DATETIME": "220506120036"
        },
        {
            "CODE": "K57S",
            "GROUP": "PART BET",
            "NAME": "BEA-828",
            "DATETIME": "220506115659"
        },
        {
            "CODE": "K57U",
            "GROUP": "PART BET",
            "NAME": "BMW-741",
            "DATETIME": "220506120520"
        },
        {
            "CODE": "K57V",
            "GROUP": "SUEROS",
            "NAME": "V8M-836",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K57X",
            "GROUP": "LINCUNA",
            "NAME": "BLC-721",
            "DATETIME": "220506090849"
        },
        {
            "CODE": "K581",
            "GROUP": "PART BET",
            "NAME": "BKV-785",
            "DATETIME": "220506115623"
        },
        {
            "CODE": "K582",
            "GROUP": "AQUIJE",
            "NAME": "BNP-834",
            "DATETIME": "220506115928"
        },
        {
            "CODE": "K583",
            "GROUP": "TRADESUR",
            "NAME": "BHF-772",
            "DATETIME": "220506115931"
        },
        {
            "CODE": "K585",
            "GROUP": "S.BARTOL",
            "NAME": "500147",
            "DATETIME": "220506120432"
        },
        {
            "CODE": "K587",
            "GROUP": "T-PRESTA",
            "NAME": "A9C-575",
            "DATETIME": "220506115942"
        },
        {
            "CODE": "K588",
            "GROUP": "S&R",
            "NAME": "AWI-725",
            "DATETIME": "220506120510"
        },
        {
            "CODE": "K58A",
            "GROUP": "RIMAC",
            "NAME": "F5A-301",
            "DATETIME": "220506115612"
        },
        {
            "CODE": "K58B",
            "GROUP": "SOLHYM",
            "NAME": "BFW-886",
            "DATETIME": "220506120434"
        },
        {
            "CODE": "K58C",
            "GROUP": "PART BET",
            "NAME": "BDO-553",
            "DATETIME": "220506112545"
        },
        {
            "CODE": "K58D",
            "GROUP": "CAMZA",
            "NAME": "BKR-727",
            "DATETIME": "220506115616"
        },
        {
            "CODE": "K58E",
            "GROUP": "PART BET",
            "NAME": "BKT-934",
            "DATETIME": "220506113548"
        },
        {
            "CODE": "K58F",
            "GROUP": "CABALLER",
            "NAME": "TAC-923",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "K58G",
            "GROUP": "PART BET",
            "NAME": "804372",
            "DATETIME": "220506115900"
        },
        {
            "CODE": "K58H",
            "GROUP": "LINCUNA",
            "NAME": "F7Q-856",
            "DATETIME": "220506095658"
        },
        {
            "CODE": "K58K",
            "GROUP": "AFEM",
            "NAME": "AJM-884",
            "DATETIME": "220506014820"
        },
        {
            "CODE": "K58M",
            "GROUP": "PRUEBASL",
            "NAME": "K58M9999",
            "DATETIME": "220118075003"
        },
        {
            "CODE": "K58P",
            "GROUP": "PRUEBASL",
            "NAME": "K58P9999",
            "DATETIME": "220118081638"
        },
        {
            "CODE": "K58T",
            "GROUP": "QUIMITRA",
            "NAME": "C8E-782",
            "DATETIME": "220505211031"
        },
        {
            "CODE": "K58V",
            "GROUP": "PART BET",
            "NAME": "BTF-533",
            "DATETIME": "220506115325"
        },
        {
            "CODE": "K58X",
            "GROUP": "SOLGASTR",
            "NAME": "F6A-971",
            "DATETIME": "220506115420"
        },
        {
            "CODE": "K593",
            "GROUP": "PRUEBASL",
            "NAME": "K5939999",
            "DATETIME": "220118065935"
        },
        {
            "CODE": "K594",
            "GROUP": "PART BET",
            "NAME": "W4R-156",
            "DATETIME": "220506115831"
        },
        {
            "CODE": "K595",
            "GROUP": "ORBIS",
            "NAME": "BJV-833",
            "DATETIME": "220506115611"
        },
        {
            "CODE": "K598",
            "GROUP": "PART BET",
            "NAME": "BTR-482",
            "DATETIME": "220506120335"
        },
        {
            "CODE": "K599",
            "GROUP": "PRUEBASL",
            "NAME": "K5999999",
            "DATETIME": "220118081901"
        },
        {
            "CODE": "K59A",
            "GROUP": "JSINVERS",
            "NAME": "ARS-946",
            "DATETIME": "220504105042"
        },
        {
            "CODE": "K59B",
            "GROUP": "INVERS57",
            "NAME": "BHQ-874",
            "DATETIME": "220506120115"
        },
        {
            "CODE": "K59D",
            "GROUP": "FRIO IMP",
            "NAME": "Z6A-350",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "K59E",
            "GROUP": "LEASING",
            "NAME": "BHB-559",
            "DATETIME": "220506115457"
        },
        {
            "CODE": "K59F",
            "GROUP": "PART BET",
            "NAME": "BEB-176",
            "DATETIME": "220506115239"
        },
        {
            "CODE": "K59G",
            "GROUP": "PART BET",
            "NAME": "BTP-399",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "K59H",
            "GROUP": "RYVAQM",
            "NAME": "F4Q-701",
            "DATETIME": "220506120324"
        },
        {
            "CODE": "K59L",
            "GROUP": "PART BET",
            "NAME": "BEP-075",
            "DATETIME": "220506115708"
        },
        {
            "CODE": "K59N",
            "GROUP": "ROSELLO",
            "NAME": "AVC-109",
            "DATETIME": "220503210211"
        },
        {
            "CODE": "K59O",
            "GROUP": "GRAMA",
            "NAME": "7509-IB",
            "DATETIME": "220506074318"
        },
        {
            "CODE": "K59Q",
            "GROUP": "RUBIO ES",
            "NAME": "BUF-546",
            "DATETIME": "220430143228"
        },
        {
            "CODE": "K59R",
            "GROUP": "FERREYRO",
            "NAME": "21022",
            "DATETIME": "220506115541"
        },
        {
            "CODE": "K59T",
            "GROUP": "PART BET",
            "NAME": "BJP-755",
            "DATETIME": "220506111751"
        },
        {
            "CODE": "K59U",
            "GROUP": "PART BET",
            "NAME": "BUG-177",
            "DATETIME": "220506115611"
        },
        {
            "CODE": "K59V",
            "GROUP": "FERREYRO",
            "NAME": "23013",
            "DATETIME": "220506120339"
        },
        {
            "CODE": "K59X",
            "GROUP": "OLATI",
            "NAME": "ANK-740",
            "DATETIME": "220506120233"
        },
        {
            "CODE": "K59Y",
            "GROUP": "T.WEIGHT",
            "NAME": "D3U-886",
            "DATETIME": "220506115438"
        },
        {
            "CODE": "K59Z",
            "GROUP": "PART BET",
            "NAME": "BJT-708",
            "DATETIME": "220506120109"
        },
        {
            "CODE": "K5A0",
            "GROUP": "T.WEIGHT",
            "NAME": "C6F-796",
            "DATETIME": "220506115859"
        },
        {
            "CODE": "K5A3",
            "GROUP": "FAMAI",
            "NAME": "V9W-891",
            "DATETIME": "220506120455"
        },
        {
            "CODE": "K5A4",
            "GROUP": "FERREYRO",
            "NAME": "24003",
            "DATETIME": "220506115806"
        },
        {
            "CODE": "K5A5",
            "GROUP": "PART BET",
            "NAME": "BUV-229",
            "DATETIME": "220506120419"
        },
        {
            "CODE": "K5A7",
            "GROUP": "FERREYRO",
            "NAME": "23010",
            "DATETIME": "220506120347"
        },
        {
            "CODE": "K5AC",
            "GROUP": "SOLHYM",
            "NAME": "ALG-816",
            "DATETIME": "220506115728"
        },
        {
            "CODE": "K5AD",
            "GROUP": "ORBIS",
            "NAME": "F6X-801",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K5AE",
            "GROUP": "POLO",
            "NAME": "B5G-735",
            "DATETIME": "220506120247"
        },
        {
            "CODE": "K5AF",
            "GROUP": "GR2000",
            "NAME": "AFT-934",
            "DATETIME": "220506120504"
        },
        {
            "CODE": "K5AH",
            "GROUP": "LOG.INT",
            "NAME": "C5G-937",
            "DATETIME": "220502093829"
        },
        {
            "CODE": "K5AJ",
            "GROUP": "IÑAKI",
            "NAME": "BVC-300",
            "DATETIME": "220506120357"
        },
        {
            "CODE": "K5AL",
            "GROUP": "SHILCAYO",
            "NAME": "B8G-996",
            "DATETIME": "220506115245"
        },
        {
            "CODE": "K5AN",
            "GROUP": "JOSUF",
            "NAME": "BPG-503",
            "DATETIME": "220506120055"
        },
        {
            "CODE": "K5AO",
            "GROUP": "NEGOCIAR",
            "NAME": "BSC-283",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K5AQ",
            "GROUP": "FERREYRO",
            "NAME": "625186",
            "DATETIME": "220428165426"
        },
        {
            "CODE": "K5AR",
            "GROUP": "PART BET",
            "NAME": "BPA-359",
            "DATETIME": "220506115552"
        },
        {
            "CODE": "K5AS",
            "GROUP": "A&J",
            "NAME": "BND-929",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "K5AU",
            "GROUP": "INTERSEN",
            "NAME": "AUZ-702",
            "DATETIME": "220506120205"
        },
        {
            "CODE": "K5AW",
            "GROUP": "LISTOTAX",
            "NAME": "BYP-098",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "K5AY",
            "GROUP": "T.SANTOS",
            "NAME": "BBU-843",
            "DATETIME": "220506120139"
        },
        {
            "CODE": "K5B4",
            "GROUP": "FERREYRO",
            "NAME": "7630",
            "DATETIME": "220506113623"
        },
        {
            "CODE": "K5B6",
            "GROUP": "FERREYRO",
            "NAME": "7642",
            "DATETIME": "220506120428"
        },
        {
            "CODE": "K5B7",
            "GROUP": "PRUEBASL",
            "NAME": "K5B79999",
            "DATETIME": "220118073646"
        },
        {
            "CODE": "K5B8",
            "GROUP": "POSITIVA",
            "NAME": "AZR-866",
            "DATETIME": "220506115753"
        },
        {
            "CODE": "K5B9",
            "GROUP": "PART BET",
            "NAME": "AXQ-853",
            "DATETIME": "220506084730"
        },
        {
            "CODE": "K5BA",
            "GROUP": "PRUEBASL",
            "NAME": "K5BA9999",
            "DATETIME": "220118065901"
        },
        {
            "CODE": "K5BC",
            "GROUP": "PART BET",
            "NAME": "BTT-695",
            "DATETIME": "220506115258"
        },
        {
            "CODE": "K5BE",
            "GROUP": "ICP",
            "NAME": "401521",
            "DATETIME": "220506115514"
        },
        {
            "CODE": "K5BG",
            "GROUP": "RENTINLE",
            "NAME": "BHB-120",
            "DATETIME": "220506112928"
        },
        {
            "CODE": "K5BH",
            "GROUP": "JHEMSA",
            "NAME": "C4W-726",
            "DATETIME": "220506120101"
        },
        {
            "CODE": "K5BK",
            "GROUP": "INNERGY",
            "NAME": "AHP-869",
            "DATETIME": "220506115627"
        },
        {
            "CODE": "K5BM",
            "GROUP": "PART BET",
            "NAME": "BTC-410",
            "DATETIME": "220506115814"
        },
        {
            "CODE": "K5BO",
            "GROUP": "YURAX",
            "NAME": "BEH-762",
            "DATETIME": "220506120441"
        },
        {
            "CODE": "K5BU",
            "GROUP": "PART BET",
            "NAME": "AJX-317",
            "DATETIME": "220506120514"
        },
        {
            "CODE": "K5BV",
            "GROUP": "PISCIFAC",
            "NAME": "F3L-711",
            "DATETIME": "220506112714"
        },
        {
            "CODE": "K5BZ",
            "GROUP": "RIO NEGR",
            "NAME": "TAL-889",
            "DATETIME": "220506120316"
        },
        {
            "CODE": "K5C0",
            "GROUP": "AGROTECN",
            "NAME": "T0L-875",
            "DATETIME": "220506111040"
        },
        {
            "CODE": "K5C2",
            "GROUP": "PART BET",
            "NAME": "BTN-344",
            "DATETIME": "220506115233"
        },
        {
            "CODE": "K5C3",
            "GROUP": "LISTOTAX",
            "NAME": "BYQ-242",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K5C4",
            "GROUP": "DELTA",
            "NAME": "EXCAVADO",
            "DATETIME": "220506120459"
        },
        {
            "CODE": "K5C6",
            "GROUP": "AGROTECN",
            "NAME": "T2J-909",
            "DATETIME": "220506110735"
        },
        {
            "CODE": "K5C7",
            "GROUP": "PART BET",
            "NAME": "M6V-816",
            "DATETIME": "220506115553"
        },
        {
            "CODE": "K5C9",
            "GROUP": "UÑEGAN",
            "NAME": "V7W-702",
            "DATETIME": "220226115311"
        },
        {
            "CODE": "K5CA",
            "GROUP": "AGROPECU",
            "NAME": "B6M-782",
            "DATETIME": "220506115609"
        },
        {
            "CODE": "K5CB",
            "GROUP": "PART BET",
            "NAME": "16752",
            "DATETIME": "220506115825"
        },
        {
            "CODE": "K5CC",
            "GROUP": "FERREYRO",
            "NAME": "430707",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K5CD",
            "GROUP": "YURAX",
            "NAME": "BHE-880",
            "DATETIME": "220506115427"
        },
        {
            "CODE": "K5CE",
            "GROUP": "PART BET",
            "NAME": "BFW-191",
            "DATETIME": "220506120031"
        },
        {
            "CODE": "K5CG",
            "GROUP": "VIA FOOD",
            "NAME": "APM-762",
            "DATETIME": "220203154442"
        },
        {
            "CODE": "K5CH",
            "GROUP": "INTERSEN",
            "NAME": "C6U-701",
            "DATETIME": "220506053813"
        },
        {
            "CODE": "K5CI",
            "GROUP": "CHANG CO",
            "NAME": "AYF-916",
            "DATETIME": "220506114646"
        },
        {
            "CODE": "K5CJ",
            "GROUP": "SOLHYM",
            "NAME": "BMN-947",
            "DATETIME": "220506120505"
        },
        {
            "CODE": "K5CL",
            "GROUP": "PALACIOS",
            "NAME": "BEL-796",
            "DATETIME": "220506120003"
        },
        {
            "CODE": "K5CP",
            "GROUP": "CHANG CO",
            "NAME": "0593-NA",
            "DATETIME": "220506113024"
        },
        {
            "CODE": "K5CQ",
            "GROUP": "JYSCORP",
            "NAME": "A7V-903",
            "DATETIME": "220505173416"
        },
        {
            "CODE": "K5CT",
            "GROUP": "HOLDING",
            "NAME": "BTA-348",
            "DATETIME": "220506105911"
        },
        {
            "CODE": "K5CW",
            "GROUP": "PART BET",
            "NAME": "BTR-292",
            "DATETIME": "220506115837"
        },
        {
            "CODE": "K5CX",
            "GROUP": "VIA FOOD",
            "NAME": "F9G-748",
            "DATETIME": "220506110422"
        },
        {
            "CODE": "K5CZ",
            "GROUP": "PART BET",
            "NAME": "BTH-530",
            "DATETIME": "220506120345"
        },
        {
            "CODE": "K5D0",
            "GROUP": "PART BET",
            "NAME": "BHE-864",
            "DATETIME": "220506115232"
        },
        {
            "CODE": "K5D5",
            "GROUP": "DIGITAL",
            "NAME": "BFW-719",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "K5D6",
            "GROUP": "LISTOTAX",
            "NAME": "BYN-354",
            "DATETIME": "220506120232"
        },
        {
            "CODE": "K5DB",
            "GROUP": "TRUCKTEA",
            "NAME": "V9U-774",
            "DATETIME": "220506113204"
        },
        {
            "CODE": "K5DF",
            "GROUP": "LISTOTAX",
            "NAME": "BDD-226",
            "DATETIME": "220506120435"
        },
        {
            "CODE": "K5DH",
            "GROUP": "PART BET",
            "NAME": "AUP-690",
            "DATETIME": "220506120053"
        },
        {
            "CODE": "K5DI",
            "GROUP": "PART BET",
            "NAME": "EUF-043",
            "DATETIME": "220506112714"
        },
        {
            "CODE": "K5DK",
            "GROUP": "CONSULT",
            "NAME": "BCA-829",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K5DM",
            "GROUP": "CALEXA",
            "NAME": "ADV-735",
            "DATETIME": "220506114725"
        },
        {
            "CODE": "K5DP",
            "GROUP": "PART BET",
            "NAME": "Y2F-823",
            "DATETIME": "220216142737"
        },
        {
            "CODE": "K5DR",
            "GROUP": "INCHE",
            "NAME": "BHD-172",
            "DATETIME": "220506112608"
        },
        {
            "CODE": "K5DS",
            "GROUP": "TORRES",
            "NAME": "BHH-768",
            "DATETIME": "220506114825"
        },
        {
            "CODE": "K5DT",
            "GROUP": "GRAMA",
            "NAME": "4607-BB",
            "DATETIME": "220506071620"
        },
        {
            "CODE": "K5E0",
            "GROUP": "CHANG CO",
            "NAME": "B1N-415",
            "DATETIME": "220506110729"
        },
        {
            "CODE": "K5E1",
            "GROUP": "PART BET",
            "NAME": "BFU-889",
            "DATETIME": "220506115951"
        },
        {
            "CODE": "K5E2",
            "GROUP": "PART BET",
            "NAME": "BFV-084",
            "DATETIME": "220506120406"
        },
        {
            "CODE": "K5F9",
            "GROUP": "TJOMAX",
            "NAME": "Z2X-814",
            "DATETIME": "220506115458"
        },
        {
            "CODE": "K5FA",
            "GROUP": "REPARTO",
            "NAME": "BHZ-934",
            "DATETIME": "220506120359"
        },
        {
            "CODE": "K5FC",
            "GROUP": "MORAN",
            "NAME": "BAA-826",
            "DATETIME": "220506115508"
        },
        {
            "CODE": "K5FD",
            "GROUP": "MORAN",
            "NAME": "B3P-835",
            "DATETIME": "220506120459"
        },
        {
            "CODE": "K5FF",
            "GROUP": "TJOMAX",
            "NAME": "C7P-745",
            "DATETIME": "220506115857"
        },
        {
            "CODE": "K5FH",
            "GROUP": "PART BET",
            "NAME": "BVP-146",
            "DATETIME": "220506115608"
        },
        {
            "CODE": "K5FI",
            "GROUP": "MORAN",
            "NAME": "ANB-734",
            "DATETIME": "220506120252"
        },
        {
            "CODE": "K5FK",
            "GROUP": "DESTINOE",
            "NAME": "ADS-837",
            "DATETIME": "220506120240"
        },
        {
            "CODE": "K5FM",
            "GROUP": "PART BET",
            "NAME": "226621",
            "DATETIME": "220506120437"
        },
        {
            "CODE": "K5FN",
            "GROUP": "MORAN",
            "NAME": "ANC-816",
            "DATETIME": "220506120458"
        },
        {
            "CODE": "K5FO",
            "GROUP": "MORAN",
            "NAME": "BDZ-762",
            "DATETIME": "220506120510"
        },
        {
            "CODE": "K5FW",
            "GROUP": "E.COMERC",
            "NAME": "F7G-716",
            "DATETIME": "220506120514"
        },
        {
            "CODE": "K5G6",
            "GROUP": "PART BET",
            "NAME": "BVL-023",
            "DATETIME": "220506120054"
        },
        {
            "CODE": "K5G7",
            "GROUP": "SELGAS",
            "NAME": "D9U-982",
            "DATETIME": "220411132236"
        },
        {
            "CODE": "K5GC",
            "GROUP": "IPANAQUE",
            "NAME": "BBK-047",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K5GE",
            "GROUP": "PART BET",
            "NAME": "W4T-098",
            "DATETIME": "220506115910"
        },
        {
            "CODE": "K5GK",
            "GROUP": "PART BET",
            "NAME": "224602",
            "DATETIME": "220506103401"
        },
        {
            "CODE": "K5GQ",
            "GROUP": "PART BET",
            "NAME": "V0X-097",
            "DATETIME": "220506120443"
        },
        {
            "CODE": "K5GT",
            "GROUP": "PART BET",
            "NAME": "F4G-351",
            "DATETIME": "220506115947"
        },
        {
            "CODE": "K5GZ",
            "GROUP": "SMPORRAS",
            "NAME": "A9U-864",
            "DATETIME": "220506115721"
        },
        {
            "CODE": "K5H2",
            "GROUP": "PART BET",
            "NAME": "BHP-347",
            "DATETIME": "220506120517"
        },
        {
            "CODE": "K5H7",
            "GROUP": "S&R",
            "NAME": "AZS-881",
            "DATETIME": "220506120003"
        },
        {
            "CODE": "K5H8",
            "GROUP": "PART BET",
            "NAME": "BVM-544",
            "DATETIME": "220506115414"
        },
        {
            "CODE": "K5H9",
            "GROUP": "PART BET",
            "NAME": "BVQ-233",
            "DATETIME": "220506115623"
        },
        {
            "CODE": "K5HA",
            "GROUP": "PART BET",
            "NAME": "BLK-864",
            "DATETIME": "220506112108"
        },
        {
            "CODE": "K5HB",
            "GROUP": "S&R",
            "NAME": "BES-906",
            "DATETIME": "220506120026"
        },
        {
            "CODE": "K5HC",
            "GROUP": "S&R",
            "NAME": "AZR-930",
            "DATETIME": "220506120229"
        },
        {
            "CODE": "K5HD",
            "GROUP": "S&R",
            "NAME": "ASQ-840",
            "DATETIME": "220506115908"
        },
        {
            "CODE": "K5HE",
            "GROUP": "HUGAMOR",
            "NAME": "BKO-732",
            "DATETIME": "220506115743"
        },
        {
            "CODE": "K5HF",
            "GROUP": "T-PRESTA",
            "NAME": "F9H-312",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K5HH",
            "GROUP": "S$R",
            "NAME": "APH-766",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K5HJ",
            "GROUP": "PART BET",
            "NAME": "BKV-881",
            "DATETIME": "220506115752"
        },
        {
            "CODE": "K5HK",
            "GROUP": "PART BET",
            "NAME": "16661",
            "DATETIME": "220506115820"
        },
        {
            "CODE": "K5HL",
            "GROUP": "S&R",
            "NAME": "APG-707",
            "DATETIME": "220506120402"
        },
        {
            "CODE": "K5HO",
            "GROUP": "S&R",
            "NAME": "BES-893",
            "DATETIME": "220506120435"
        },
        {
            "CODE": "K5HP",
            "GROUP": "T. HILDA",
            "NAME": "D8V-781",
            "DATETIME": "220506115653"
        },
        {
            "CODE": "K5HQ",
            "GROUP": "PART BET",
            "NAME": "BPN-277",
            "DATETIME": "220506115713"
        },
        {
            "CODE": "K5HR",
            "GROUP": "PART BET",
            "NAME": "36722",
            "DATETIME": "220506120005"
        },
        {
            "CODE": "K5HS",
            "GROUP": "PART BET",
            "NAME": "AWT-766",
            "DATETIME": "220506115942"
        },
        {
            "CODE": "K5HT",
            "GROUP": "M&I GLOB",
            "NAME": "AMJ-761",
            "DATETIME": "220506120054"
        },
        {
            "CODE": "K5HU",
            "GROUP": "PAR BET",
            "NAME": "AZB-723",
            "DATETIME": "220506120517"
        },
        {
            "CODE": "K5HV",
            "GROUP": "MALPASO",
            "NAME": "F4O-755",
            "DATETIME": "220506115659"
        },
        {
            "CODE": "K5HX",
            "GROUP": "CEYESA",
            "NAME": "BKR-717",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "K5HZ",
            "GROUP": "T. HILDA",
            "NAME": "AZY-736",
            "DATETIME": "220506120145"
        },
        {
            "CODE": "K5I0",
            "GROUP": "BALTODAN",
            "NAME": "AFM-210",
            "DATETIME": "220506115456"
        },
        {
            "CODE": "K5I1",
            "GROUP": "FCG",
            "NAME": "D0D-932",
            "DATETIME": "220506120513"
        },
        {
            "CODE": "K5I2",
            "GROUP": "SAN BART",
            "NAME": "AYT-864",
            "DATETIME": "220505091904"
        },
        {
            "CODE": "K5I3",
            "GROUP": "PART BET",
            "NAME": "Z6F-562",
            "DATETIME": "220506115336"
        },
        {
            "CODE": "K5I4",
            "GROUP": "MALPASO",
            "NAME": "BAI-598",
            "DATETIME": "220506115747"
        },
        {
            "CODE": "K5I7",
            "GROUP": "TEPECA",
            "NAME": "BKQ-905",
            "DATETIME": "220506115625"
        },
        {
            "CODE": "K5I9",
            "GROUP": "SAGA",
            "NAME": "BLH-826",
            "DATETIME": "220506115613"
        },
        {
            "CODE": "K5IA",
            "GROUP": "GENOA H",
            "NAME": "D3S-112",
            "DATETIME": "220506115846"
        },
        {
            "CODE": "K5IB",
            "GROUP": "PART BET",
            "NAME": "1123",
            "DATETIME": "220506115141"
        },
        {
            "CODE": "K5IC",
            "GROUP": "INTERSEN",
            "NAME": "C7B-763",
            "DATETIME": "220506053239"
        },
        {
            "CODE": "K5IE",
            "GROUP": "TOMACITO",
            "NAME": "Z3Q-846",
            "DATETIME": "220506120501"
        },
        {
            "CODE": "K5IH",
            "GROUP": "S.BARTOL",
            "NAME": "113897",
            "DATETIME": "220506120027"
        },
        {
            "CODE": "K5II",
            "GROUP": "PART BET",
            "NAME": "APY-230",
            "DATETIME": "220506115439"
        },
        {
            "CODE": "K5IJ",
            "GROUP": "S BARTOL",
            "NAME": "95085",
            "DATETIME": "220506120229"
        },
        {
            "CODE": "K5IM",
            "GROUP": "LISTOTAX",
            "NAME": "BYQ-022",
            "DATETIME": "220506115427"
        },
        {
            "CODE": "K5IN",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-503",
            "DATETIME": "220506120429"
        },
        {
            "CODE": "K5IO",
            "GROUP": "YEKARE",
            "NAME": "AZT-769",
            "DATETIME": "220506115657"
        },
        {
            "CODE": "K5IQ",
            "GROUP": "YEKARE",
            "NAME": "D9F-863",
            "DATETIME": "220506120405"
        },
        {
            "CODE": "K5IT",
            "GROUP": "MR EXCAV",
            "NAME": "EXCAVA 5",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K5IU",
            "GROUP": "CAMZA",
            "NAME": "BKR-895",
            "DATETIME": "220504130719"
        },
        {
            "CODE": "K5IW",
            "GROUP": "FVS",
            "NAME": "X3X-846",
            "DATETIME": "220506120036"
        },
        {
            "CODE": "K5IX",
            "GROUP": "DELTA",
            "NAME": "L20B",
            "DATETIME": "220506115756"
        },
        {
            "CODE": "K5IY",
            "GROUP": "CACERES",
            "NAME": "AST-152",
            "DATETIME": "220506115245"
        },
        {
            "CODE": "K5IZ",
            "GROUP": "S&R",
            "NAME": "AZS-742",
            "DATETIME": "220506120238"
        },
        {
            "CODE": "K5J0",
            "GROUP": "PART BET",
            "NAME": "A4W-924",
            "DATETIME": "220506115628"
        },
        {
            "CODE": "K5J1",
            "GROUP": "S&R",
            "NAME": "AKU-936",
            "DATETIME": "220506120422"
        },
        {
            "CODE": "K5J3",
            "GROUP": "T.SANTOS",
            "NAME": "BBU-748",
            "DATETIME": "220506120018"
        },
        {
            "CODE": "K5J4",
            "GROUP": "PART BET",
            "NAME": "APN-640",
            "DATETIME": "220506115346"
        },
        {
            "CODE": "K5J5",
            "GROUP": "LINCUNA",
            "NAME": "AUD-946",
            "DATETIME": "220506120029"
        },
        {
            "CODE": "K5J6",
            "GROUP": "GEMEVA",
            "NAME": "B5T-872",
            "DATETIME": "220506120313"
        },
        {
            "CODE": "K5J8",
            "GROUP": "PART BET",
            "NAME": "X5D-265",
            "DATETIME": "220506115550"
        },
        {
            "CODE": "K5J9",
            "GROUP": "PART BET",
            "NAME": "BVQ-329",
            "DATETIME": "220506120203"
        },
        {
            "CODE": "K5JA",
            "GROUP": "S&R",
            "NAME": "AZX-768",
            "DATETIME": "220506120514"
        },
        {
            "CODE": "K5JB",
            "GROUP": "S&R",
            "NAME": "AFZ-701",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "K5JV",
            "GROUP": "BONALIS",
            "NAME": "B9V-865",
            "DATETIME": "220506115841"
        },
        {
            "CODE": "K5K0",
            "GROUP": "BALTODAN",
            "NAME": "BEV-694",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K5K4",
            "GROUP": "S&R",
            "NAME": "BBU-729",
            "DATETIME": "220506114151"
        },
        {
            "CODE": "K5K5",
            "GROUP": "PART BET",
            "NAME": "BKK-791",
            "DATETIME": "220506120030"
        },
        {
            "CODE": "K5K6",
            "GROUP": "MALPASO",
            "NAME": "BVO-043",
            "DATETIME": "220506120131"
        },
        {
            "CODE": "K5KC",
            "GROUP": "SOLHYM",
            "NAME": "BDS-833",
            "DATETIME": "220506120401"
        },
        {
            "CODE": "K5KF",
            "GROUP": "DATHISA",
            "NAME": "A1C-147",
            "DATETIME": "220506115948"
        },
        {
            "CODE": "K5KG",
            "GROUP": "T. HILDA",
            "NAME": "C4T-855",
            "DATETIME": "220506120256"
        },
        {
            "CODE": "K5KH",
            "GROUP": "SAN BART",
            "NAME": "102731",
            "DATETIME": "220405233015"
        },
        {
            "CODE": "K5KN",
            "GROUP": "YUPUPUPU",
            "NAME": "S1W-937",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "K5KP",
            "GROUP": "THEM",
            "NAME": "T2C-852",
            "DATETIME": "220506120351"
        },
        {
            "CODE": "K5KS",
            "GROUP": "PART BET",
            "NAME": "BCD-730",
            "DATETIME": "220506115555"
        },
        {
            "CODE": "K5KU",
            "GROUP": "KCOMTFIA",
            "NAME": "231525",
            "DATETIME": "220506120249"
        },
        {
            "CODE": "K5KX",
            "GROUP": "T.HILDA",
            "NAME": "BKC-820",
            "DATETIME": "220506120201"
        },
        {
            "CODE": "K5KZ",
            "GROUP": "GONZALES",
            "NAME": "T4K-359",
            "DATETIME": "220506115946"
        },
        {
            "CODE": "K5LK",
            "GROUP": "PART BET",
            "NAME": "BVM-363",
            "DATETIME": "220506115308"
        },
        {
            "CODE": "K5LU",
            "GROUP": "TJOMAX",
            "NAME": "C3U-853",
            "DATETIME": "220506120020"
        },
        {
            "CODE": "K5LV",
            "GROUP": "TRANSGES",
            "NAME": "BKC-922",
            "DATETIME": "220506120333"
        },
        {
            "CODE": "K5LX",
            "GROUP": "PART BET",
            "NAME": "C3I-742",
            "DATETIME": "220506115105"
        },
        {
            "CODE": "K5M2",
            "GROUP": "PART BET",
            "NAME": "VAU-807",
            "DATETIME": "220506115941"
        },
        {
            "CODE": "K5M4",
            "GROUP": "RENTINLE",
            "NAME": "BHA-691",
            "DATETIME": "220506105649"
        },
        {
            "CODE": "K5M5",
            "GROUP": "RENTINLE",
            "NAME": "BHB-528",
            "DATETIME": "220506120012"
        },
        {
            "CODE": "K5M7",
            "GROUP": "FERREYRO",
            "NAME": "21014",
            "DATETIME": "220506115948"
        },
        {
            "CODE": "K5M8",
            "GROUP": "PART BET",
            "NAME": "BSZ-022",
            "DATETIME": "220506115208"
        },
        {
            "CODE": "K5M9",
            "GROUP": "M.INFANT",
            "NAME": "BJB-849",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K5MA",
            "GROUP": "ESCARCEN",
            "NAME": "BTQ-119",
            "DATETIME": "220506120409"
        },
        {
            "CODE": "K5MC",
            "GROUP": "FERREYRO",
            "NAME": "26014",
            "DATETIME": "220315122144"
        },
        {
            "CODE": "K5ME",
            "GROUP": "FERREYRO",
            "NAME": "26021",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K5MF",
            "GROUP": "ING CONT",
            "NAME": "AXA-774",
            "DATETIME": "220506115906"
        },
        {
            "CODE": "K5MG",
            "GROUP": "PART BET",
            "NAME": "EAD-307",
            "DATETIME": "220506115357"
        },
        {
            "CODE": "K5MI",
            "GROUP": "TUV ",
            "NAME": "BJM-767",
            "DATETIME": "220506120235"
        },
        {
            "CODE": "K5MK",
            "GROUP": "INTERSEN",
            "NAME": "C3C-729",
            "DATETIME": "220506104730"
        },
        {
            "CODE": "K5MM",
            "GROUP": "PRUEBASL",
            "NAME": "KONZ9999",
            "DATETIME": "220118085544"
        },
        {
            "CODE": "K5N7",
            "GROUP": "FIMATRAN",
            "NAME": "B0O-749",
            "DATETIME": "220506120417"
        },
        {
            "CODE": "K5N8",
            "GROUP": "TRABAJA",
            "NAME": "EAE-890",
            "DATETIME": "220506114524"
        },
        {
            "CODE": "K5N9",
            "GROUP": "TRABAJA",
            "NAME": "EAE-908",
            "DATETIME": "220506105550"
        },
        {
            "CODE": "K5NA",
            "GROUP": "SALUD",
            "NAME": "BUE-173",
            "DATETIME": "220506120009"
        },
        {
            "CODE": "K5NB",
            "GROUP": "PART BET",
            "NAME": "BLO-438",
            "DATETIME": "220506115758"
        },
        {
            "CODE": "K5NC",
            "GROUP": "TRABAJA",
            "NAME": "EAE-925",
            "DATETIME": "220506120459"
        },
        {
            "CODE": "K5ND",
            "GROUP": "TRABAJA",
            "NAME": "EAE-928",
            "DATETIME": "220506105713"
        },
        {
            "CODE": "K5NF",
            "GROUP": "NEKA",
            "NAME": "BTX-012",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "K5NG",
            "GROUP": "FAMAI",
            "NAME": "V9V-886",
            "DATETIME": "220506115758"
        },
        {
            "CODE": "K5NH",
            "GROUP": "TRABAJA",
            "NAME": "EAE-865",
            "DATETIME": "220506120440"
        },
        {
            "CODE": "K5NI",
            "GROUP": "TRABAJA",
            "NAME": "EAE-866",
            "DATETIME": "220506120149"
        },
        {
            "CODE": "K5NJ",
            "GROUP": "SMIGUELG",
            "NAME": "V9C-733",
            "DATETIME": "220506115658"
        },
        {
            "CODE": "K5NK",
            "GROUP": "SOLTRAK",
            "NAME": "BJG-810",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "K5NL",
            "GROUP": "GILDEMEI",
            "NAME": "BJD-858",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "K5NM",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-233",
            "DATETIME": "220506115541"
        },
        {
            "CODE": "K5NQ",
            "GROUP": "G.ROMERO",
            "NAME": "C0O-735"
        },
        {
            "CODE": "K5NR",
            "GROUP": "INTERSEN",
            "NAME": "AVF-929",
            "DATETIME": "220506115842"
        },
        {
            "CODE": "K5NS",
            "GROUP": "VINELLI",
            "NAME": "V0R-002",
            "DATETIME": "220506105649"
        },
        {
            "CODE": "K5NT",
            "GROUP": "TAXI AH",
            "NAME": "AZY-197",
            "DATETIME": "220506120516"
        },
        {
            "CODE": "K5NU",
            "GROUP": "ARBECO",
            "NAME": "W5X-872",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K5NW",
            "GROUP": "INTERSEN",
            "NAME": "AUZ-722",
            "DATETIME": "220506115653"
        },
        {
            "CODE": "K5NX",
            "GROUP": "PART BET",
            "NAME": "BJO-833",
            "DATETIME": "220506115434"
        },
        {
            "CODE": "K5NZ",
            "GROUP": "MORAN",
            "NAME": "AUB-727",
            "DATETIME": "220506120459"
        },
        {
            "CODE": "K5O0",
            "GROUP": "CARTONES",
            "NAME": "ASQ-852",
            "DATETIME": "220506120359"
        },
        {
            "CODE": "K5O1",
            "GROUP": "INTERSEN",
            "NAME": "AUY-772",
            "DATETIME": "220506120023"
        },
        {
            "CODE": "K5O2",
            "GROUP": "OLIVOS S",
            "NAME": "ARK-943",
            "DATETIME": "220506120207"
        },
        {
            "CODE": "K5O5",
            "GROUP": "OLIVOS S",
            "NAME": "BHT-908",
            "DATETIME": "220506120319"
        },
        {
            "CODE": "K5O6",
            "GROUP": "INTERSEN",
            "NAME": "BPT-453",
            "DATETIME": "220506115742"
        },
        {
            "CODE": "K5O8",
            "GROUP": "MORAN",
            "NAME": "F5B-707",
            "DATETIME": "220506115851"
        },
        {
            "CODE": "K5OA",
            "GROUP": "ARBECO",
            "NAME": "W6M-757",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "K5OD",
            "GROUP": "PART BET",
            "NAME": "BVK-340",
            "DATETIME": "220506120429"
        },
        {
            "CODE": "K5OF",
            "GROUP": "SBN",
            "NAME": "EAE-820",
            "DATETIME": "220506115804"
        },
        {
            "CODE": "K5OG",
            "GROUP": "PART BET",
            "NAME": "BKA-891",
            "DATETIME": "220506115623"
        },
        {
            "CODE": "K5OH",
            "GROUP": "ABAD",
            "NAME": "W2L-977",
            "DATETIME": "220415085253"
        },
        {
            "CODE": "K5OJ",
            "GROUP": "LISTOTAX",
            "NAME": "BTH-610",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K5OK",
            "GROUP": "PART BET",
            "NAME": "226802",
            "DATETIME": "220506115328"
        },
        {
            "CODE": "K5OL",
            "GROUP": "MORAN",
            "NAME": "AZX-925",
            "DATETIME": "220506120024"
        },
        {
            "CODE": "K5OM",
            "GROUP": "MORAN",
            "NAME": "ACZ-718",
            "DATETIME": "220506120103"
        },
        {
            "CODE": "K5ON",
            "GROUP": "V.CASTRO",
            "NAME": "A9R-612",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "K5OO",
            "GROUP": "LINCUNA",
            "NAME": "C7Z-793",
            "DATETIME": "220423191351"
        },
        {
            "CODE": "K5OP",
            "GROUP": "SOLGASTR",
            "NAME": "AWI-972",
            "DATETIME": "220506115225"
        },
        {
            "CODE": "K5OR",
            "GROUP": "HERCON",
            "NAME": "B0M-930",
            "DATETIME": "220506115555"
        },
        {
            "CODE": "K5OS",
            "GROUP": "VIDITEK",
            "NAME": "AFW-845F",
            "DATETIME": "220506115607"
        },
        {
            "CODE": "K5OU",
            "GROUP": "PART BET",
            "NAME": "BDB-487",
            "DATETIME": "220506120117"
        },
        {
            "CODE": "K5OX",
            "GROUP": "PART BET",
            "NAME": "AWJ-336",
            "DATETIME": "220506120058"
        },
        {
            "CODE": "K5OY",
            "GROUP": "ORBIS",
            "NAME": "BJU-837",
            "DATETIME": "220506120453"
        },
        {
            "CODE": "K5OZ",
            "GROUP": "PART BET",
            "NAME": "BEE-697",
            "DATETIME": "220506120458"
        },
        {
            "CODE": "K5P0",
            "GROUP": "BACHET",
            "NAME": "C7F-865",
            "DATETIME": "220506115650"
        },
        {
            "CODE": "K5P1",
            "GROUP": "PORTUARI",
            "NAME": "B2I-865",
            "DATETIME": "220506120231"
        },
        {
            "CODE": "K5P3",
            "GROUP": "PART BET",
            "NAME": "BVL-177",
            "DATETIME": "220506120450"
        },
        {
            "CODE": "K5P4",
            "GROUP": "SOLHYM",
            "NAME": "BFH-938",
            "DATETIME": "220506120113"
        },
        {
            "CODE": "K5P5",
            "GROUP": "PROCARGO",
            "NAME": "AZZ-807",
            "DATETIME": "220506115525"
        },
        {
            "CODE": "K5P6",
            "GROUP": "LUCERO",
            "NAME": "APP-524",
            "DATETIME": "220506120220"
        },
        {
            "CODE": "K5P8",
            "GROUP": "PART BET",
            "NAME": "194592",
            "DATETIME": "220506115558"
        },
        {
            "CODE": "K5P9",
            "GROUP": "PART BET",
            "NAME": "BTY-208",
            "DATETIME": "220506120125"
        },
        {
            "CODE": "K5PA",
            "GROUP": "PART BET",
            "NAME": "BDX-383",
            "DATETIME": "220506115116"
        },
        {
            "CODE": "K5PB",
            "GROUP": "PART BET",
            "NAME": "4880",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "K5PD",
            "GROUP": "PART BET",
            "NAME": "AWP-444",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "K5PF",
            "GROUP": "PART BET",
            "NAME": "BVG-128",
            "DATETIME": "220506115550"
        },
        {
            "CODE": "K5PG",
            "GROUP": "PART BET",
            "NAME": "391404",
            "DATETIME": "220506115416"
        },
        {
            "CODE": "K5PH",
            "GROUP": "S&R",
            "NAME": "BKH-701",
            "DATETIME": "220506120354"
        },
        {
            "CODE": "K5PI",
            "GROUP": "TAFUR",
            "NAME": "BNR-089",
            "DATETIME": "220506120003"
        },
        {
            "CODE": "K5PJ",
            "GROUP": "AYBIMPOR",
            "NAME": "BCE-905",
            "DATETIME": "220506120408"
        },
        {
            "CODE": "K5PK",
            "GROUP": "PART BET",
            "NAME": "ASR-217",
            "DATETIME": "220506115335"
        },
        {
            "CODE": "K5PM",
            "GROUP": "PART BET",
            "NAME": "BVK-163",
            "DATETIME": "220323161104"
        },
        {
            "CODE": "K5PO",
            "GROUP": "PART BET",
            "NAME": "800050",
            "DATETIME": "220506115323"
        },
        {
            "CODE": "K5PP",
            "GROUP": "PART BET",
            "NAME": "BKL-907",
            "DATETIME": "220506115320"
        },
        {
            "CODE": "K5PR",
            "GROUP": "SOLHYM",
            "NAME": "BDC-878",
            "DATETIME": "220506120428"
        },
        {
            "CODE": "K5PS",
            "GROUP": "RPIMPORT",
            "NAME": "BVK-583",
            "DATETIME": "220506120124"
        },
        {
            "CODE": "K5PV",
            "GROUP": "PART BET",
            "NAME": "BSV-393",
            "DATETIME": "220330062256"
        },
        {
            "CODE": "K5PW",
            "GROUP": "TAMBOGRA",
            "NAME": "BBZ-805",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "K5PY",
            "GROUP": "TRUCKTEA",
            "NAME": "V9F-110",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "K5PZ",
            "GROUP": "VIZCARDO",
            "NAME": "VAL-731",
            "DATETIME": "220506120104"
        },
        {
            "CODE": "K5Q1",
            "GROUP": "LOGISTIC",
            "NAME": "BUY-507",
            "DATETIME": "220422195903"
        },
        {
            "CODE": "K5Q2",
            "GROUP": "PART BET",
            "NAME": "VAX-855",
            "DATETIME": "220506072301"
        },
        {
            "CODE": "K5Q4",
            "GROUP": "PART BET",
            "NAME": "433554",
            "DATETIME": "220506115944"
        },
        {
            "CODE": "K5Q6",
            "GROUP": "PART BET",
            "NAME": "C1K-911",
            "DATETIME": "220126110141"
        },
        {
            "CODE": "K5Q7",
            "GROUP": "GOO TRIP",
            "NAME": "VAY-891",
            "DATETIME": "220506081612"
        },
        {
            "CODE": "K5Q8",
            "GROUP": "PART BET",
            "NAME": "X4Z-749",
            "DATETIME": "220506115824"
        },
        {
            "CODE": "K5Q9",
            "GROUP": "GOO TRIP",
            "NAME": "VAY-884",
            "DATETIME": "220506114221"
        },
        {
            "CODE": "K5QA",
            "GROUP": "PACORIFU",
            "NAME": "6049",
            "DATETIME": "220403101031"
        },
        {
            "CODE": "K5QB",
            "GROUP": "TRUCKTEA",
            "NAME": "V9T-733",
            "DATETIME": "220506115715"
        },
        {
            "CODE": "K5QD",
            "GROUP": "LOGISTIC",
            "NAME": "BVA-378",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "K5QE",
            "GROUP": "PART BET",
            "NAME": "VAV-844",
            "DATETIME": "220506090158"
        },
        {
            "CODE": "K5QF",
            "GROUP": "SBN",
            "NAME": "EAD-502",
            "DATETIME": "220506120330"
        },
        {
            "CODE": "K5QG",
            "GROUP": "MORAN",
            "NAME": "F4F-891",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "K5QH",
            "GROUP": "ARZOBISP",
            "NAME": "C7J-933",
            "DATETIME": "220506120238"
        },
        {
            "CODE": "K5QI",
            "GROUP": "PART BET",
            "NAME": "BPR-639",
            "DATETIME": "220506115113"
        },
        {
            "CODE": "K5QJ",
            "GROUP": "V&N",
            "NAME": "BJS-840",
            "DATETIME": "220506120520"
        },
        {
            "CODE": "K5QK",
            "GROUP": "MONTERRE",
            "NAME": "BKN-933",
            "DATETIME": "220506115644"
        },
        {
            "CODE": "K5QL",
            "GROUP": "PART BET",
            "NAME": "Z6E-500",
            "DATETIME": "220506115231"
        },
        {
            "CODE": "K5QM",
            "GROUP": "DATHISA",
            "NAME": "BVN-572",
            "DATETIME": "220506120517"
        },
        {
            "CODE": "K5QN",
            "GROUP": "MORAN",
            "NAME": "BDY-947",
            "DATETIME": "220506115737"
        },
        {
            "CODE": "K5QP",
            "GROUP": "LINCUNA",
            "NAME": "A6N-800",
            "DATETIME": "220310131347"
        },
        {
            "CODE": "K5QQ",
            "GROUP": "I.VILCA",
            "NAME": "BKE-923",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "K5QR",
            "GROUP": "LABTRONI",
            "NAME": "BKK-918",
            "DATETIME": "220506115553"
        },
        {
            "CODE": "K5QS",
            "GROUP": "GILDEMEI",
            "NAME": "AUM-564",
            "DATETIME": "220506115225"
        },
        {
            "CODE": "K5QT",
            "GROUP": "MORAN",
            "NAME": "C7L-727",
            "DATETIME": "220506120440"
        },
        {
            "CODE": "K5QU",
            "GROUP": "PART BET",
            "NAME": "BVN-537",
            "DATETIME": "220506115223"
        },
        {
            "CODE": "K5QV",
            "GROUP": "PART BET",
            "NAME": "BNM-697",
            "DATETIME": "220506120026"
        },
        {
            "CODE": "K5QX",
            "GROUP": "PROCARGO",
            "NAME": "C1O-901",
            "DATETIME": "220506115742"
        },
        {
            "CODE": "K5QY",
            "GROUP": "INTERSEN",
            "NAME": "AYZ-737",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K5QZ",
            "GROUP": "CHAMORRO",
            "NAME": "BUU-209",
            "DATETIME": "220506115806"
        },
        {
            "CODE": "K5R0",
            "GROUP": "INTERSEN",
            "NAME": "AUY-816",
            "DATETIME": "220506120443"
        },
        {
            "CODE": "K5R1",
            "GROUP": "PART BET",
            "NAME": "BDB-401",
            "DATETIME": "220506115520"
        },
        {
            "CODE": "K5R2",
            "GROUP": "MANDUJAN",
            "NAME": "B7F-895",
            "DATETIME": "220506120338"
        },
        {
            "CODE": "K5R3",
            "GROUP": "OSEX",
            "NAME": "D3P-804",
            "DATETIME": "220506115920"
        },
        {
            "CODE": "K5R5",
            "GROUP": "WIRACOCH",
            "NAME": "TAI-916",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "K5R7",
            "GROUP": "L & M",
            "NAME": "D9W-810",
            "DATETIME": "220506115730"
        },
        {
            "CODE": "K5R8",
            "GROUP": "UVICA",
            "NAME": "BJI-817",
            "DATETIME": "220506120006"
        },
        {
            "CODE": "K5R9",
            "GROUP": "PART BET",
            "NAME": "BUU-520",
            "DATETIME": "220506115433"
        },
        {
            "CODE": "K5RB",
            "GROUP": "PART BET",
            "NAME": "BJO-774",
            "DATETIME": "220506115844"
        },
        {
            "CODE": "K5RC",
            "GROUP": "PART BET",
            "NAME": "BHO-889",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "K5RD",
            "GROUP": "PART BET",
            "NAME": "BTD-426",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "K5RE",
            "GROUP": "PART BET",
            "NAME": "7000015",
            "DATETIME": "220506120007"
        },
        {
            "CODE": "K5RF",
            "GROUP": "PART BET",
            "NAME": "ARU-001",
            "DATETIME": "220506115457"
        },
        {
            "CODE": "K5RG",
            "GROUP": "PART BET",
            "NAME": "BUX-297",
            "DATETIME": "220506115214"
        },
        {
            "CODE": "K5RH",
            "GROUP": "GR2000",
            "NAME": "F5R-097",
            "DATETIME": "220506115809"
        },
        {
            "CODE": "K5RI",
            "GROUP": "PROCARGO",
            "NAME": "D2V-790",
            "DATETIME": "220506115839"
        },
        {
            "CODE": "K5RJ",
            "GROUP": "PART BET",
            "NAME": "BUR-499",
            "DATETIME": "220506115440"
        },
        {
            "CODE": "K5RL",
            "GROUP": "T. LUCKY",
            "NAME": "AYR-733",
            "DATETIME": "220506115716"
        },
        {
            "CODE": "K5RM",
            "GROUP": "INTERSEN",
            "NAME": "AUZ-767",
            "DATETIME": "220506120226"
        },
        {
            "CODE": "K5RN",
            "GROUP": "INTERSEN",
            "NAME": "AYZ-736",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K5RO",
            "GROUP": "LG Y G",
            "NAME": "W6Q-889",
            "DATETIME": "220506115741"
        },
        {
            "CODE": "K5RP",
            "GROUP": "SAN BART",
            "NAME": "101704",
            "DATETIME": "220506120218"
        },
        {
            "CODE": "K5RQ",
            "GROUP": "OLPE",
            "NAME": "C1B-721",
            "DATETIME": "220506115810"
        },
        {
            "CODE": "K5RS",
            "GROUP": "T. LUCKY",
            "NAME": "D2D-705",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "K5RU",
            "GROUP": "PART BET",
            "NAME": "500362",
            "DATETIME": "220506115621"
        },
        {
            "CODE": "K5RV",
            "GROUP": "OLPE",
            "NAME": "B4V-803",
            "DATETIME": "220506115850"
        },
        {
            "CODE": "K5RW",
            "GROUP": "PART BET",
            "NAME": "ANR-907",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "K5RX",
            "GROUP": "ING PROY",
            "NAME": "BJT-948",
            "DATETIME": "220506120255"
        },
        {
            "CODE": "K5RY",
            "GROUP": "PART BET",
            "NAME": "BFU-148",
            "DATETIME": "220506120208"
        },
        {
            "CODE": "K5RZ",
            "GROUP": "PART BET",
            "NAME": "BUY-420",
            "DATETIME": "220506115144"
        },
        {
            "CODE": "K5S0",
            "GROUP": "PART BET",
            "NAME": "BBO-612",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "K5S1",
            "GROUP": "A&S CORP",
            "NAME": "AVV-886",
            "DATETIME": "220506120321"
        },
        {
            "CODE": "K5S2",
            "GROUP": "INTERSEN",
            "NAME": "AYZ-860",
            "DATETIME": "220506120513"
        },
        {
            "CODE": "K5S3",
            "GROUP": "PART BET",
            "NAME": "BMQ-703",
            "DATETIME": "220506115633"
        },
        {
            "CODE": "K5S4",
            "GROUP": "ARBECO",
            "NAME": "AMY-901",
            "DATETIME": "220506120449"
        },
        {
            "CODE": "K5S5",
            "GROUP": "TRAN GLP",
            "NAME": "B6Z-744",
            "DATETIME": "220318181102"
        },
        {
            "CODE": "K5S6",
            "GROUP": "I.MEDALY",
            "NAME": "W6S-806",
            "DATETIME": "220506120100"
        },
        {
            "CODE": "K5S7",
            "GROUP": "SALOMON",
            "NAME": "VAT-877",
            "DATETIME": "220506115003"
        },
        {
            "CODE": "K5S8",
            "GROUP": "OLPE",
            "NAME": "D5K-881",
            "DATETIME": "220506115615"
        },
        {
            "CODE": "K5S9",
            "GROUP": "LINCUNA",
            "NAME": "214442",
            "DATETIME": "220506115455"
        },
        {
            "CODE": "K5SA",
            "GROUP": "PART BET",
            "NAME": "BUX-251",
            "DATETIME": "220506115728"
        },
        {
            "CODE": "K5SB",
            "GROUP": "INTERSEN",
            "NAME": "AZA-759",
            "DATETIME": "220506115550"
        },
        {
            "CODE": "K5SC",
            "GROUP": "INTERSEN",
            "NAME": "AYZ-785",
            "DATETIME": "220506110149"
        },
        {
            "CODE": "K5SD",
            "GROUP": "INTERSEN",
            "NAME": "AYV-747",
            "DATETIME": "220506120420"
        },
        {
            "CODE": "K5SE",
            "GROUP": "I.MEDALY",
            "NAME": "W4S-676",
            "DATETIME": "220506103503"
        },
        {
            "CODE": "K5SF",
            "GROUP": "PART BET",
            "NAME": "V8R-152",
            "DATETIME": "220506120455"
        },
        {
            "CODE": "K5SG",
            "GROUP": "INTERSEN",
            "NAME": "AYZ-879",
            "DATETIME": "220506111817"
        },
        {
            "CODE": "K5SH",
            "GROUP": "SUEROS",
            "NAME": "V8M-825",
            "DATETIME": "220506120006"
        },
        {
            "CODE": "K5SI",
            "GROUP": "PART BET",
            "NAME": "ERI-006",
            "DATETIME": "220506115249"
        },
        {
            "CODE": "K5SJ",
            "GROUP": "PART BET",
            "NAME": "V0X-679",
            "DATETIME": "220506115149"
        },
        {
            "CODE": "K5SK",
            "GROUP": "SOLHYM",
            "NAME": "AUP-731",
            "DATETIME": "220506120411"
        },
        {
            "CODE": "K5SL",
            "GROUP": "GR2000",
            "NAME": "AMS-766",
            "DATETIME": "220506115549"
        },
        {
            "CODE": "K5SM",
            "GROUP": "SOLHYM",
            "NAME": "ANW-919",
            "DATETIME": "220506115055"
        },
        {
            "CODE": "K5SN",
            "GROUP": "PART BET",
            "NAME": "825827",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K5SO",
            "GROUP": "PART BET",
            "NAME": "BUU-405",
            "DATETIME": "220506115620"
        },
        {
            "CODE": "K5SP",
            "GROUP": "PART BET",
            "NAME": "ERP-244",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K5SQ",
            "GROUP": "PART BET",
            "NAME": "BJX-690",
            "DATETIME": "220506120007"
        },
        {
            "CODE": "K5SR",
            "GROUP": "PART BET",
            "NAME": "BUO-406",
            "DATETIME": "220506120029"
        },
        {
            "CODE": "K5SS",
            "GROUP": "PART BET",
            "NAME": "BJS-738",
            "DATETIME": "220506120015"
        },
        {
            "CODE": "K5ST",
            "GROUP": "PRO NATU",
            "NAME": "87017",
            "DATETIME": "220506082604"
        },
        {
            "CODE": "K5SU",
            "GROUP": "TRANSITA",
            "NAME": "BJP-704",
            "DATETIME": "220506115559"
        },
        {
            "CODE": "K5SV",
            "GROUP": "MAINQUI",
            "NAME": "BKA-799",
            "DATETIME": "220506115841"
        },
        {
            "CODE": "K5SW",
            "GROUP": "PART BET",
            "NAME": "804163",
            "DATETIME": "220119140302"
        },
        {
            "CODE": "K5SX",
            "GROUP": "MAININ",
            "NAME": "BDM-754",
            "DATETIME": "220506115845"
        },
        {
            "CODE": "K5SY",
            "GROUP": "HUASCAR",
            "NAME": "AFB-937",
            "DATETIME": "220506120409"
        },
        {
            "CODE": "K5T0",
            "GROUP": "ARBECO",
            "NAME": "W6M-758",
            "DATETIME": "220506120511"
        },
        {
            "CODE": "K5T1",
            "GROUP": "SOLTRAK",
            "NAME": "C8R-963",
            "DATETIME": "220506115843"
        },
        {
            "CODE": "K5T2",
            "GROUP": "GR2000",
            "NAME": "AJB-259",
            "DATETIME": "220506120426"
        },
        {
            "CODE": "K5T3",
            "GROUP": "PART BET",
            "NAME": "BTS-111",
            "DATETIME": "220506115236"
        },
        {
            "CODE": "K5T4",
            "GROUP": "HUAPAYA",
            "NAME": "BTT-189",
            "DATETIME": "220506113716"
        },
        {
            "CODE": "K5T5",
            "GROUP": "SBN",
            "NAME": "EGX-776",
            "DATETIME": "220506120410"
        },
        {
            "CODE": "K5T6",
            "GROUP": "SBN",
            "NAME": "EGQ-617",
            "DATETIME": "220506115946"
        },
        {
            "CODE": "K5T7",
            "GROUP": "MR EXCAV",
            "NAME": "EXCAVA 3",
            "DATETIME": "220506113704"
        },
        {
            "CODE": "K5T8",
            "GROUP": "SBN",
            "NAME": "EAD-483",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "K5T9",
            "GROUP": "SBN",
            "NAME": "EGV-584",
            "DATETIME": "220331162124"
        },
        {
            "CODE": "K5TA",
            "GROUP": "PART BET",
            "NAME": "BSW-247",
            "DATETIME": "220506115925"
        },
        {
            "CODE": "K5TB",
            "GROUP": "PART BET",
            "NAME": "BKQ-838",
            "DATETIME": "220505164756"
        },
        {
            "CODE": "K5TD",
            "GROUP": "DELTA",
            "NAME": "C8Z-704",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "K5TE",
            "GROUP": "PLASTISE",
            "NAME": "TAO-894",
            "DATETIME": "220506115953"
        },
        {
            "CODE": "K5TF",
            "GROUP": "SBN",
            "NAME": "EGX-782",
            "DATETIME": "220506120213"
        },
        {
            "CODE": "K5TG",
            "GROUP": "POSITIVA",
            "NAME": "S1X-930",
            "DATETIME": "220506120502"
        },
        {
            "CODE": "K5TH",
            "GROUP": "PART BET",
            "NAME": "A5P-902",
            "DATETIME": "220506120102"
        },
        {
            "CODE": "K5TI",
            "GROUP": "SBN",
            "NAME": "EAD-433",
            "DATETIME": "220506115741"
        },
        {
            "CODE": "K5TK",
            "GROUP": "MR EXCAV",
            "NAME": "EXCAVA 1",
            "DATETIME": "220506120337"
        },
        {
            "CODE": "K5TL",
            "GROUP": "SBN",
            "NAME": "EAD-501",
            "DATETIME": "220506115518"
        },
        {
            "CODE": "K5TN",
            "GROUP": "MR EXCAV",
            "NAME": "EXCAVA 2",
            "DATETIME": "220506120455"
        },
        {
            "CODE": "K5TO",
            "GROUP": "MR EXCAV",
            "NAME": "EXCAVA 4",
            "DATETIME": "220314161635"
        },
        {
            "CODE": "K5TP",
            "GROUP": "PART BET",
            "NAME": "BVG-045",
            "DATETIME": "220506120417"
        },
        {
            "CODE": "K5TQ",
            "GROUP": "PART BET",
            "NAME": "BAS-080",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K5TR",
            "GROUP": "TRABAJA",
            "NAME": "EAE-919",
            "DATETIME": "220506120100"
        },
        {
            "CODE": "K5TS",
            "GROUP": "PART BET",
            "NAME": "BJC-656",
            "DATETIME": "220506120425"
        },
        {
            "CODE": "K5TT",
            "GROUP": "MALDONAD",
            "NAME": "BTU-414",
            "DATETIME": "220312114119"
        },
        {
            "CODE": "K5TU",
            "GROUP": "TRABAJA",
            "NAME": "EAE-907",
            "DATETIME": "220506111045"
        },
        {
            "CODE": "K5TV",
            "GROUP": "TRABAJA",
            "NAME": "EAE-869",
            "DATETIME": "220427105625"
        },
        {
            "CODE": "K5TW",
            "GROUP": "TRABAJA",
            "NAME": "EAE-878",
            "DATETIME": "220506120317"
        },
        {
            "CODE": "K5TX",
            "GROUP": "S.BARTOL",
            "NAME": "825281",
            "DATETIME": "220506120110"
        },
        {
            "CODE": "K5TZ",
            "GROUP": "S&R",
            "NAME": "B3C-807",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "K5U0",
            "GROUP": "PART BET",
            "NAME": "BUN-622",
            "DATETIME": "220506115045"
        },
        {
            "CODE": "K5U3",
            "GROUP": "PART BET",
            "NAME": "BJN-785",
            "DATETIME": "220506115256"
        },
        {
            "CODE": "K5U4",
            "GROUP": "POSITIVA",
            "NAME": "AUF-430",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "K5U5",
            "GROUP": "PART BET",
            "NAME": "BLZ-227",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "K5U7",
            "GROUP": "S&R",
            "NAME": "AWH-885",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K5U8",
            "GROUP": "V&S CONS",
            "NAME": "Y2C-897",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "K5UB",
            "GROUP": "T.WEIGHT",
            "NAME": "BKR-077",
            "DATETIME": "220506120438"
        },
        {
            "CODE": "K5UC",
            "GROUP": "TRADESUR",
            "NAME": "BJM-802",
            "DATETIME": "220506120504"
        },
        {
            "CODE": "K5UD",
            "GROUP": "SOBERON",
            "NAME": "BBR-816",
            "DATETIME": "220506114330"
        },
        {
            "CODE": "K5UF",
            "GROUP": "PART BET",
            "NAME": "ASO-831",
            "DATETIME": "220506115922"
        },
        {
            "CODE": "K5UG",
            "GROUP": "PART BET",
            "NAME": "BKS-884",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "K5UH",
            "GROUP": "CASTRO",
            "NAME": "BSJ-126",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "K5UI",
            "GROUP": "PART BET",
            "NAME": "801634",
            "DATETIME": "220506115502"
        },
        {
            "CODE": "K5UJ",
            "GROUP": "PART BET",
            "NAME": "BNC-432",
            "DATETIME": "220504191908"
        },
        {
            "CODE": "K5UK",
            "GROUP": "COPERO",
            "NAME": "C2Q-874",
            "DATETIME": "220506061513"
        },
        {
            "CODE": "K5UL",
            "GROUP": "LINCUNA",
            "NAME": "95337",
            "DATETIME": "220311112946"
        },
        {
            "CODE": "K5UO",
            "GROUP": "TAMBOGRA",
            "NAME": "BBW-725",
            "DATETIME": "220506095731"
        },
        {
            "CODE": "K5UP",
            "GROUP": "PORTUARI",
            "NAME": "B0K-858",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "K5UQ",
            "GROUP": "SOBERON",
            "NAME": "F3F-059",
            "DATETIME": "220506113520"
        },
        {
            "CODE": "K5UR",
            "GROUP": "PART BET",
            "NAME": "BUP-480",
            "DATETIME": "220506115520"
        },
        {
            "CODE": "K5US",
            "GROUP": "TAMBOGRA",
            "NAME": "BBX-721",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "K5UU",
            "GROUP": "MBA",
            "NAME": "C6K-704",
            "DATETIME": "220506115605"
        },
        {
            "CODE": "K5UV",
            "GROUP": "PART BET",
            "NAME": "BTS-228",
            "DATETIME": "220506080514"
        },
        {
            "CODE": "K5UW",
            "GROUP": "ARBECO",
            "NAME": "W5X-871",
            "DATETIME": "220506112249"
        },
        {
            "CODE": "K5UX",
            "GROUP": "TAMBOGRA",
            "NAME": "BBW-853",
            "DATETIME": "220502162316"
        },
        {
            "CODE": "K5UY",
            "GROUP": "CHAMBI",
            "NAME": "50510002",
            "DATETIME": "220506120458"
        },
        {
            "CODE": "K5UZ",
            "GROUP": "LEON",
            "NAME": "BSD-097",
            "DATETIME": "220506110759"
        },
        {
            "CODE": "K5V0",
            "GROUP": "ICP",
            "NAME": "AXQ-829",
            "DATETIME": "220506115424"
        },
        {
            "CODE": "K5V2",
            "GROUP": "PART BET",
            "NAME": "BJH-871",
            "DATETIME": "220506104827"
        },
        {
            "CODE": "K5V3",
            "GROUP": "PART BET",
            "NAME": "Z5Y-117",
            "DATETIME": "220506115602"
        },
        {
            "CODE": "K5V4",
            "GROUP": "JDM",
            "NAME": "VAP-766",
            "DATETIME": "220506115720"
        },
        {
            "CODE": "K5V5",
            "GROUP": "INTERSEN",
            "NAME": "C4V-712",
            "DATETIME": "220504174801"
        },
        {
            "CODE": "K5V6",
            "GROUP": "PART BET",
            "NAME": "BUD-242",
            "DATETIME": "220506115909"
        },
        {
            "CODE": "K5V7",
            "GROUP": "ARBECO",
            "NAME": "ANG-789",
            "DATETIME": "220506115752"
        },
        {
            "CODE": "K5V8",
            "GROUP": "PART BET",
            "NAME": "TAT-934",
            "DATETIME": "220506055711"
        },
        {
            "CODE": "K5VA",
            "GROUP": "CORREX",
            "NAME": "BHE-902",
            "DATETIME": "220506120339"
        },
        {
            "CODE": "K5VB",
            "GROUP": "PART-BET",
            "NAME": "BPH-183",
            "DATETIME": "220503111955"
        },
        {
            "CODE": "K5VC",
            "GROUP": "TAFUR",
            "NAME": "AZV-516",
            "DATETIME": "220506120354"
        },
        {
            "CODE": "K5VD",
            "GROUP": "JDM",
            "NAME": "VAP-826",
            "DATETIME": "220506114657"
        },
        {
            "CODE": "K5VF",
            "GROUP": "PART BET",
            "NAME": "BRW-542",
            "DATETIME": "220506115605"
        },
        {
            "CODE": "K5VJ",
            "GROUP": "SAMAIVAN",
            "NAME": "D3R-491",
            "DATETIME": "220506115534"
        },
        {
            "CODE": "K5VL",
            "GROUP": "SAMAIVAN",
            "NAME": "A8S-837",
            "DATETIME": "220506115700"
        },
        {
            "CODE": "K5VM",
            "GROUP": "TAMBOGRA",
            "NAME": "BCA-776",
            "DATETIME": "220505022829"
        },
        {
            "CODE": "K5VO",
            "GROUP": "TAMBOGRA",
            "NAME": "AYI-753",
            "DATETIME": "220328151531"
        },
        {
            "CODE": "K5VP",
            "GROUP": "CARTONES",
            "NAME": "BHE-783",
            "DATETIME": "220506120401"
        },
        {
            "CODE": "K5VQ",
            "GROUP": "AZEDO",
            "NAME": "P2Y-500",
            "DATETIME": "220506115546"
        },
        {
            "CODE": "K5VR",
            "GROUP": "TAMBOGRA",
            "NAME": "BBO-925",
            "DATETIME": "220506120022"
        },
        {
            "CODE": "K5VT",
            "GROUP": "SAMAIVAN",
            "NAME": "C6W-903",
            "DATETIME": "220506115856"
        },
        {
            "CODE": "K5VU",
            "GROUP": "SAMAIVAN",
            "NAME": "ALW-722",
            "DATETIME": "220506115529"
        },
        {
            "CODE": "K5VW",
            "GROUP": "PART BET",
            "NAME": "V0S-271",
            "DATETIME": "220506115039"
        },
        {
            "CODE": "K5VY",
            "GROUP": "DOORS",
            "NAME": "BUT-359",
            "DATETIME": "220502120027"
        },
        {
            "CODE": "K5W0",
            "GROUP": "PART BET",
            "NAME": "BPK-062",
            "DATETIME": "220506115818"
        },
        {
            "CODE": "K5W2",
            "GROUP": "SOLHYM",
            "NAME": "C1Z-770",
            "DATETIME": "220506075633"
        },
        {
            "CODE": "K5W3",
            "GROUP": "FERREYRO",
            "NAME": "23011",
            "DATETIME": "220506115911"
        },
        {
            "CODE": "K5W5",
            "GROUP": "PART BET",
            "NAME": "ASM-658",
            "DATETIME": "220506115948"
        },
        {
            "CODE": "K5W6",
            "GROUP": "CABALLER",
            "NAME": "T5N-061",
            "DATETIME": "220506115704"
        },
        {
            "CODE": "K5W7",
            "GROUP": "GRAMA",
            "NAME": "0439-JB",
            "DATETIME": "220506115140"
        },
        {
            "CODE": "K5W8",
            "GROUP": "LINCUNA",
            "NAME": "BAZ-786",
            "DATETIME": "220506072924"
        },
        {
            "CODE": "K5W9",
            "GROUP": "DATHISA",
            "NAME": "BNI-074",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "K5WB",
            "GROUP": "FERREYRO",
            "NAME": "21009",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "K5WC",
            "GROUP": "TRADESUR",
            "NAME": "BJM-763",
            "DATETIME": "220506120121"
        },
        {
            "CODE": "K5WD",
            "GROUP": "GRAMA",
            "NAME": "1613-JB",
            "DATETIME": "220421180014"
        },
        {
            "CODE": "K5WE",
            "GROUP": "ARBECO",
            "NAME": "W5H-709",
            "DATETIME": "220418142812"
        },
        {
            "CODE": "K5WF",
            "GROUP": "INTERSEN",
            "NAME": "AUY-858",
            "DATETIME": "220506120259"
        },
        {
            "CODE": "K5WG",
            "GROUP": "INTERSEN",
            "NAME": "AUX-920",
            "DATETIME": "220506115729"
        },
        {
            "CODE": "K5WI",
            "GROUP": "INTERSEN",
            "NAME": "AUY-853",
            "DATETIME": "220506120212"
        },
        {
            "CODE": "K5WJ",
            "GROUP": "PART BET",
            "NAME": "BUF-046",
            "DATETIME": "220506115735"
        },
        {
            "CODE": "K5WL",
            "GROUP": "PART BET",
            "NAME": "BUE-392",
            "DATETIME": "220506120048"
        },
        {
            "CODE": "K5WM",
            "GROUP": "SOLTRAK",
            "NAME": "BJG-843",
            "DATETIME": "220129102312"
        },
        {
            "CODE": "K5WN",
            "GROUP": "INTERSEN",
            "NAME": "AUY-876",
            "DATETIME": "220506120058"
        },
        {
            "CODE": "K5WQ",
            "GROUP": "CARTONES",
            "NAME": "BFG-926",
            "DATETIME": "220506115737"
        },
        {
            "CODE": "K5WT",
            "GROUP": "INTERSEN",
            "NAME": "AWB-749",
            "DATETIME": "220506115911"
        },
        {
            "CODE": "K5WV",
            "GROUP": "CARTONES",
            "NAME": "BFD-842",
            "DATETIME": "220506115745"
        },
        {
            "CODE": "K5WZ",
            "GROUP": "PART BET",
            "NAME": "BKN-757",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "K5X0",
            "GROUP": "ALFRANSA",
            "NAME": "C5L-734",
            "DATETIME": "220506115707"
        },
        {
            "CODE": "K5X1",
            "GROUP": "TRUCKTEA",
            "NAME": "V9S-938",
            "DATETIME": "220506065614"
        },
        {
            "CODE": "K5X6",
            "GROUP": "GILDEMEI",
            "NAME": "ARB-943",
            "DATETIME": "220506115200"
        },
        {
            "CODE": "K5XA",
            "GROUP": "LINCUNA",
            "NAME": "BLB-900",
            "DATETIME": "220506120049"
        },
        {
            "CODE": "K5XE",
            "GROUP": "SAG.",
            "NAME": "ASZ-777",
            "DATETIME": "220216172812"
        },
        {
            "CODE": "K5XF",
            "GROUP": "FERTILIZ",
            "NAME": "P4J-784",
            "DATETIME": "220506115640"
        },
        {
            "CODE": "K5XG",
            "GROUP": "SALOMON",
            "NAME": "VAS-850",
            "DATETIME": "220506115040"
        },
        {
            "CODE": "K5XH",
            "GROUP": "CORP AME",
            "NAME": "F4Z-734",
            "DATETIME": "220506120437"
        },
        {
            "CODE": "K5XI",
            "GROUP": "PART BET",
            "NAME": "BTN-164",
            "DATETIME": "220506120050"
        },
        {
            "CODE": "KMKL",
            "GROUP": "INTERSEN",
            "NAME": "AUT-741",
            "DATETIME": "220506112015"
        },
        {
            "CODE": "KMKN",
            "GROUP": "INTERSEN",
            "NAME": "AUT-740",
            "DATETIME": "220506115055"
        },
        {
            "CODE": "KN0Z",
            "GROUP": "LOAYZA",
            "NAME": "ACT-105",
            "DATETIME": "220506114012"
        },
        {
            "CODE": "KN1Z",
            "GROUP": "PART BET",
            "NAME": "BDN-292",
            "DATETIME": "220506120159"
        },
        {
            "CODE": "KN26",
            "GROUP": "SVS TRAN",
            "NAME": "BLR-902",
            "DATETIME": "220506093546"
        },
        {
            "CODE": "KN2H",
            "GROUP": "SINCONVE",
            "NAME": "BCH-860",
            "DATETIME": "220506113242"
        },
        {
            "CODE": "KN2J",
            "GROUP": "POSITIVA",
            "NAME": "BCU-017",
            "DATETIME": "220504092314"
        },
        {
            "CODE": "KN30",
            "GROUP": "TDP CORP",
            "NAME": "ABW-921",
            "DATETIME": "220506113043"
        },
        {
            "CODE": "KN31",
            "GROUP": "INVER 57",
            "NAME": "BBY-890",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "KN32",
            "GROUP": "TRADESUR",
            "NAME": "AXK-831",
            "DATETIME": "220506120225"
        },
        {
            "CODE": "KN3M",
            "GROUP": "PRUEBASL",
            "NAME": "KN3M9999",
            "DATETIME": "220118052146"
        },
        {
            "CODE": "KN3O",
            "GROUP": "LAUVIDAL",
            "NAME": "BFG-714",
            "DATETIME": "220506120458"
        },
        {
            "CODE": "KN3P",
            "GROUP": "LAUVIDAL",
            "NAME": "BFQ-830",
            "DATETIME": "220506120516"
        },
        {
            "CODE": "KN3R",
            "GROUP": "SVS TRAN",
            "NAME": "V4R-760",
            "DATETIME": "220506113402"
        },
        {
            "CODE": "KN3W",
            "GROUP": "PRUEBASL",
            "NAME": "KN3W9999",
            "DATETIME": "220118082132"
        },
        {
            "CODE": "KN43",
            "GROUP": "DATHISA",
            "NAME": "BMG-833",
            "DATETIME": "220506120138"
        },
        {
            "CODE": "KN47",
            "GROUP": "PART BET",
            "NAME": "BRY-352",
            "DATETIME": "220506115700"
        },
        {
            "CODE": "KN48",
            "GROUP": "FAMAI",
            "NAME": "V0P-918",
            "DATETIME": "220506115349"
        },
        {
            "CODE": "KN49",
            "GROUP": "ASEGURAD",
            "NAME": "Y2E-923",
            "DATETIME": "220506113245"
        },
        {
            "CODE": "KN4B",
            "GROUP": "LISTO",
            "NAME": "BXZ-598",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "KN4C",
            "GROUP": "CEYESA",
            "NAME": "BAB-764",
            "DATETIME": "220506114601"
        },
        {
            "CODE": "KN4G",
            "GROUP": "POSITIVA",
            "NAME": "AXO-776",
            "DATETIME": "220506113301"
        },
        {
            "CODE": "KN4I",
            "GROUP": "PART BET",
            "NAME": "BCO-805",
            "DATETIME": "220506115716"
        },
        {
            "CODE": "KN4K",
            "GROUP": "YCHACOND",
            "NAME": "6067",
            "DATETIME": "220506115433"
        },
        {
            "CODE": "KN4O",
            "GROUP": "FERREYRO",
            "NAME": "254064",
            "DATETIME": "220506114708"
        },
        {
            "CODE": "KN4X",
            "GROUP": "UEZU",
            "NAME": "BCL-732",
            "DATETIME": "220506114844"
        },
        {
            "CODE": "KN55",
            "GROUP": "CEYESA",
            "NAME": "ATO-894",
            "DATETIME": "220506120440"
        },
        {
            "CODE": "KN57",
            "GROUP": "LISTO",
            "NAME": "BXY-556",
            "DATETIME": "220506115745"
        },
        {
            "CODE": "KN58",
            "GROUP": "PART BET",
            "NAME": "BMM-399",
            "DATETIME": "220506115433"
        },
        {
            "CODE": "KN5B",
            "GROUP": "LISTOTAX",
            "NAME": "BLA-685",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "KN5F",
            "GROUP": "CACHAY",
            "NAME": "BMO-293",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "KN5K",
            "GROUP": "YUPUPUPU",
            "NAME": "T0P-823",
            "DATETIME": "220506120156"
        },
        {
            "CODE": "KN5L",
            "GROUP": "V.CASTRO",
            "NAME": "A9C-521",
            "DATETIME": "220506120112"
        },
        {
            "CODE": "KN5M",
            "GROUP": "PART BET",
            "NAME": "H2M-348",
            "DATETIME": "220506115132"
        },
        {
            "CODE": "KN5N",
            "GROUP": "FIERRO",
            "NAME": "Z7V-789",
            "DATETIME": "220506115523"
        },
        {
            "CODE": "KN5Q",
            "GROUP": "GILDEMEI",
            "NAME": "BHH-128",
            "DATETIME": "220506111603"
        },
        {
            "CODE": "KN5S",
            "GROUP": "AGRONEGO",
            "NAME": "ALH-732",
            "DATETIME": "220506120347"
        },
        {
            "CODE": "KN5T",
            "GROUP": "PART BET",
            "NAME": "Y2F-790",
            "DATETIME": "220506115407"
        },
        {
            "CODE": "KN5U",
            "GROUP": "M2 LOGIS",
            "NAME": "Y2D-923",
            "DATETIME": "220506120336"
        },
        {
            "CODE": "KN5V",
            "GROUP": "YUPUPUPU",
            "NAME": "M6U-863",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "KN5Y",
            "GROUP": "LINCUNA",
            "NAME": "BBA-751",
            "DATETIME": "220506100730"
        },
        {
            "CODE": "KN62",
            "GROUP": "JOSUF",
            "NAME": "BFR-751",
            "DATETIME": "220505200059"
        },
        {
            "CODE": "KN63",
            "GROUP": "PART BET",
            "NAME": "BSK-263",
            "DATETIME": "220506115431"
        },
        {
            "CODE": "KN64",
            "GROUP": "SANTAINE",
            "NAME": "AVD-897",
            "DATETIME": "220506110847"
        },
        {
            "CODE": "KN69",
            "GROUP": "INTERSEN",
            "NAME": "BCC-712",
            "DATETIME": "220506104534"
        },
        {
            "CODE": "KN6A",
            "GROUP": "NOR OIL",
            "NAME": "T3L-812",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "KN6C",
            "GROUP": "PART BET",
            "NAME": "BSJ-488",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "KN6H",
            "GROUP": "TRABAJA",
            "NAME": "A1B-905",
            "DATETIME": "220506112024"
        },
        {
            "CODE": "KN6J",
            "GROUP": "PART BET",
            "NAME": "BMV-427",
            "DATETIME": "220506115137"
        },
        {
            "CODE": "KN6K",
            "GROUP": "SANTA IN",
            "NAME": "ANQ-863",
            "DATETIME": "220506120520"
        },
        {
            "CODE": "KN6L",
            "GROUP": "SANEAMIE",
            "NAME": "EAD-545",
            "DATETIME": "220503105506"
        },
        {
            "CODE": "KN6M",
            "GROUP": "PART BET",
            "NAME": "BSH-543",
            "DATETIME": "220506115252"
        },
        {
            "CODE": "KN6N",
            "GROUP": "PART BET",
            "NAME": "T0O-920",
            "DATETIME": "220506081337"
        },
        {
            "CODE": "KN6O",
            "GROUP": "FERREYRO",
            "NAME": "575968",
            "DATETIME": "220506120302"
        },
        {
            "CODE": "KN6P",
            "GROUP": "PART BET",
            "NAME": "BNR-202",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "KN6T",
            "GROUP": "LABRIN",
            "NAME": "B0A-773",
            "DATETIME": "220506113748"
        },
        {
            "CODE": "KN6V",
            "GROUP": "A&R AMAZ",
            "NAME": "BDD-924",
            "DATETIME": "220405101829"
        },
        {
            "CODE": "KN6W",
            "GROUP": "PART BET",
            "NAME": "BFJ-881",
            "DATETIME": "220506115530"
        },
        {
            "CODE": "KN6X",
            "GROUP": "PART BET",
            "NAME": "BFR-738",
            "DATETIME": "220506115359"
        },
        {
            "CODE": "KN6Y",
            "GROUP": "PART BET",
            "NAME": "S2D-953",
            "DATETIME": "220506115503"
        },
        {
            "CODE": "KN6Z",
            "GROUP": "SANEAMI",
            "NAME": "EAA-487",
            "DATETIME": "220506120007"
        },
        {
            "CODE": "KN70",
            "GROUP": "LAUVIDAL",
            "NAME": "BRU-165",
            "DATETIME": "220506120305"
        },
        {
            "CODE": "KN72",
            "GROUP": "PART BET",
            "NAME": "BMS-263",
            "DATETIME": "220506104256"
        },
        {
            "CODE": "KN73",
            "GROUP": "SANEAMIE",
            "NAME": "EAD-544",
            "DATETIME": "220506120143"
        },
        {
            "CODE": "KN74",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-955",
            "DATETIME": "220506115941"
        },
        {
            "CODE": "KN76",
            "GROUP": "YUPUPUPU",
            "NAME": "T0Y-859",
            "DATETIME": "220506120446"
        },
        {
            "CODE": "KN78",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-954",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "KN79",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-953",
            "DATETIME": "220506105050"
        },
        {
            "CODE": "KN7A",
            "GROUP": "PART BET",
            "NAME": "T4Z-176",
            "DATETIME": "220506115656"
        },
        {
            "CODE": "KN7C",
            "GROUP": "SANEAMIE",
            "NAME": "EAA-621",
            "DATETIME": "220506112117"
        },
        {
            "CODE": "KN7D",
            "GROUP": "SANEAMI",
            "NAME": "EAA-607",
            "DATETIME": "220506114549"
        },
        {
            "CODE": "KN7E",
            "GROUP": "SANEAMIE",
            "NAME": "EAA-617",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "KN7F",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-964",
            "DATETIME": "220506113903"
        },
        {
            "CODE": "KN7G",
            "GROUP": "SANEAMIE",
            "NAME": "EAA-623",
            "DATETIME": "220506120450"
        },
        {
            "CODE": "KN7I",
            "GROUP": "YUPUPUPU",
            "NAME": "T0Y-823",
            "DATETIME": "220506120401"
        },
        {
            "CODE": "KN7J",
            "GROUP": "YUPUPUPU",
            "NAME": "AER-857",
            "DATETIME": "220506115541"
        },
        {
            "CODE": "KN7L",
            "GROUP": "GILDEMEI",
            "NAME": "BHD-541",
            "DATETIME": "220506115333"
        },
        {
            "CODE": "KN7M",
            "GROUP": "EMNA",
            "NAME": "D0J-743",
            "DATETIME": "220506115207"
        },
        {
            "CODE": "KN7P",
            "GROUP": "FERREYRO",
            "NAME": "98018",
            "DATETIME": "220506104626"
        },
        {
            "CODE": "KN7R",
            "GROUP": "VIZCARDO",
            "NAME": "V0L-750",
            "DATETIME": "220209150225"
        },
        {
            "CODE": "KN7S",
            "GROUP": "FERREYRO",
            "NAME": "606667",
            "DATETIME": "220503182552"
        },
        {
            "CODE": "KN7U",
            "GROUP": "MARLUBE",
            "NAME": "BJW-283",
            "DATETIME": "220506120249"
        },
        {
            "CODE": "KN7V",
            "GROUP": "INTERSEN",
            "NAME": "C4P-713",
            "DATETIME": "220506115132"
        },
        {
            "CODE": "KN7X",
            "GROUP": "FERREYRO",
            "NAME": "94007",
            "DATETIME": "220506110118"
        },
        {
            "CODE": "KN7Y",
            "GROUP": "GILDEMEI",
            "NAME": "BBL-180",
            "DATETIME": "220506115908"
        },
        {
            "CODE": "KN7Z",
            "GROUP": "PART BET",
            "NAME": "BPW-253",
            "DATETIME": "220506110757"
        },
        {
            "CODE": "KN80",
            "GROUP": "SANEAMIE",
            "NAME": "EAD-571",
            "DATETIME": "220506110345"
        },
        {
            "CODE": "KN81",
            "GROUP": "PART BET",
            "NAME": "BLX-436",
            "DATETIME": "220506120517"
        },
        {
            "CODE": "KN84",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-270",
            "DATETIME": "220506115250"
        },
        {
            "CODE": "KN86",
            "GROUP": "CRISPETR",
            "NAME": "BAU-874",
            "DATETIME": "220505135613"
        },
        {
            "CODE": "KN89",
            "GROUP": "GILDEMEI",
            "NAME": "F8H-291",
            "DATETIME": "220506120232"
        },
        {
            "CODE": "KN8A",
            "GROUP": "LISTO",
            "NAME": "BXY-064",
            "DATETIME": "220506115816"
        },
        {
            "CODE": "KN8B",
            "GROUP": "T-PRESTA",
            "NAME": "D5S-367 ",
            "DATETIME": "220506115530"
        },
        {
            "CODE": "KN8D",
            "GROUP": "PART BET",
            "NAME": "C8L-060",
            "DATETIME": "220418203018"
        },
        {
            "CODE": "KN8E",
            "GROUP": "LISTOTAX",
            "NAME": "BPE-374",
            "DATETIME": "220506120440"
        },
        {
            "CODE": "KN8F",
            "GROUP": "ICP",
            "NAME": "ANW-700",
            "DATETIME": "220506115859"
        },
        {
            "CODE": "KN8G",
            "GROUP": "S&R",
            "NAME": "BBP-823",
            "DATETIME": "220506120513"
        },
        {
            "CODE": "KN8H",
            "GROUP": "S&R",
            "NAME": "BBY-765",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "KN8J",
            "GROUP": "PART BET",
            "NAME": "BPS-222",
            "DATETIME": "220506115814"
        },
        {
            "CODE": "KN8K",
            "GROUP": "MAPFRE",
            "NAME": "BKF-195",
            "DATETIME": "220506112856"
        },
        {
            "CODE": "KN8L",
            "GROUP": "T.HILDA",
            "NAME": "BMO-923",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "KN8P",
            "GROUP": "CYTCORP",
            "NAME": "B6M-777",
            "DATETIME": "220503045736"
        },
        {
            "CODE": "KN8R",
            "GROUP": "G.GEMEVA",
            "NAME": "D0J-921",
            "DATETIME": "220506103645"
        },
        {
            "CODE": "KN8V",
            "GROUP": "CYTCORP",
            "NAME": "D3X-740",
            "DATETIME": "220506103837"
        },
        {
            "CODE": "KN8Y",
            "GROUP": "CUPERTIN",
            "NAME": "ADK-521",
            "DATETIME": "220506111618"
        },
        {
            "CODE": "KN8Z",
            "GROUP": "LISTOTAX",
            "NAME": "BKC-083",
            "DATETIME": "220506120408"
        },
        {
            "CODE": "KN90",
            "GROUP": "SILICE",
            "NAME": "A1L-926",
            "DATETIME": "220506120304"
        },
        {
            "CODE": "KN91",
            "GROUP": "E.COMERC",
            "NAME": "AFE-866",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "KN93",
            "GROUP": "VILCHEZ",
            "NAME": "Y1N-841",
            "DATETIME": "220506115804"
        },
        {
            "CODE": "KN96",
            "GROUP": "INCHE",
            "NAME": "AAJ-790",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "KN97",
            "GROUP": "T.INCHE",
            "NAME": "B9U-792",
            "DATETIME": "220506110456"
        },
        {
            "CODE": "KN98",
            "GROUP": "T.INCHE",
            "NAME": "AKI-764",
            "DATETIME": "220506113015"
        },
        {
            "CODE": "KN9A",
            "GROUP": "LAUVIDAL",
            "NAME": "C1F-824",
            "DATETIME": "220506120459"
        },
        {
            "CODE": "KN9B",
            "GROUP": "FERREYRO",
            "NAME": "381432",
            "DATETIME": "220506112953"
        },
        {
            "CODE": "KN9E",
            "GROUP": "LIMAAUTO",
            "NAME": "BDY-753",
            "DATETIME": "220506111517"
        },
        {
            "CODE": "KN9H",
            "GROUP": "PROCARGO",
            "NAME": "C0U-899",
            "DATETIME": "220506113246"
        },
        {
            "CODE": "KN9I",
            "GROUP": "PART BET",
            "NAME": "AWF-925",
            "DATETIME": "220506120355"
        },
        {
            "CODE": "KN9K",
            "GROUP": "IPANAQUE",
            "NAME": "B2J-446",
            "DATETIME": "220506120432"
        },
        {
            "CODE": "KN9N",
            "GROUP": "LISTOTAX",
            "NAME": "BTG-573",
            "DATETIME": "220506115359"
        },
        {
            "CODE": "KN9O",
            "GROUP": "MIGUEL ",
            "NAME": "AYA-988",
            "DATETIME": "220324163337"
        },
        {
            "CODE": "KN9P",
            "GROUP": "TRADESUR",
            "NAME": "BJB-931",
            "DATETIME": "220506115352"
        },
        {
            "CODE": "KN9Q",
            "GROUP": "S.BARTOL",
            "NAME": "500148",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "KN9R",
            "GROUP": "SOLGASER",
            "NAME": "C4V-976",
            "DATETIME": "220506114949"
        },
        {
            "CODE": "KN9V",
            "GROUP": "FERREYRO",
            "NAME": "347007",
            "DATETIME": "220506113756"
        },
        {
            "CODE": "KN9W",
            "GROUP": "GILDEMEI",
            "NAME": "BEJ-221",
            "DATETIME": "220506115901"
        },
        {
            "CODE": "KN9X",
            "GROUP": "RYVAQM",
            "NAME": "D0K-783",
            "DATETIME": "220506112238"
        },
        {
            "CODE": "KN9Y",
            "GROUP": "PART BET",
            "NAME": "BPH-228",
            "DATETIME": "220506115758"
        },
        {
            "CODE": "KNA0",
            "GROUP": "LISTOTAX",
            "NAME": "BYP-465",
            "DATETIME": "220506115631"
        },
        {
            "CODE": "KNA1",
            "GROUP": "PART BET",
            "NAME": "BPV-224",
            "DATETIME": "220506115757"
        },
        {
            "CODE": "KNA2",
            "GROUP": "ENERLETR",
            "NAME": "W6X-939",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "KNA6",
            "GROUP": "IMECSA",
            "NAME": "AXL-732",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "KNA7",
            "GROUP": "LISTO",
            "NAME": "BXY-482",
            "DATETIME": "220506120511"
        },
        {
            "CODE": "KNA8",
            "GROUP": "RENTING",
            "NAME": "BEQ-583",
            "DATETIME": "220411094611"
        },
        {
            "CODE": "KNA9",
            "GROUP": "CRISPETR",
            "NAME": "D6M-836",
            "DATETIME": "220506113048"
        },
        {
            "CODE": "KNAC",
            "GROUP": "INLAND",
            "NAME": "95579",
            "DATETIME": "220506115808"
        },
        {
            "CODE": "KNAD",
            "GROUP": "RENTING",
            "NAME": "BLN-031",
            "DATETIME": "220506115651"
        },
        {
            "CODE": "KNAF",
            "GROUP": "JDM",
            "NAME": "VBG-716",
            "DATETIME": "220506115210"
        },
        {
            "CODE": "KNAM",
            "GROUP": "PART BET",
            "NAME": "BNU-119",
            "DATETIME": "220506115233"
        },
        {
            "CODE": "KNAN",
            "GROUP": "GILDEMEI",
            "NAME": "D2L-111",
            "DATETIME": "220506115531"
        },
        {
            "CODE": "KNAO",
            "GROUP": "YUPUPUPU",
            "NAME": "M6E-820",
            "DATETIME": "220506120403"
        },
        {
            "CODE": "KNAR",
            "GROUP": "YUPUPUPU",
            "NAME": "M5Q-853",
            "DATETIME": "220402194531"
        },
        {
            "CODE": "KNAT",
            "GROUP": "ANDINAPL",
            "NAME": "BCY-890",
            "DATETIME": "220506113438"
        },
        {
            "CODE": "KNAU",
            "GROUP": "JESHUA",
            "NAME": "P3M-819",
            "DATETIME": "220506120422"
        },
        {
            "CODE": "KNB1",
            "GROUP": "PACIFICO",
            "NAME": "BHD-101",
            "DATETIME": "220506114336"
        },
        {
            "CODE": "KNB2",
            "GROUP": "POCHITO",
            "NAME": "BCZ-883",
            "DATETIME": "220506115720"
        },
        {
            "CODE": "KNB9",
            "GROUP": "MEZA",
            "NAME": "BEY-012",
            "DATETIME": "220506115943"
        },
        {
            "CODE": "KNBB",
            "GROUP": "SISSA",
            "NAME": "AXI-800",
            "DATETIME": "220506120438"
        },
        {
            "CODE": "KNBC",
            "GROUP": "GILDEMEI",
            "NAME": "BCV-149",
            "DATETIME": "220505181447"
        },
        {
            "CODE": "KNBE",
            "GROUP": "YUPUPUPU",
            "NAME": "T6L-931",
            "DATETIME": "220506120021"
        },
        {
            "CODE": "KNBH",
            "GROUP": "SISSA",
            "NAME": "AWK-904",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "KNBI",
            "GROUP": "MIGUEL G",
            "NAME": "VBJ-868",
            "DATETIME": "220506115730"
        },
        {
            "CODE": "KNBJ",
            "GROUP": "LAUVIDAL",
            "NAME": "F1Q-027",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "KNBM",
            "GROUP": "T.SANTOP",
            "NAME": "BNB-738",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "KNBQ",
            "GROUP": "YUPUPUPU",
            "NAME": "ABT-948",
            "DATETIME": "220506115915"
        },
        {
            "CODE": "KNBR",
            "GROUP": "LAUVIDAL",
            "NAME": "BRS-644",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "KNBT",
            "GROUP": "SOLGASTR",
            "NAME": "AWC-991",
            "DATETIME": "220502124748"
        },
        {
            "CODE": "KNBV",
            "GROUP": "SOLHYM",
            "NAME": "AYH-922",
            "DATETIME": "220506115527"
        },
        {
            "CODE": "KNBW",
            "GROUP": "YUPUPUPU",
            "NAME": "M6M-934",
            "DATETIME": "220506115936"
        },
        {
            "CODE": "KNBZ",
            "GROUP": "YUPUPUPU",
            "NAME": "T0H-845",
            "DATETIME": "220506115753"
        },
        {
            "CODE": "KNC2",
            "GROUP": "MORCAS",
            "NAME": "BBL-839",
            "DATETIME": "220506115649"
        },
        {
            "CODE": "KNC3",
            "GROUP": "GILDEMEI",
            "NAME": "BDZ-110",
            "DATETIME": "220506113934"
        },
        {
            "CODE": "KNC4",
            "GROUP": "VANTICOP",
            "NAME": "W3I-997",
            "DATETIME": "220506120139"
        },
        {
            "CODE": "KNC5",
            "GROUP": "PART BET",
            "NAME": "AJK-141",
            "DATETIME": "220506115724"
        },
        {
            "CODE": "KNC6",
            "GROUP": "MORCAS",
            "NAME": "BBN-799",
            "DATETIME": "220506115309"
        },
        {
            "CODE": "KNC7",
            "GROUP": "INTERSEN",
            "NAME": "C6V-736",
            "DATETIME": "220506113153"
        },
        {
            "CODE": "KNCG",
            "GROUP": "MHK",
            "NAME": "B6U-774",
            "DATETIME": "220506102012"
        },
        {
            "CODE": "KNCI",
            "GROUP": "COLQUI",
            "NAME": "C7K-778",
            "DATETIME": "220502144504"
        },
        {
            "CODE": "KNCJ",
            "GROUP": "SAN BART",
            "NAME": "AYJ-817",
            "DATETIME": "220506115410"
        },
        {
            "CODE": "KNCM",
            "GROUP": "PART BET",
            "NAME": "BAG-528",
            "DATETIME": "220506115459"
        },
        {
            "CODE": "KNCP",
            "GROUP": "LISTOTAX",
            "NAME": "BYP-101",
            "DATETIME": "220506115357"
        },
        {
            "CODE": "KNCQ",
            "GROUP": "RENTING",
            "NAME": "BLM-563",
            "DATETIME": "220506120516"
        },
        {
            "CODE": "KNCS",
            "GROUP": "CACHAY",
            "NAME": "BMN-027",
            "DATETIME": "220506114957"
        },
        {
            "CODE": "KNCU",
            "GROUP": "S.BARTOL",
            "NAME": "112038",
            "DATETIME": "220506115741"
        },
        {
            "CODE": "KNCW",
            "GROUP": "MOVILGAS",
            "NAME": "A5L-970",
            "DATETIME": "220506114906"
        },
        {
            "CODE": "KND1",
            "GROUP": "NETZSCH",
            "NAME": "C9G-361",
            "DATETIME": "220421224643"
        },
        {
            "CODE": "KND2",
            "GROUP": "PART BET",
            "NAME": "B5R-744",
            "DATETIME": "220506115133"
        },
        {
            "CODE": "KND9",
            "GROUP": "YUPUPUPU",
            "NAME": "M2L-795",
            "DATETIME": "220502112820"
        },
        {
            "CODE": "KNDA",
            "GROUP": "PART BET",
            "NAME": "BSC-670",
            "DATETIME": "220506115555"
        },
        {
            "CODE": "KNDD",
            "GROUP": "ASEGURAD",
            "NAME": "BDX-033",
            "DATETIME": "220417172539"
        },
        {
            "CODE": "KNDJ",
            "GROUP": "PRUEBASL",
            "NAME": "KNDJ9999",
            "DATETIME": "220118081958"
        },
        {
            "CODE": "KNDM",
            "GROUP": "ORVIS",
            "NAME": "BZH-268",
            "DATETIME": "220506115618"
        },
        {
            "CODE": "KNDO",
            "GROUP": "PRUEBASL",
            "NAME": "KNDO9999",
            "DATETIME": "220113083619"
        },
        {
            "CODE": "KNDQ",
            "GROUP": "PART BET",
            "NAME": "BPE-038",
            "DATETIME": "220506114458"
        },
        {
            "CODE": "KNDR",
            "GROUP": "PART BET",
            "NAME": "BCA-378",
            "DATETIME": "220506115907"
        },
        {
            "CODE": "KNDT",
            "GROUP": "PART BET",
            "NAME": "BPE-418",
            "DATETIME": "220506120157"
        },
        {
            "CODE": "KNDU",
            "GROUP": "CASTRO",
            "NAME": "AWG-606",
            "DATETIME": "220506115502"
        },
        {
            "CODE": "KNDV",
            "GROUP": "PART BET",
            "NAME": "BAH-268",
            "DATETIME": "220506120151"
        },
        {
            "CODE": "KNDW",
            "GROUP": "PART BET",
            "NAME": "BDU-313",
            "DATETIME": "220506120444"
        },
        {
            "CODE": "KNDX",
            "GROUP": "ALCOHOL",
            "NAME": "D1U-757",
            "DATETIME": "220506120508"
        },
        {
            "CODE": "KNDY",
            "GROUP": "ASEGURAD",
            "NAME": "BNS-416",
            "DATETIME": "220506120009"
        },
        {
            "CODE": "KNDZ",
            "GROUP": "CACHAY",
            "NAME": "BKT-643",
            "DATETIME": "220506120440"
        },
        {
            "CODE": "KNE0",
            "GROUP": "PART BET",
            "NAME": "BDP-819",
            "DATETIME": "220506120256"
        },
        {
            "CODE": "KNE1",
            "GROUP": "MYI GLO",
            "NAME": "C0P-879",
            "DATETIME": "220506120428"
        },
        {
            "CODE": "KNE2",
            "GROUP": "ASEGURAD",
            "NAME": "BPB-289",
            "DATETIME": "220506114835"
        },
        {
            "CODE": "KNE3",
            "GROUP": "GRAMA",
            "NAME": "9426-OA",
            "DATETIME": "220505131259"
        },
        {
            "CODE": "KNE4",
            "GROUP": "LYM",
            "NAME": "BCZ-940",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "KNE5",
            "GROUP": "PART BET",
            "NAME": "BNC-160",
            "DATETIME": "220506115532"
        },
        {
            "CODE": "KNE7",
            "GROUP": "PART BET",
            "NAME": "BDP-545",
            "DATETIME": "220506115152"
        },
        {
            "CODE": "KNE9",
            "GROUP": "ARBECO",
            "NAME": "ASQ-842",
            "DATETIME": "220506120441"
        },
        {
            "CODE": "KNEB",
            "GROUP": "S.BARTOL",
            "NAME": "10101",
            "DATETIME": "220506115435"
        },
        {
            "CODE": "KNEC",
            "GROUP": "GILDEMEI",
            "NAME": "BBD-268",
            "DATETIME": "220506115411"
        },
        {
            "CODE": "KNED",
            "GROUP": "VILLENA",
            "NAME": "F2F-757",
            "DATETIME": "220506120143"
        },
        {
            "CODE": "KNEF",
            "GROUP": "PART BET",
            "NAME": "ABF-656",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "KNEG",
            "GROUP": "OBRAS CI",
            "NAME": "APC-816",
            "DATETIME": "220506115718"
        },
        {
            "CODE": "KNEK",
            "GROUP": "SGV",
            "NAME": "C5R-780",
            "DATETIME": "220506120511"
        },
        {
            "CODE": "KNEL",
            "GROUP": "MAPFRE",
            "NAME": "BPN-548",
            "DATETIME": "220504214636"
        },
        {
            "CODE": "KNEM",
            "GROUP": "S&R",
            "NAME": "BBU-943",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "KNEN",
            "GROUP": "PART BET",
            "NAME": "AYG-785",
            "DATETIME": "220424121436"
        },
        {
            "CODE": "KNEO",
            "GROUP": "MAPFRE",
            "NAME": "Y2F-750",
            "DATETIME": "220506120109"
        },
        {
            "CODE": "KNEP",
            "GROUP": "YUPUPUPU",
            "NAME": "T0M-837",
            "DATETIME": "220506115740"
        },
        {
            "CODE": "KNEQ",
            "GROUP": "M2 LOGIS",
            "NAME": "AWL-706",
            "DATETIME": "220506120431"
        },
        {
            "CODE": "KNET",
            "GROUP": "TRANSPOR",
            "NAME": "BED-710",
            "DATETIME": "220506113745"
        },
        {
            "CODE": "KNEX",
            "GROUP": "PART BET",
            "NAME": "BDQ-918",
            "DATETIME": "220506115650"
        },
        {
            "CODE": "KNF0",
            "GROUP": "PRUEBASL",
            "NAME": "KNF09999",
            "DATETIME": "220118091317"
        },
        {
            "CODE": "KNF1",
            "GROUP": "TRANSPOR",
            "NAME": "AFY-802",
            "DATETIME": "220504104013"
        },
        {
            "CODE": "KNF4",
            "GROUP": "CHANG CO",
            "NAME": "AYA-845",
            "DATETIME": "220506113740"
        },
        {
            "CODE": "KNF6",
            "GROUP": "ARBECO",
            "NAME": "AMX-900",
            "DATETIME": "220506120002"
        },
        {
            "CODE": "KNFA",
            "GROUP": "INLAND",
            "NAME": "94888",
            "DATETIME": "220506115728"
        },
        {
            "CODE": "KNFB",
            "GROUP": "PRUEBASL",
            "NAME": "KNFB9999",
            "DATETIME": "220317171838"
        },
        {
            "CODE": "KNFD",
            "GROUP": "PART BET",
            "NAME": "BNG-157",
            "DATETIME": "220506115233"
        },
        {
            "CODE": "KNFG",
            "GROUP": "PRUEBASL",
            "NAME": "KNFG9999",
            "DATETIME": "220118081646"
        },
        {
            "CODE": "KNFP",
            "GROUP": "M.INFANT",
            "NAME": "D2M-758",
            "DATETIME": "220506115438"
        },
        {
            "CODE": "KNFQ",
            "GROUP": "PART BET",
            "NAME": "BSR-132",
            "DATETIME": "220506115649"
        },
        {
            "CODE": "KNFU",
            "GROUP": "OLIDEN",
            "NAME": "P2Q-411",
            "DATETIME": "220506105641"
        },
        {
            "CODE": "KNFV",
            "GROUP": "PRUEBASL",
            "NAME": "KNFV9999",
            "DATETIME": "220117230344"
        },
        {
            "CODE": "KNFY",
            "GROUP": "PART BET",
            "NAME": "BMZ-279",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "KNFZ",
            "GROUP": "INSA",
            "NAME": "ARQ-909",
            "DATETIME": "220401213943"
        },
        {
            "CODE": "KNG2",
            "GROUP": "ET.MARTI",
            "NAME": "BND-033",
            "DATETIME": "220506113336"
        },
        {
            "CODE": "KNG5",
            "GROUP": "PART BET",
            "NAME": "BMY-086",
            "DATETIME": "220506115450"
        },
        {
            "CODE": "KNGA",
            "GROUP": "CESEL",
            "NAME": "ROQ-666",
            "DATETIME": "220506114246"
        },
        {
            "CODE": "KNGE",
            "GROUP": "TRADESUR",
            "NAME": "BMJ-823",
            "DATETIME": "220506120116"
        },
        {
            "CODE": "KNGL",
            "GROUP": "ICP",
            "NAME": "ANW-707",
            "DATETIME": "220429152554"
        },
        {
            "CODE": "KNGN",
            "GROUP": "LISTOSEÑ",
            "NAME": "KNGN9999",
            "DATETIME": "220315165325"
        },
        {
            "CODE": "KNGZ",
            "GROUP": "SOLHYM",
            "NAME": "ANY-861",
            "DATETIME": "220506115230"
        },
        {
            "CODE": "KNH6",
            "GROUP": "JDM IMPO",
            "NAME": "VAT-908",
            "DATETIME": "220506115256"
        },
        {
            "CODE": "KNH7",
            "GROUP": "CALIENES",
            "NAME": "ADU-889",
            "DATETIME": "220504073404"
        },
        {
            "CODE": "KNH9",
            "GROUP": "PRUEBASL",
            "NAME": "KNH99999",
            "DATETIME": "220118204449"
        },
        {
            "CODE": "KNHA",
            "GROUP": "PART BET",
            "NAME": "BNC-300",
            "DATETIME": "220506115043"
        },
        {
            "CODE": "KNHE",
            "GROUP": "SOLGASER",
            "NAME": "B6A-994",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "KNHG",
            "GROUP": "LISTOTAX",
            "NAME": "BYP-327",
            "DATETIME": "220506115744"
        },
        {
            "CODE": "KNHH",
            "GROUP": "QORYINTI",
            "NAME": "ARH-846",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "KNHK",
            "GROUP": "PRUEBASL",
            "NAME": "KNHK9999",
            "DATETIME": "220118085955"
        },
        {
            "CODE": "KNHO",
            "GROUP": "CORINSER",
            "NAME": "A5X-319",
            "DATETIME": "220506115151"
        },
        {
            "CODE": "KNHS",
            "GROUP": "ORBIS",
            "NAME": "F6V-711",
            "DATETIME": "220506115756"
        },
        {
            "CODE": "KNHT",
            "GROUP": "LISTOTAX",
            "NAME": "BDD-625",
            "DATETIME": "220506105203"
        },
        {
            "CODE": "KNHU",
            "GROUP": "JDM",
            "NAME": "VBB-710",
            "DATETIME": "220128091002"
        },
        {
            "CODE": "KNHX",
            "GROUP": "PART BET",
            "NAME": "AUD-341",
            "DATETIME": "220506115926"
        },
        {
            "CODE": "KNHY",
            "GROUP": "RNP MADE",
            "NAME": "BDW-804",
            "DATETIME": "220506111442"
        },
        {
            "CODE": "KNHZ",
            "GROUP": "GOOTRIP",
            "NAME": "1534",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "KNI0",
            "GROUP": "GEMEVA",
            "NAME": "TAE-862",
            "DATETIME": "220506115139"
        },
        {
            "CODE": "KNI2",
            "GROUP": "RNP MADE",
            "NAME": "BDU-808",
            "DATETIME": "220506110115"
        },
        {
            "CODE": "KNI3",
            "GROUP": "LISTOTAX",
            "NAME": "BJP-513",
            "DATETIME": "220506112155"
        },
        {
            "CODE": "KNI4",
            "GROUP": "RENTING",
            "NAME": "BHB-375",
            "DATETIME": "220506102744"
        },
        {
            "CODE": "KNI5",
            "GROUP": "LIMA RES",
            "NAME": "ANR-720",
            "DATETIME": "220506115304"
        },
        {
            "CODE": "KNIA",
            "GROUP": "MOVILGAS",
            "NAME": "AYQ-990",
            "DATETIME": "220505140143"
        },
        {
            "CODE": "KNIC",
            "GROUP": "PART BET",
            "NAME": "BRB-088",
            "DATETIME": "220506115418"
        },
        {
            "CODE": "KNID",
            "GROUP": "PART BET",
            "NAME": "BPV-123",
            "DATETIME": "220506115142"
        },
        {
            "CODE": "KNIE",
            "GROUP": "AUTOESPA",
            "NAME": "C1V-829",
            "DATETIME": "220506120346"
        },
        {
            "CODE": "KNIF",
            "GROUP": "IPANAQUE",
            "NAME": "ATC-159",
            "DATETIME": "220506120459"
        },
        {
            "CODE": "KNIK",
            "GROUP": "NECIOSUP",
            "NAME": "D5R-635",
            "DATETIME": "220506111429"
        },
        {
            "CODE": "KNIL",
            "GROUP": "INLAND",
            "NAME": "94886",
            "DATETIME": "220506115520"
        },
        {
            "CODE": "KNIM",
            "GROUP": "INGMEL",
            "NAME": "AUP-753",
            "DATETIME": "220506085532"
        },
        {
            "CODE": "KNIW",
            "GROUP": "INTERNAT",
            "NAME": "AWJ-843",
            "DATETIME": "220506120124"
        },
        {
            "CODE": "KNIX",
            "GROUP": "D.CASTRO",
            "NAME": "D5T-207",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "KNIY",
            "GROUP": "REPARTO",
            "NAME": "F7C-878",
            "DATETIME": "220506115704"
        },
        {
            "CODE": "KNIZ",
            "GROUP": "FERREYRO",
            "NAME": "568436",
            "DATETIME": "220420165606"
        },
        {
            "CODE": "KNJ1",
            "GROUP": "HUARCAYA",
            "NAME": "BMX-765",
            "DATETIME": "220130123929"
        },
        {
            "CODE": "KNJ3",
            "GROUP": "LABRIN",
            "NAME": "A2S-958",
            "DATETIME": "220506114341"
        },
        {
            "CODE": "KNJ4",
            "GROUP": "SANTAINE",
            "NAME": "F6G-890",
            "DATETIME": "220506115126"
        },
        {
            "CODE": "KNJ6",
            "GROUP": "PART BET",
            "NAME": "BRH-432",
            "DATETIME": "220506110219"
        },
        {
            "CODE": "KNJ7",
            "GROUP": "SAGA",
            "NAME": "BNA-708",
            "DATETIME": "220506065919"
        },
        {
            "CODE": "KNJ8",
            "GROUP": "PRUEBASL",
            "NAME": "KNJ89999",
            "DATETIME": "220118084357"
        },
        {
            "CODE": "KNJA",
            "GROUP": "LISTOTAX",
            "NAME": "BYN-600",
            "DATETIME": "220506115730"
        },
        {
            "CODE": "KNJC",
            "GROUP": "FERREYRO",
            "NAME": "485065",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "KNJD",
            "GROUP": "SANTA IN",
            "NAME": "B2F-865",
            "DATETIME": "220506105416"
        },
        {
            "CODE": "KNJI",
            "GROUP": "GILDEMEI",
            "NAME": "BKT-536",
            "DATETIME": "220506104318"
        },
        {
            "CODE": "KNJJ",
            "GROUP": "PART BET",
            "NAME": "F2E-323",
            "DATETIME": "220401061821"
        },
        {
            "CODE": "KNJL",
            "GROUP": "SANTAINE",
            "NAME": "ANQ-846",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "KNJM",
            "GROUP": "INES",
            "NAME": "AVE-763",
            "DATETIME": "220506111635"
        },
        {
            "CODE": "KNJN",
            "GROUP": "TCARRANZ",
            "NAME": "V9F-946",
            "DATETIME": "220506104141"
        },
        {
            "CODE": "KNJP",
            "GROUP": "PART BET",
            "NAME": "BPG-908",
            "DATETIME": "220506115801"
        },
        {
            "CODE": "KNJQ",
            "GROUP": "PART BET",
            "NAME": "1465-OB",
            "DATETIME": "220308172507"
        },
        {
            "CODE": "KNJS",
            "GROUP": "PAPALUVE",
            "NAME": "BPY-240",
            "DATETIME": "220506103940"
        },
        {
            "CODE": "KNJU",
            "GROUP": "PART BET",
            "NAME": "BKU-314",
            "DATETIME": "220506120447"
        },
        {
            "CODE": "KNJX",
            "GROUP": "PAPALUVE",
            "NAME": "BPY-596",
            "DATETIME": "220506120323"
        },
        {
            "CODE": "KNJZ",
            "GROUP": "PAPALUVE",
            "NAME": "BPY-595",
            "DATETIME": "220506115745"
        },
        {
            "CODE": "KNK0",
            "GROUP": "ARBECO",
            "NAME": "W4J-830",
            "DATETIME": "220506113711"
        },
        {
            "CODE": "KNK1",
            "GROUP": "PART BET",
            "NAME": "BPW-635",
            "DATETIME": "220506120158"
        },
        {
            "CODE": "KNK2",
            "GROUP": "G.CAIMAN",
            "NAME": "AXX-989",
            "DATETIME": "220506115851"
        },
        {
            "CODE": "KNK3",
            "GROUP": "PART BET",
            "NAME": "P1V-779",
            "DATETIME": "220506115956"
        },
        {
            "CODE": "KNK5",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-277",
            "DATETIME": "220506115829"
        },
        {
            "CODE": "KNK6",
            "GROUP": "LISTOTAX",
            "NAME": "BYP-100",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "KNK8",
            "GROUP": "HUARCAYA",
            "NAME": "AKY-781",
            "DATETIME": "220222101453"
        },
        {
            "CODE": "KNKB",
            "GROUP": "LAVANDER",
            "NAME": "BHC-750",
            "DATETIME": "220506115127"
        },
        {
            "CODE": "KNKD",
            "GROUP": "SOLHYM",
            "NAME": "BDT-754",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "KNKF",
            "GROUP": "SOLHYM",
            "NAME": "BDC-723",
            "DATETIME": "220506120501"
        },
        {
            "CODE": "KNKG",
            "GROUP": "WESTERN ",
            "NAME": "BFB-734",
            "DATETIME": "220506103951"
        },
        {
            "CODE": "KNKH",
            "GROUP": "INTERSEN",
            "NAME": "AKH-064",
            "DATETIME": "220506113227"
        },
        {
            "CODE": "KNKI",
            "GROUP": "FCAMILA",
            "NAME": "F9P-989",
            "DATETIME": "220506120307"
        },
        {
            "CODE": "KNKK",
            "GROUP": "T.SANTAM",
            "NAME": "C1H-908",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "KNKO",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-968",
            "DATETIME": "220414041550"
        },
        {
            "CODE": "KNKP",
            "GROUP": "T.SANTOS",
            "NAME": "BBT-902",
            "DATETIME": "220506112220"
        },
        {
            "CODE": "KNKQ",
            "GROUP": "TRABAJA",
            "NAME": "EGA-010",
            "DATETIME": "220506115211"
        },
        {
            "CODE": "KNKR",
            "GROUP": "MOSAYHUA",
            "NAME": "BDT-940",
            "DATETIME": "220506112419"
        },
        {
            "CODE": "KNKS",
            "GROUP": "JMT OUT",
            "NAME": "D1N-522",
            "DATETIME": "220506112647"
        },
        {
            "CODE": "KNKT",
            "GROUP": "SANEAMIE",
            "NAME": "EAA-624",
            "DATETIME": "220317093244"
        },
        {
            "CODE": "KNKU",
            "GROUP": "G. PIERO",
            "NAME": "ANE-980",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "KNKW",
            "GROUP": "SANEAMIE",
            "NAME": "EAA-610",
            "DATETIME": "220506120458"
        },
        {
            "CODE": "KNKX",
            "GROUP": "SANEAMIE",
            "NAME": "EAA-609",
            "DATETIME": "220506112312"
        },
        {
            "CODE": "KNKY",
            "GROUP": "CHARACA",
            "NAME": "T0V-862",
            "DATETIME": "220506104459"
        },
        {
            "CODE": "KNL0",
            "GROUP": "INTERSEN",
            "NAME": "BED-873",
            "DATETIME": "220506110845"
        },
        {
            "CODE": "KNL1",
            "GROUP": "JESH OPE",
            "NAME": "P3Y-717",
            "DATETIME": "220506120206"
        },
        {
            "CODE": "KNL4",
            "GROUP": "RENTINLE",
            "NAME": "BHB-561",
            "DATETIME": "220506120204"
        },
        {
            "CODE": "KNL5",
            "GROUP": "YUCRA",
            "NAME": "D0A-819",
            "DATETIME": "220506115819"
        },
        {
            "CODE": "KNL7",
            "GROUP": "S&R",
            "NAME": "BAR-435",
            "DATETIME": "220506120106"
        },
        {
            "CODE": "KNL9",
            "GROUP": "FERREYRO",
            "NAME": "569173",
            "DATETIME": "220417175843"
        },
        {
            "CODE": "KNLA",
            "GROUP": "LEASING",
            "NAME": "BLL-343",
            "DATETIME": "220506115404"
        },
        {
            "CODE": "KNLC",
            "GROUP": "SVS TRAN",
            "NAME": "BLP-744",
            "DATETIME": "220420170648"
        },
        {
            "CODE": "KNLD",
            "GROUP": "A&J",
            "NAME": "BND-924",
            "DATETIME": "220506115604"
        },
        {
            "CODE": "KNLE",
            "GROUP": "PART BET",
            "NAME": "ATN-009",
            "DATETIME": "220506115723"
        },
        {
            "CODE": "KNLH",
            "GROUP": "FERREYRO",
            "NAME": "105528",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "KNLI",
            "GROUP": "JAIRO",
            "NAME": "D8U-885",
            "DATETIME": "220506110552"
        },
        {
            "CODE": "KNLJ",
            "GROUP": "PART BET",
            "NAME": "BDY-866",
            "DATETIME": "220506115651"
        },
        {
            "CODE": "KNLN",
            "GROUP": "PART BET",
            "NAME": "BRG-453",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "KNLO",
            "GROUP": "PART BET",
            "NAME": "VAE-804 ",
            "DATETIME": "220506120438"
        },
        {
            "CODE": "KNLQ",
            "GROUP": "S.BARTOL",
            "NAME": "109797",
            "DATETIME": "220506115545"
        },
        {
            "CODE": "KNLR",
            "GROUP": "LISTOTAX",
            "NAME": "BYS-219",
            "DATETIME": "220506120357"
        },
        {
            "CODE": "KNLS",
            "GROUP": "CAMZA",
            "NAME": "F7I-960",
            "DATETIME": "220506115838"
        },
        {
            "CODE": "KNLU",
            "GROUP": "INTERSEN",
            "NAME": "BED-872",
            "DATETIME": "220506115301"
        },
        {
            "CODE": "KNLV",
            "GROUP": "PART BET",
            "NAME": "BER-926",
            "DATETIME": "220506104009"
        },
        {
            "CODE": "KNLW",
            "GROUP": "OBRAS CI",
            "NAME": "F4L-776",
            "DATETIME": "220506120357"
        },
        {
            "CODE": "KNLX",
            "GROUP": "PART BET",
            "NAME": "BEP-854",
            "DATETIME": "220506115703"
        },
        {
            "CODE": "KNM3",
            "GROUP": "PART BET",
            "NAME": "BRJ-560",
            "DATETIME": "220506115354"
        },
        {
            "CODE": "KNM4",
            "GROUP": "PART BET",
            "NAME": "BRR-510",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "KNM6",
            "GROUP": "PART BET",
            "NAME": "BRG-002",
            "DATETIME": "220506120151"
        },
        {
            "CODE": "KNM7",
            "GROUP": "BERTASOL",
            "NAME": "BDH-946",
            "DATETIME": "220506111146"
        },
        {
            "CODE": "KNMC",
            "GROUP": "MUTIMODA",
            "NAME": "BNG-831",
            "DATETIME": "220506120011"
        },
        {
            "CODE": "KNMF",
            "GROUP": "SOLHYM",
            "NAME": "AYJ-806",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "KNML",
            "GROUP": "VILCA",
            "NAME": "C9T-841",
            "DATETIME": "220506120322"
        },
        {
            "CODE": "KNMM",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-506",
            "DATETIME": "220506120402"
        },
        {
            "CODE": "KNMN",
            "GROUP": "IPANAQUE",
            "NAME": "BPN-059",
            "DATETIME": "220506120307"
        },
        {
            "CODE": "KNMW",
            "GROUP": "SANEAMIE",
            "NAME": "EAD-538",
            "DATETIME": "220506120446"
        },
        {
            "CODE": "KNMX",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-969",
            "DATETIME": "220506115914"
        },
        {
            "CODE": "KNMZ",
            "GROUP": "LISTOTAX",
            "NAME": "BYP-651",
            "DATETIME": "220506120301"
        },
        {
            "CODE": "KNN1",
            "GROUP": "INTERSEN",
            "NAME": "C4P-776",
            "DATETIME": "220506105650"
        },
        {
            "CODE": "KNN3",
            "GROUP": "PART BET",
            "NAME": "BCO-255",
            "DATETIME": "220506120056"
        },
        {
            "CODE": "KNN5",
            "GROUP": "FIESTA",
            "NAME": "AYM-747",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "KNN6",
            "GROUP": "OBRAS CI",
            "NAME": "BBY-694",
            "DATETIME": "220506115941"
        },
        {
            "CODE": "KNN7",
            "GROUP": "PERUVIAN",
            "NAME": "B5F-725",
            "DATETIME": "220506101111"
        },
        {
            "CODE": "KNN8",
            "GROUP": "FIESTRA",
            "NAME": "AJN-741",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "KNN9",
            "GROUP": "ENERLETR",
            "NAME": "W6X-940",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "KNNA",
            "GROUP": "PORTALES",
            "NAME": "96095",
            "DATETIME": "220506115657"
        },
        {
            "CODE": "KNNE",
            "GROUP": "INTERSEN",
            "NAME": "BCC-773",
            "DATETIME": "220506110847"
        },
        {
            "CODE": "KNNF",
            "GROUP": "ICP",
            "NAME": "240676",
            "DATETIME": "220506115803"
        },
        {
            "CODE": "KNNI",
            "GROUP": "PART BET",
            "NAME": "BRD-038",
            "DATETIME": "220506120039"
        },
        {
            "CODE": "KNNJ",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-280",
            "DATETIME": "220506114430"
        },
        {
            "CODE": "KNNM",
            "GROUP": "SOLHYM",
            "NAME": "C5Q-752",
            "DATETIME": "220506120327"
        },
        {
            "CODE": "KNNN",
            "GROUP": "PART BET",
            "NAME": "BAW-322",
            "DATETIME": "220506115920"
        },
        {
            "CODE": "KNNO",
            "GROUP": "PART BET",
            "NAME": "AVR-008",
            "DATETIME": "220506115811"
        },
        {
            "CODE": "KNNS",
            "GROUP": "BELNORTE",
            "NAME": "AZK-983",
            "DATETIME": "220505115454"
        },
        {
            "CODE": "KNNT",
            "GROUP": "TOTAL FA",
            "NAME": "BBG-941",
            "DATETIME": "220505200009"
        },
        {
            "CODE": "KNNU",
            "GROUP": "PANIBRA",
            "NAME": "B5I-810",
            "DATETIME": "220506120154"
        },
        {
            "CODE": "KNNX",
            "GROUP": "SANTOS",
            "NAME": "BND-877",
            "DATETIME": "220506115318"
        },
        {
            "CODE": "KNNY",
            "GROUP": "LIMAAUTO",
            "NAME": "BFS-798",
            "DATETIME": "220506041258"
        },
        {
            "CODE": "KNO0",
            "GROUP": "DEPURA T",
            "NAME": "BFD-825",
            "DATETIME": "220506113514"
        },
        {
            "CODE": "KNO2",
            "GROUP": "PART BET",
            "NAME": "BRQ-575",
            "DATETIME": "220505214518"
        },
        {
            "CODE": "KNO3",
            "GROUP": "FERRETER",
            "NAME": "BFG-819",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "KNO4",
            "GROUP": "SANEAMIE",
            "NAME": "EAA-620",
            "DATETIME": "220506112515"
        },
        {
            "CODE": "KNO5",
            "GROUP": "FERRETER",
            "NAME": "AVI-861",
            "DATETIME": "220506115317"
        },
        {
            "CODE": "KNO6",
            "GROUP": "PART BET",
            "NAME": "ACZ-509",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "KNO8",
            "GROUP": "ALCOHOL",
            "NAME": "B7O-889",
            "DATETIME": "220506115257"
        },
        {
            "CODE": "KNO9",
            "GROUP": "PART BET",
            "NAME": "BSD-680",
            "DATETIME": "220503182122"
        },
        {
            "CODE": "KNOB",
            "GROUP": "LISTOTAX",
            "NAME": "BYQ-023",
            "DATETIME": "220506120514"
        },
        {
            "CODE": "KNOE",
            "GROUP": "CONTRERA",
            "NAME": "EEB-023",
            "DATETIME": "220506112547"
        },
        {
            "CODE": "KNOF",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-967",
            "DATETIME": "220506111641"
        },
        {
            "CODE": "KNOH",
            "GROUP": "FERMINA",
            "NAME": "D8J-710",
            "DATETIME": "220506112058"
        },
        {
            "CODE": "KNOJ",
            "GROUP": "TOTAL FA",
            "NAME": "AWP-828",
            "DATETIME": "220506115349"
        },
        {
            "CODE": "KNOK",
            "GROUP": "PART BET",
            "NAME": "543715",
            "DATETIME": "220506115451"
        },
        {
            "CODE": "KNOM",
            "GROUP": "MIGUEL",
            "NAME": "VOW-828",
            "DATETIME": "220506115801"
        },
        {
            "CODE": "KNOO",
            "GROUP": "LISTOTAX",
            "NAME": "BYP-355",
            "DATETIME": "220506115603"
        },
        {
            "CODE": "KNOQ",
            "GROUP": "PART BET",
            "NAME": "BRT-622",
            "DATETIME": "220506115428"
        },
        {
            "CODE": "KNOR",
            "GROUP": "PART BET",
            "NAME": "BRU-517",
            "DATETIME": "220402161133"
        },
        {
            "CODE": "KNOU",
            "GROUP": "FERMINA",
            "NAME": "F7B-709",
            "DATETIME": "220506102812"
        },
        {
            "CODE": "KNOW",
            "GROUP": "EMNA",
            "NAME": "F0I-738",
            "DATETIME": "220505144645"
        },
        {
            "CODE": "KNP0",
            "GROUP": "DEPURA T",
            "NAME": "AYA-726",
            "DATETIME": "220506115934"
        },
        {
            "CODE": "KNP3",
            "GROUP": "JMT OUT",
            "NAME": "A5I-401",
            "DATETIME": "220506103720"
        },
        {
            "CODE": "KNP5",
            "GROUP": "MAINQUI",
            "NAME": "AZY-815",
            "DATETIME": "220505215840"
        },
        {
            "CODE": "KNP8",
            "GROUP": "SANEAMIE",
            "NAME": "EAA-656",
            "DATETIME": "220414161904"
        },
        {
            "CODE": "KNP9",
            "GROUP": "SANEAMIE",
            "NAME": "EAA-613",
            "DATETIME": "220506113120"
        },
        {
            "CODE": "KNPA",
            "GROUP": "YUPUPUPU",
            "NAME": "T0Z-824",
            "DATETIME": "220506120131"
        },
        {
            "CODE": "KNPC",
            "GROUP": "ICP",
            "NAME": "AWK-777",
            "DATETIME": "220506120438"
        },
        {
            "CODE": "KNPE",
            "GROUP": "TRABAJA ",
            "NAME": "EGJ-598",
            "DATETIME": "220506111054"
        },
        {
            "CODE": "KNPH",
            "GROUP": "T.WEIGHT",
            "NAME": "BRP-252",
            "DATETIME": "220506120000"
        },
        {
            "CODE": "KNPK",
            "GROUP": "LAVAQUIN",
            "NAME": "AEJ-871",
            "DATETIME": "220506112917"
        },
        {
            "CODE": "KNPM",
            "GROUP": "MIGUEL",
            "NAME": "V0W-780",
            "DATETIME": "220506120525"
        },
        {
            "CODE": "KNPO",
            "GROUP": "SANEAMIE",
            "NAME": "AMJ-794",
            "DATETIME": "220506120402"
        },
        {
            "CODE": "KNPR",
            "GROUP": "JSINVERS",
            "NAME": "ARB-914",
            "DATETIME": "220506120519"
        },
        {
            "CODE": "KNPS",
            "GROUP": "POSITIVA",
            "NAME": "BCU-299",
            "DATETIME": "220506105517"
        },
        {
            "CODE": "KNPT",
            "GROUP": "GRAMA",
            "NAME": "6101-BB",
            "DATETIME": "220506092417"
        },
        {
            "CODE": "KNPU",
            "GROUP": "PART BET",
            "NAME": "AKC-724",
            "DATETIME": "220506115247"
        },
        {
            "CODE": "KNPV",
            "GROUP": "UVICA",
            "NAME": "BNI-747",
            "DATETIME": "220506120505"
        },
        {
            "CODE": "KNPX",
            "GROUP": "LAVAQUIN",
            "NAME": "A5W-824",
            "DATETIME": "220506110205"
        },
        {
            "CODE": "KNPZ",
            "GROUP": "OLATI",
            "NAME": "BHU-796",
            "DATETIME": "220506104942"
        },
        {
            "CODE": "KNQ0",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-111",
            "DATETIME": "220506115516"
        },
        {
            "CODE": "KNQ2",
            "GROUP": "SANEAMIE",
            "NAME": "EAD-543",
            "DATETIME": "220506113708"
        },
        {
            "CODE": "KNQ5",
            "GROUP": "CRISPETR",
            "NAME": "ARN-734",
            "DATETIME": "220506115450"
        },
        {
            "CODE": "KNQ7",
            "GROUP": "SOLHYM",
            "NAME": "BBQ-779",
            "DATETIME": "220506120452"
        },
        {
            "CODE": "KNQA",
            "GROUP": "INTERSEN",
            "NAME": "C7K-832",
            "DATETIME": "220506104928"
        },
        {
            "CODE": "KNQD",
            "GROUP": "CHANG CO",
            "NAME": "0409-NA",
            "DATETIME": "220506114948"
        },
        {
            "CODE": "KNQE",
            "GROUP": "PART BET",
            "NAME": "BHC-066",
            "DATETIME": "220506115316"
        },
        {
            "CODE": "KNQH",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-963",
            "DATETIME": "220506120522"
        },
        {
            "CODE": "KNQI",
            "GROUP": "A & B",
            "NAME": "BFY-843",
            "DATETIME": "220506120140"
        },
        {
            "CODE": "KNQJ",
            "GROUP": "PART BET",
            "NAME": "BAP-932",
            "DATETIME": "220506115508"
        },
        {
            "CODE": "KNQM",
            "GROUP": "PART BET",
            "NAME": "BKR-661 ",
            "DATETIME": "220506115418"
        },
        {
            "CODE": "KNQN",
            "GROUP": "IMC.INMO",
            "NAME": "AXN-903",
            "DATETIME": "220506120349"
        },
        {
            "CODE": "KNQP",
            "GROUP": "DE LA O",
            "NAME": "ADJ-748",
            "DATETIME": "220506105309"
        },
        {
            "CODE": "KNQQ",
            "GROUP": "LAUVIDAL",
            "NAME": "F0H-234",
            "DATETIME": "220506114146"
        },
        {
            "CODE": "KNQR",
            "GROUP": "CHANG CO",
            "NAME": "AYA-790",
            "DATETIME": "220506120413"
        },
        {
            "CODE": "KNQU",
            "GROUP": "CAMDE",
            "NAME": "BSJ-507",
            "DATETIME": "220506120403"
        },
        {
            "CODE": "KNQW",
            "GROUP": "RAVELO",
            "NAME": "C2S-191",
            "DATETIME": "220506114129"
        },
        {
            "CODE": "KNQX",
            "GROUP": "WILLIAMS",
            "NAME": "BSD-636",
            "DATETIME": "220506113420"
        },
        {
            "CODE": "KNQY",
            "GROUP": "T.WEIGHT",
            "NAME": "BNS-761",
            "DATETIME": "220506115327"
        },
        {
            "CODE": "KNR0",
            "GROUP": "FERRYERO",
            "NAME": "47005",
            "DATETIME": "220318135242"
        },
        {
            "CODE": "KNR1",
            "GROUP": "SIREB",
            "NAME": "BHD-882",
            "DATETIME": "220504194612"
        },
        {
            "CODE": "KNR3",
            "GROUP": "ARBECO",
            "NAME": "ASP-831",
            "DATETIME": "220506120513"
        },
        {
            "CODE": "KNR5",
            "GROUP": "FERREYRO",
            "NAME": "573555",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "KNR7",
            "GROUP": "SOLHYM",
            "NAME": "ANX-761",
            "DATETIME": "220506115858"
        },
        {
            "CODE": "KNR8",
            "GROUP": "FERREYRO",
            "NAME": "6641",
            "DATETIME": "220506112253"
        },
        {
            "CODE": "KNR9",
            "GROUP": "AGROPECU",
            "NAME": "T4N-892",
            "DATETIME": "220430182944"
        },
        {
            "CODE": "KNRA",
            "GROUP": "FERREYRO",
            "NAME": "580678",
            "DATETIME": "220506120139"
        },
        {
            "CODE": "KNRB",
            "GROUP": "SANEAMIE",
            "NAME": "EAD-546",
            "DATETIME": "220506105720"
        },
        {
            "CODE": "KNRC",
            "GROUP": "YURAX",
            "NAME": "BHE-877",
            "DATETIME": "220430113434"
        },
        {
            "CODE": "KNRD",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-952",
            "DATETIME": "220506114858"
        },
        {
            "CODE": "KNRE",
            "GROUP": "PART BET",
            "NAME": "S2B-854",
            "DATETIME": "220506120042"
        },
        {
            "CODE": "KNRF",
            "GROUP": "CASTINO",
            "NAME": "TAC-874",
            "DATETIME": "220506113958"
        },
        {
            "CODE": "KNRG",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-962",
            "DATETIME": "220506120325"
        },
        {
            "CODE": "KNRI",
            "GROUP": "LISTOTAX",
            "NAME": "BYR-254",
            "DATETIME": "220506120523"
        },
        {
            "CODE": "KNRL",
            "GROUP": "FERREYRO",
            "NAME": "103087",
            "DATETIME": "220506120501"
        },
        {
            "CODE": "KNRM",
            "GROUP": "PART BET",
            "NAME": "S2C-861",
            "DATETIME": "220506115830"
        },
        {
            "CODE": "KNRN",
            "GROUP": "SOL MEDI",
            "NAME": "BTK-238",
            "DATETIME": "220506114024"
        },
        {
            "CODE": "KNRO",
            "GROUP": "IMC.INMO",
            "NAME": "F5L-646",
            "DATETIME": "220506112608"
        },
        {
            "CODE": "KNRP",
            "GROUP": "DELGADO",
            "NAME": "ABR-710",
            "DATETIME": "220322144719"
        },
        {
            "CODE": "KNRR",
            "GROUP": "M.AMBIEN",
            "NAME": "F5L-607",
            "DATETIME": "220506120449"
        },
        {
            "CODE": "KNRU",
            "GROUP": "PART BET",
            "NAME": "BEE-434",
            "DATETIME": "220506115232"
        },
        {
            "CODE": "KNRW",
            "GROUP": "IMC.INMO",
            "NAME": "AXW-787",
            "DATETIME": "220506120328"
        },
        {
            "CODE": "KNRX",
            "GROUP": "PART BET",
            "NAME": "BTO-698",
            "DATETIME": "220304165145"
        },
        {
            "CODE": "KNS0",
            "GROUP": "INTERSEN",
            "NAME": "C4P-724",
            "DATETIME": "220506115525"
        },
        {
            "CODE": "KNS3",
            "GROUP": "STA INES",
            "NAME": "AWR-841",
            "DATETIME": "220504181114"
        },
        {
            "CODE": "KNS4",
            "GROUP": "STA ROSA",
            "NAME": "AAB-971",
            "DATETIME": "220506120259"
        },
        {
            "CODE": "KNS7",
            "GROUP": "REPARTO",
            "NAME": "F7C-862",
            "DATETIME": "220506115353"
        },
        {
            "CODE": "KNTY",
            "GROUP": "PART BET",
            "NAME": "AZC-411",
            "DATETIME": "220506115151"
        },
        {
            "CODE": "KNTZ",
            "GROUP": "SISSA",
            "NAME": "B4C-945",
            "DATETIME": "220506115101"
        },
        {
            "CODE": "KNU8",
            "GROUP": "LAUVIDAL",
            "NAME": "ACV-786",
            "DATETIME": "220506115523"
        },
        {
            "CODE": "KNUC",
            "GROUP": "LAUVIDAL",
            "NAME": "C7E-049",
            "DATETIME": "220506120517"
        },
        {
            "CODE": "KOKG",
            "GROUP": "PRUEBASL",
            "NAME": "KOKG9999",
            "DATETIME": "220118084337"
        },
        {
            "CODE": "KOL4",
            "GROUP": "YUPUPUPU",
            "NAME": "T0I-905",
            "DATETIME": "220428124911"
        },
        {
            "CODE": "KON5",
            "GROUP": "SOLGASTR",
            "NAME": "C3F-995",
            "DATETIME": "220506092137"
        },
        {
            "CODE": "KON6",
            "GROUP": "SANEAMIE",
            "NAME": "EAC-966",
            "DATETIME": "220506114100"
        },
        {
            "CODE": "KON7",
            "GROUP": "PART BET",
            "NAME": "BJQ-139",
            "DATETIME": "220506115402"
        },
        {
            "CODE": "KONA",
            "GROUP": "T.ARMI",
            "NAME": "AKL-793",
            "DATETIME": "220506120434"
        },
        {
            "CODE": "KONB",
            "GROUP": "JESHUA",
            "NAME": "P3Y-725",
            "DATETIME": "220506120407"
        },
        {
            "CODE": "KONE",
            "GROUP": "GILDEMEI",
            "NAME": "BHD-513",
            "DATETIME": "220506112753"
        },
        {
            "CODE": "KONG",
            "GROUP": "JSINVERS",
            "NAME": "ADY-789",
            "DATETIME": "220506120230"
        },
        {
            "CODE": "KONN",
            "GROUP": "JKM",
            "NAME": "F3S-744",
            "DATETIME": "220506120021"
        },
        {
            "CODE": "KONO",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-269",
            "DATETIME": "220506115221"
        },
        {
            "CODE": "KONP",
            "GROUP": "MOVILGAS",
            "NAME": "D7T-713",
            "DATETIME": "220506115801"
        },
        {
            "CODE": "KONU",
            "GROUP": "CACHAY",
            "NAME": "BMM-609",
            "DATETIME": "220506114228"
        },
        {
            "CODE": "KONZ",
            "GROUP": "OBRAS CI",
            "NAME": "ASO-284",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "KOO0",
            "GROUP": "PART BET",
            "NAME": "BRT-532",
            "DATETIME": "220506115634"
        },
        {
            "CODE": "KOO1",
            "GROUP": "ICP",
            "NAME": "292327",
            "DATETIME": "220506082904"
        },
        {
            "CODE": "KOO2",
            "GROUP": "ICP",
            "NAME": "148587",
            "DATETIME": "220506120205"
        },
        {
            "CODE": "KOO3",
            "GROUP": "S.BARTOL",
            "NAME": "500136",
            "DATETIME": "220506115754"
        },
        {
            "CODE": "KOO4",
            "GROUP": "LISTO",
            "NAME": "BXX-669",
            "DATETIME": "220506115309"
        },
        {
            "CODE": "KOO8",
            "GROUP": "PART BET",
            "NAME": "S2A-930",
            "DATETIME": "220506120002"
        },
        {
            "CODE": "KOO9",
            "GROUP": "PART BET",
            "NAME": "BRI-569",
            "DATETIME": "220506120023"
        },
        {
            "CODE": "KOOC",
            "GROUP": "WILLIAMS",
            "NAME": "BSE-637",
            "DATETIME": "220506114230"
        },
        {
            "CODE": "KOOD",
            "GROUP": "FERREYRO",
            "NAME": "322018",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "KOOE",
            "GROUP": "NARCISO",
            "NAME": "BBT-295",
            "DATETIME": "220506115709"
        },
        {
            "CODE": "KOOF",
            "GROUP": "ARBECO",
            "NAME": "W5M-774",
            "DATETIME": "220506115708"
        },
        {
            "CODE": "KOOH",
            "GROUP": "SOLHYM",
            "NAME": "ANR-925",
            "DATETIME": "220506120517"
        },
        {
            "CODE": "KOOI",
            "GROUP": "YUPUPUPU",
            "NAME": "T0Y-875",
            "DATETIME": "220506115843"
        },
        {
            "CODE": "KOOL",
            "GROUP": "INTERSEN",
            "NAME": "C3D-733",
            "DATETIME": "220429072711"
        },
        {
            "CODE": "KOOM",
            "GROUP": "FERREYRO",
            "NAME": "254617",
            "DATETIME": "220506100445"
        },
        {
            "CODE": "KOON",
            "GROUP": "PART BET",
            "NAME": "BYG-535",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "KOOQ",
            "GROUP": "EYON",
            "NAME": "ADD-822",
            "DATETIME": "220506090036"
        },
        {
            "CODE": "KOOR",
            "GROUP": "M2 LOGIS",
            "NAME": "X4X-814",
            "DATETIME": "220506120516"
        },
        {
            "CODE": "KOOS",
            "GROUP": "LISTOTAX",
            "NAME": "BYO-512",
            "DATETIME": "220506115642"
        },
        {
            "CODE": "KOOU",
            "GROUP": "SANEAMIE",
            "NAME": "EAA-626",
            "DATETIME": "220306115626"
        },
        {
            "CODE": "KOP2",
            "GROUP": "INTERSEN",
            "NAME": "C0Z-795",
            "DATETIME": "220423111042"
        },
        {
            "CODE": "KOP3",
            "GROUP": "DIAG.UAL",
            "NAME": "AYX-737",
            "DATETIME": "220506120409"
        },
        {
            "CODE": "KOP4",
            "GROUP": "PART BET",
            "NAME": "BMI-350",
            "DATETIME": "220506115502"
        },
        {
            "CODE": "KOP6",
            "GROUP": "INTERSEN",
            "NAME": "BCB-898",
            "DATETIME": "220506120336"
        },
        {
            "CODE": "L03P",
            "GROUP": "LISTOTAX",
            "NAME": "BTH-674",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "L03Q",
            "GROUP": "LISTOTAX",
            "NAME": "BTH-033",
            "DATETIME": "220506120221"
        },
        {
            "CODE": "L03U",
            "GROUP": "LISTOTAX",
            "NAME": "BTH-116",
            "DATETIME": "220506115451"
        },
        {
            "CODE": "L03V",
            "GROUP": "T.SANTOS",
            "NAME": "ACB-861",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "L044",
            "GROUP": "GRAMA",
            "NAME": "BHR-748",
            "DATETIME": "220506115306"
        },
        {
            "CODE": "L045",
            "GROUP": "REPARTO",
            "NAME": "ANP-707",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "L049",
            "GROUP": "SHILCAYO",
            "NAME": "ABZ-987",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "L04A",
            "GROUP": "TRANSEL",
            "NAME": "AVB-486",
            "DATETIME": "220506115254"
        },
        {
            "CODE": "L04B",
            "GROUP": "LISTOTAX",
            "NAME": "BCL-285",
            "DATETIME": "220506102448"
        },
        {
            "CODE": "L04Q",
            "GROUP": "RENPA",
            "NAME": "BEJ-828",
            "DATETIME": "220506120321"
        },
        {
            "CODE": "L04R",
            "GROUP": "MOVILGAS",
            "NAME": "F8Y-994",
            "DATETIME": "220503084239"
        },
        {
            "CODE": "L04T",
            "GROUP": "LISTOTAX",
            "NAME": "BJP-506",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "L04U",
            "GROUP": "LISTOTAX",
            "NAME": "BJP-063",
            "DATETIME": "220506120227"
        },
        {
            "CODE": "L04V",
            "GROUP": "LISTOTAX",
            "NAME": "BJO-584",
            "DATETIME": "220506064348"
        },
        {
            "CODE": "L050",
            "GROUP": "SOLGASTR",
            "NAME": "C4V-993",
            "DATETIME": "220506114639"
        },
        {
            "CODE": "L05A",
            "GROUP": "LIMAAUTO",
            "NAME": "BSE-451",
            "DATETIME": "220327200206"
        },
        {
            "CODE": "L05G",
            "GROUP": "SOLGASTR",
            "NAME": "D1K-798",
            "DATETIME": "220402121039"
        },
        {
            "CODE": "L05J",
            "GROUP": "SOLGASTR",
            "NAME": "C4V-998",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "L05K",
            "GROUP": "LISTOTAX",
            "NAME": "BCJ-302",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "L05M",
            "GROUP": "VALSAGAS",
            "NAME": "AVL-999",
            "DATETIME": "220505235445"
        },
        {
            "CODE": "L05N",
            "GROUP": "LISTOTAX",
            "NAME": "BJL-141",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "L05X",
            "GROUP": "SOLGASTR",
            "NAME": "B4K-993",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "L060",
            "GROUP": "LISTOTAX",
            "NAME": "BLB-494",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "L063",
            "GROUP": "MOVILGAS",
            "NAME": "F8Z-978",
            "DATETIME": "220506115542"
        },
        {
            "CODE": "L064",
            "GROUP": "LOGVILCH",
            "NAME": "F5D-713",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "L065",
            "GROUP": "LISTOTAX",
            "NAME": "BCI-094",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "L066",
            "GROUP": "PART BET",
            "NAME": "AFY-209",
            "DATETIME": "220506120327"
        },
        {
            "CODE": "L067",
            "GROUP": "NAVARRO",
            "NAME": "C1I-926",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "L068",
            "GROUP": "SOLGASTR",
            "NAME": "D8A-983",
            "DATETIME": "220506120051"
        },
        {
            "CODE": "L069",
            "GROUP": "T.SANTOS",
            "NAME": "C8Z-851",
            "DATETIME": "220506120321"
        },
        {
            "CODE": "L06A",
            "GROUP": "LISTOTAX",
            "NAME": "BCK-490",
            "DATETIME": "220506083439"
        },
        {
            "CODE": "L06B",
            "GROUP": "LOGVILCH",
            "NAME": "BFE-896",
            "DATETIME": "220506120103"
        },
        {
            "CODE": "L06D",
            "GROUP": "LOGVILCH",
            "NAME": "F7V-857",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "L06G",
            "GROUP": "LISTOTAX",
            "NAME": "BDD-515",
            "DATETIME": "220506115718"
        },
        {
            "CODE": "L06H",
            "GROUP": "LISTOTAX",
            "NAME": "BLB-496",
            "DATETIME": "220506111851"
        },
        {
            "CODE": "L06J",
            "GROUP": "SOLGASTR",
            "NAME": "B0D-998",
            "DATETIME": "220506120330"
        },
        {
            "CODE": "L06L",
            "GROUP": "LISTOTAX",
            "NAME": "BCJ-359",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "L06M",
            "GROUP": "LISTOTAX",
            "NAME": "BJL-456",
            "DATETIME": "220506115233"
        },
        {
            "CODE": "L06N",
            "GROUP": "T.SANTOS",
            "NAME": "A8M-882",
            "DATETIME": "220506113857"
        },
        {
            "CODE": "L070",
            "GROUP": "LISTOTAX",
            "NAME": "AMM-307",
            "DATETIME": "220506114439"
        },
        {
            "CODE": "L071",
            "GROUP": "PAMPA",
            "NAME": "216692",
            "DATETIME": "220506113615"
        },
        {
            "CODE": "L074",
            "GROUP": "AG.PAMPA",
            "NAME": "547680",
            "DATETIME": "220506061112"
        },
        {
            "CODE": "L075",
            "GROUP": "LISTOTAX",
            "NAME": "BJQ-011",
            "DATETIME": "220506104630"
        },
        {
            "CODE": "L079",
            "GROUP": "PORTALES",
            "NAME": "BDJ-749",
            "DATETIME": "220506120000"
        },
        {
            "CODE": "L07A",
            "GROUP": "LOGVILCH",
            "NAME": "C5W-928",
            "DATETIME": "220506115033"
        },
        {
            "CODE": "L07C",
            "GROUP": "PAMPA",
            "NAME": "216696",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "L07D",
            "GROUP": "SOLGASER",
            "NAME": "D3M-989",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "L07E",
            "GROUP": "T.SANTOS",
            "NAME": "C9B-846",
            "DATETIME": "220506114218"
        },
        {
            "CODE": "L07F",
            "GROUP": "SOLGASTR",
            "NAME": "B4K-997",
            "DATETIME": "220505104400"
        },
        {
            "CODE": "L07G",
            "GROUP": "LISTOTAX",
            "NAME": "AMO-460",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "L07J",
            "GROUP": "SOLGASTR",
            "NAME": "A7G-973",
            "DATETIME": "220215114239"
        },
        {
            "CODE": "L07Q",
            "GROUP": "LISTOTAX",
            "NAME": "BJL-561",
            "DATETIME": "220506105757"
        },
        {
            "CODE": "L07V",
            "GROUP": "SOLGASTR",
            "NAME": "D1J-996",
            "DATETIME": "220506114100"
        },
        {
            "CODE": "L07W",
            "GROUP": "LISTOTAX",
            "NAME": "BCV-538",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "L080",
            "GROUP": "BEST POR",
            "NAME": "AVL-711",
            "DATETIME": "220506115100"
        },
        {
            "CODE": "L082",
            "GROUP": "MOVILGAS",
            "NAME": "C4W-993",
            "DATETIME": "220506071345"
        },
        {
            "CODE": "L084",
            "GROUP": "SOLTRAK",
            "NAME": "AZB-786",
            "DATETIME": "220502134715"
        },
        {
            "CODE": "L08M",
            "GROUP": "SOLGAS",
            "NAME": "B6J-970",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "L08P",
            "GROUP": "MOVILGAS",
            "NAME": "F4H-995",
            "DATETIME": "220506120339"
        },
        {
            "CODE": "L09K",
            "GROUP": "SOLGASTR",
            "NAME": "D1K-977",
            "DATETIME": "220502111951"
        },
        {
            "CODE": "L0AG",
            "GROUP": "VALSAGAS",
            "NAME": "ALV-902",
            "DATETIME": "220506120403"
        },
        {
            "CODE": "L0AM",
            "GROUP": "SOLGASTR",
            "NAME": "C7I-995",
            "DATETIME": "220506120142"
        },
        {
            "CODE": "L0AN",
            "GROUP": "LISTOTAX",
            "NAME": "BJK-236",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "L0AW",
            "GROUP": "SOLGASER",
            "NAME": "B4Q-970",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "L0B2",
            "GROUP": "OROGAS",
            "NAME": "F1M-980",
            "DATETIME": "220301230045"
        },
        {
            "CODE": "L0B3",
            "GROUP": "T.SANTOS",
            "NAME": "AXK-878",
            "DATETIME": "220506115627"
        },
        {
            "CODE": "L0B7",
            "GROUP": "LISTOTAX",
            "NAME": "BCN-404",
            "DATETIME": "220506114854"
        },
        {
            "CODE": "L0B8",
            "GROUP": "LISTOTAX",
            "NAME": "BJQ-612",
            "DATETIME": "220506114736"
        },
        {
            "CODE": "L0BQ",
            "GROUP": "SAN DIEG",
            "NAME": "BOC-993",
            "DATETIME": "220506092630"
        },
        {
            "CODE": "L0BV",
            "GROUP": "LISTOTAX",
            "NAME": "BTI-253",
            "DATETIME": "220506120027"
        },
        {
            "CODE": "L0BW",
            "GROUP": "SHILCAYO",
            "NAME": "B0G-987",
            "DATETIME": "220201173518"
        },
        {
            "CODE": "L0BX",
            "GROUP": "LOGVILCH",
            "NAME": "B4A-948",
            "DATETIME": "220506104306"
        },
        {
            "CODE": "L0BY",
            "GROUP": "REPARTO",
            "NAME": "BAO-852",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "L0BZ",
            "GROUP": "SOLGASER",
            "NAME": "B4P-984",
            "DATETIME": "220506120354"
        },
        {
            "CODE": "L0C0",
            "GROUP": "LISTOTAX",
            "NAME": "BJL-187",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "L0C2",
            "GROUP": "LISTOTAX",
            "NAME": "BDE-286",
            "DATETIME": "220506120345"
        },
        {
            "CODE": "L0C3",
            "GROUP": "SOLGASTR",
            "NAME": "D9N-978",
            "DATETIME": "220506120351"
        },
        {
            "CODE": "L0C4",
            "GROUP": "SOLGASTR",
            "NAME": "F6A-994",
            "DATETIME": "220506055424"
        },
        {
            "CODE": "L0C6",
            "GROUP": "T.SANTOS",
            "NAME": "F9G-945",
            "DATETIME": "220506120112"
        },
        {
            "CODE": "L0C7",
            "GROUP": "SOLGASTR",
            "NAME": "B0D-997",
            "DATETIME": "220506115045"
        },
        {
            "CODE": "L0C8",
            "GROUP": "LISTOTAX",
            "NAME": "BJQ-385",
            "DATETIME": "220506120333"
        },
        {
            "CODE": "L0C9",
            "GROUP": "LISTOTAX",
            "NAME": "BDE-399",
            "DATETIME": "220506112009"
        },
        {
            "CODE": "L0CA",
            "GROUP": "SELGAS",
            "NAME": "F0K-974",
            "DATETIME": "220505214254"
        },
        {
            "CODE": "L0CC",
            "GROUP": "MOVILGAS",
            "NAME": "F9W-980",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "L0CD",
            "GROUP": "SOLGASER",
            "NAME": "B6H-978",
            "DATETIME": "220506090036"
        },
        {
            "CODE": "L0CE",
            "GROUP": "LISTOTAX",
            "NAME": "BJP-542",
            "DATETIME": "220506120206"
        },
        {
            "CODE": "L0CF",
            "GROUP": "LISTOTAX",
            "NAME": "BJQ-253",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "L0CG",
            "GROUP": "VALSAGAS",
            "NAME": "ASC-999",
            "DATETIME": "220504091618"
        },
        {
            "CODE": "L0CH",
            "GROUP": "TRAN GLP",
            "NAME": "F6O-990",
            "DATETIME": "220506120051"
        },
        {
            "CODE": "L0CJ",
            "GROUP": "SOLGASTR",
            "NAME": "D8D-979",
            "DATETIME": "220210162319"
        },
        {
            "CODE": "L0CL",
            "GROUP": "SLI",
            "NAME": "AYT-820",
            "DATETIME": "220506120127"
        },
        {
            "CODE": "L0CP",
            "GROUP": "MOTORCYC",
            "NAME": "BFN-895",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "L0CQ",
            "GROUP": "LISTOTAX",
            "NAME": "BEG-656",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "L0CS",
            "GROUP": "SOLGASTR",
            "NAME": "D3E-994",
            "DATETIME": "220419171030"
        },
        {
            "CODE": "L0CT",
            "GROUP": "LISTOTAX",
            "NAME": "AVN-611",
            "DATETIME": "220506080939"
        },
        {
            "CODE": "L0CU",
            "GROUP": "SOLGASTR",
            "NAME": "F9A-999",
            "DATETIME": "220329095139"
        },
        {
            "CODE": "L0CX",
            "GROUP": "A&J",
            "NAME": "BAG-903",
            "DATETIME": "220506113200"
        },
        {
            "CODE": "L0CZ",
            "GROUP": "LISTOTAX",
            "NAME": "BJL-471",
            "DATETIME": "220506115612"
        },
        {
            "CODE": "L0D0",
            "GROUP": "PART BET",
            "NAME": "BPF-675",
            "DATETIME": "220506120036"
        },
        {
            "CODE": "L0D1",
            "GROUP": "LISTOTAX",
            "NAME": "BLB-260",
            "DATETIME": "220506113518"
        },
        {
            "CODE": "L0D2",
            "GROUP": "LISTOTAX",
            "NAME": "BLB-080",
            "DATETIME": "220506072336"
        },
        {
            "CODE": "L0D4",
            "GROUP": "SOLGASTR",
            "NAME": "A9A-978",
            "DATETIME": "220428181245"
        },
        {
            "CODE": "L0D5",
            "GROUP": "LOGVILCH",
            "NAME": "B4N-912",
            "DATETIME": "220506120400"
        },
        {
            "CODE": "L0D6",
            "GROUP": "SOLGASTR",
            "NAME": "F3N-996",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "L0DB",
            "GROUP": "T.WDJC",
            "NAME": "A3R-917",
            "DATETIME": "220506103054"
        },
        {
            "CODE": "L0DS",
            "GROUP": "SOLGASTR",
            "NAME": "C3G-971",
            "DATETIME": "220222162200"
        },
        {
            "CODE": "L0E2",
            "GROUP": "SOLGASTR",
            "NAME": "D9N-982",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "L0E7",
            "GROUP": "SOLGASTR",
            "NAME": "B4K-996",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "L0E8",
            "GROUP": "SOLGASTR",
            "NAME": "F6B-994",
            "DATETIME": "220506115648"
        },
        {
            "CODE": "L0EF",
            "GROUP": "SOLGASTR",
            "NAME": "D0E-991",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "L0G1",
            "GROUP": "SOLGASTR",
            "NAME": "C4V-994",
            "DATETIME": "220413100834"
        },
        {
            "CODE": "L0G2",
            "GROUP": "SOLGASTR",
            "NAME": "A4R-990",
            "DATETIME": "220506120257"
        },
        {
            "CODE": "L0G4",
            "GROUP": "LISTOTAX",
            "NAME": "BJL-578",
            "DATETIME": "220506113121"
        },
        {
            "CODE": "L0GN",
            "GROUP": "LISTOTAX",
            "NAME": "BPE-376",
            "DATETIME": "220504131442"
        },
        {
            "CODE": "L0GY",
            "GROUP": "LISTOTAX",
            "NAME": "BJL-563",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "L0H1",
            "GROUP": "LISTOTAX",
            "NAME": "BJL-142",
            "DATETIME": "220506115409"
        },
        {
            "CODE": "L0H2",
            "GROUP": "SOLGASTR",
            "NAME": "D1K-979",
            "DATETIME": "220506120303"
        },
        {
            "CODE": "L0H4",
            "GROUP": "TRAN GLP",
            "NAME": "A3E-970",
            "DATETIME": "220301140339"
        },
        {
            "CODE": "L0H6",
            "GROUP": "LISTOTAX",
            "NAME": "BJL-472",
            "DATETIME": "220506065754"
        },
        {
            "CODE": "L0H7",
            "GROUP": "T.SANTOS",
            "NAME": "AHJ-762",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "L0H8",
            "GROUP": "LISTOTAX",
            "NAME": "BCK-106",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "L0HA",
            "GROUP": "LOGVILCH",
            "NAME": "Y1U-731",
            "DATETIME": "220506114657"
        },
        {
            "CODE": "L0HC",
            "GROUP": "LISTOTAX",
            "NAME": "BDE-269",
            "DATETIME": "220506093354"
        },
        {
            "CODE": "L0HD",
            "GROUP": "LISTOTAX",
            "NAME": "BDD-630",
            "DATETIME": "220505154436"
        },
        {
            "CODE": "L0HE",
            "GROUP": "AGREVO",
            "NAME": "BFQ-838",
            "DATETIME": "220506114118"
        },
        {
            "CODE": "L0HF",
            "GROUP": "VALSAGAS",
            "NAME": "ACQ-985",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "L11N",
            "GROUP": "M.INFANT",
            "NAME": "B4I-916",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "L1PC",
            "GROUP": "PART BET",
            "NAME": "C5R-825",
            "DATETIME": "220506120318"
        },
        {
            "CODE": "L1Q0",
            "GROUP": "SUEROS",
            "NAME": "V2J-863",
            "DATETIME": "220506120321"
        },
        {
            "CODE": "L1R4",
            "GROUP": "PORRAS",
            "NAME": "B2Z-840",
            "DATETIME": "220506114700"
        },
        {
            "CODE": "L1R6",
            "GROUP": "PART BET",
            "NAME": "AFD-387",
            "DATETIME": "220506120042"
        },
        {
            "CODE": "L1RX",
            "GROUP": "PACIFICO",
            "NAME": "C8O-122",
            "DATETIME": "220505130327"
        },
        {
            "CODE": "L3ME",
            "GROUP": "PART BET",
            "NAME": "D5G-222",
            "DATETIME": "220505151300"
        },
        {
            "CODE": "L56S",
            "GROUP": "STA-ROSA",
            "NAME": "D1V-788",
            "DATETIME": "220506115454"
        },
        {
            "CODE": "L594",
            "GROUP": "INLAND",
            "NAME": "C8X-762",
            "DATETIME": "220506111024"
        },
        {
            "CODE": "L5A4",
            "GROUP": "T.CALDER",
            "NAME": "V8C-932",
            "DATETIME": "220506093206"
        },
        {
            "CODE": "L5AC",
            "GROUP": "TRANSGES",
            "NAME": "D1L-735",
            "DATETIME": "220506013121"
        },
        {
            "CODE": "L5GK",
            "GROUP": "JCZ",
            "NAME": "B6J-761",
            "DATETIME": "220505233427"
        },
        {
            "CODE": "L5H8",
            "GROUP": "CORPESA",
            "NAME": "C5O-260",
            "DATETIME": "220506080221"
        },
        {
            "CODE": "L5HK",
            "GROUP": "ORELLANA",
            "NAME": "F8W-731",
            "DATETIME": "220506114309"
        },
        {
            "CODE": "L5HP",
            "GROUP": "AYBCARGU",
            "NAME": "C0V-855",
            "DATETIME": "220506115142"
        },
        {
            "CODE": "L5HT",
            "GROUP": "AUTOESPA",
            "NAME": "C1V-836",
            "DATETIME": "220430122324"
        },
        {
            "CODE": "L5HW",
            "GROUP": "ENMANUEL",
            "NAME": "C1T-845",
            "DATETIME": "220506120300"
        },
        {
            "CODE": "L5JC",
            "GROUP": "AYBCARGU",
            "NAME": "C0Y-886",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "L5JM",
            "GROUP": "REPARTO",
            "NAME": "A4Q-805",
            "DATETIME": "220331121100"
        },
        {
            "CODE": "L5K6",
            "GROUP": "TRANSGES",
            "NAME": "C0W-730",
            "DATETIME": "220505112439"
        },
        {
            "CODE": "L5K7",
            "GROUP": "TRANSGES",
            "NAME": "C0T-705",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "L5K8",
            "GROUP": "TRANSGES",
            "NAME": "C0S-793",
            "DATETIME": "220414201754"
        },
        {
            "CODE": "L5KA",
            "GROUP": "TRANSGES",
            "NAME": "C0T-764",
            "DATETIME": "220112084654"
        },
        {
            "CODE": "L5LA",
            "GROUP": "REDISE",
            "NAME": "D1E-926",
            "DATETIME": "220506115557"
        },
        {
            "CODE": "L5ZL",
            "GROUP": "STA-ROSA",
            "NAME": "C0B-858",
            "DATETIME": "220421110139"
        },
        {
            "CODE": "L603",
            "GROUP": "FORTALEZ",
            "NAME": "BJH-776",
            "DATETIME": "220506114803"
        },
        {
            "CODE": "L604",
            "GROUP": "ENMANUEL",
            "NAME": "ARE-928",
            "DATETIME": "220506113639"
        },
        {
            "CODE": "L60X",
            "GROUP": "MOVIL.GA",
            "NAME": "B8P-034",
            "DATETIME": "220506082539"
        },
        {
            "CODE": "L616",
            "GROUP": "V.CASTRO",
            "NAME": "AVG-172",
            "DATETIME": "220506104551"
        },
        {
            "CODE": "L61A",
            "GROUP": "ALCIDES",
            "NAME": "D1R-125",
            "DATETIME": "220506103700"
        },
        {
            "CODE": "L61C",
            "GROUP": "PALACIN",
            "NAME": "F1G-868",
            "DATETIME": "220505173945"
        },
        {
            "CODE": "L61L",
            "GROUP": "JAISA",
            "NAME": "T4M-914",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "L61S",
            "GROUP": "V.CASTRO",
            "NAME": "D6C-342",
            "DATETIME": "220506115239"
        },
        {
            "CODE": "L61T",
            "GROUP": "ISIL",
            "NAME": "D9L-091",
            "DATETIME": "220506114830"
        },
        {
            "CODE": "L622",
            "GROUP": "ISIL",
            "NAME": "D5E-512",
            "DATETIME": "220505122100"
        },
        {
            "CODE": "L623",
            "GROUP": "SUEROS",
            "NAME": "V8U-793",
            "DATETIME": "220506114521"
        },
        {
            "CODE": "L626",
            "GROUP": "TICLAVIL",
            "NAME": "AZO-873",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "L6SE",
            "GROUP": "ZUÑIGA",
            "NAME": "D4J-751",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "L6UM",
            "GROUP": "JCZTRANS",
            "NAME": "F2H-917",
            "DATETIME": "220506094442"
        },
        {
            "CODE": "L797",
            "GROUP": "T.CALDER",
            "NAME": "V5O-700",
            "DATETIME": "220506114051"
        },
        {
            "CODE": "L7AG",
            "GROUP": "PALACIN",
            "NAME": "C7Z-809",
            "DATETIME": "220506114957"
        },
        {
            "CODE": "L7AW",
            "GROUP": "SERV.GEN",
            "NAME": "D2Z-703",
            "DATETIME": "220503113821"
        },
        {
            "CODE": "L7BZ",
            "GROUP": "ALGARROB",
            "NAME": "D5B-491",
            "DATETIME": "220506120139"
        },
        {
            "CODE": "L7C8",
            "GROUP": "HERCON",
            "NAME": "AJW-700",
            "DATETIME": "220506120357"
        },
        {
            "CODE": "L7CA",
            "GROUP": "MAD.JUNI",
            "NAME": "AKZ-702",
            "DATETIME": "220506115415"
        },
        {
            "CODE": "L7FP",
            "GROUP": "MAPFRE",
            "NAME": "AFN-674",
            "DATETIME": "220506112121"
        },
        {
            "CODE": "L7HV",
            "GROUP": "AYBCARGU",
            "NAME": "D8U-938",
            "DATETIME": "220506120200"
        },
        {
            "CODE": "L7HY",
            "GROUP": "T.SANTAM",
            "NAME": "B3H-295",
            "DATETIME": "220315183257"
        },
        {
            "CODE": "L7JF",
            "GROUP": "REP_GALL",
            "NAME": "V5F-748",
            "DATETIME": "220506114703"
        },
        {
            "CODE": "L7K3",
            "GROUP": "ALCIDESF",
            "NAME": "C5R-502",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "L7L3",
            "GROUP": "MOVIL.GA",
            "NAME": "D8C-938",
            "DATETIME": "220506111754"
        },
        {
            "CODE": "L7QV",
            "GROUP": "INTERBAN",
            "NAME": "C6N-586",
            "DATETIME": "220506115224"
        },
        {
            "CODE": "L7QZ",
            "GROUP": "CESEL",
            "NAME": "D3I-204",
            "DATETIME": "220506104357"
        },
        {
            "CODE": "L7RP",
            "GROUP": "SERVINSA",
            "NAME": "BMH-818",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "L7RW",
            "GROUP": "CESEL",
            "NAME": "D2Z-335",
            "DATETIME": "220420201551"
        },
        {
            "CODE": "L7U7",
            "GROUP": "PART BET",
            "NAME": "F8F-238",
            "DATETIME": "220506090218"
        },
        {
            "CODE": "L7UJ",
            "GROUP": "TILIN",
            "NAME": "V5E-717",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "L84T",
            "GROUP": "TRABAJA",
            "NAME": "EGJ-577",
            "DATETIME": "220503120548"
        },
        {
            "CODE": "L851",
            "GROUP": "TRABAJA",
            "NAME": "A1D-874",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "L85S",
            "GROUP": "TICLAVIL",
            "NAME": "AZO-807",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "L85X",
            "GROUP": "TRABAJA",
            "NAME": "EGA-015",
            "DATETIME": "220505131054"
        },
        {
            "CODE": "L867",
            "GROUP": "TRABAJA",
            "NAME": "EGJ-601",
            "DATETIME": "220506092812"
        },
        {
            "CODE": "L868",
            "GROUP": "TRABAJA",
            "NAME": "EGA-001",
            "DATETIME": "220505145648"
        },
        {
            "CODE": "L86D",
            "GROUP": "TRABAJA",
            "NAME": "EGJ-635",
            "DATETIME": "220506103224"
        },
        {
            "CODE": "L9RV",
            "GROUP": "MANASA",
            "NAME": "C2I-053",
            "DATETIME": "220505225745"
        },
        {
            "CODE": "L9VQ",
            "GROUP": "TAXI",
            "NAME": "A5A-252",
            "DATETIME": "220506105606"
        },
        {
            "CODE": "L9W9",
            "GROUP": "BONALIS",
            "NAME": "D8R-339",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "L9WN",
            "GROUP": "TAXI",
            "NAME": "TGP-355",
            "DATETIME": "220506073718"
        },
        {
            "CODE": "LAAE",
            "GROUP": "MOVIL.GA",
            "NAME": "AEB-691",
            "DATETIME": "220506114036"
        },
        {
            "CODE": "LAAQ",
            "GROUP": "QUALIT",
            "NAME": "AAD-771",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "LAB1",
            "GROUP": "TRABAJA",
            "NAME": "A1D-871",
            "DATETIME": "220421225030"
        },
        {
            "CODE": "LAB3",
            "GROUP": "T.CALDER",
            "NAME": "V4X-868",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "LAB6",
            "GROUP": "T.EMNA",
            "NAME": "D0I-770",
            "DATETIME": "220506115400"
        },
        {
            "CODE": "LAB7",
            "GROUP": "AGROPECU",
            "NAME": "F4I-871",
            "DATETIME": "220419143200"
        },
        {
            "CODE": "LABA",
            "GROUP": "VILCA",
            "NAME": "F2Q-923",
            "DATETIME": "220506113048"
        },
        {
            "CODE": "LABR",
            "GROUP": "VILCA",
            "NAME": "F2R-786",
            "DATETIME": "220506101909"
        },
        {
            "CODE": "LACG",
            "GROUP": "TRANSGES",
            "NAME": "F5Q-835",
            "DATETIME": "220506105730"
        },
        {
            "CODE": "LACQ",
            "GROUP": "VANTICOP",
            "NAME": "W2G-985",
            "DATETIME": "220506112115"
        },
        {
            "CODE": "LACY",
            "GROUP": "CORMEI",
            "NAME": "D6K-765",
            "DATETIME": "220506093518"
        },
        {
            "CODE": "LAD0",
            "GROUP": "CORMEI",
            "NAME": "A3Y-878",
            "DATETIME": "220505081948"
        },
        {
            "CODE": "LADW",
            "GROUP": "REPARTO ",
            "NAME": "F7C-869",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "LAEA",
            "GROUP": "STA-ROSA",
            "NAME": "F5P-896",
            "DATETIME": "220506115254"
        },
        {
            "CODE": "LAEL",
            "GROUP": "TRANSGES",
            "NAME": "F5P-905",
            "DATETIME": "220425091730"
        },
        {
            "CODE": "LAFJ",
            "GROUP": "TRANSGES",
            "NAME": "F5P-861",
            "DATETIME": "220506120012"
        },
        {
            "CODE": "LAPD",
            "GROUP": "PASQUEL",
            "NAME": "F9J-353",
            "DATETIME": "220506115651"
        },
        {
            "CODE": "LAQ2",
            "GROUP": "VILCA",
            "NAME": "D7E-807",
            "DATETIME": "220428055051"
        },
        {
            "CODE": "LAZS",
            "GROUP": "CORMEI",
            "NAME": "C0W-795",
            "DATETIME": "220506110545"
        },
        {
            "CODE": "LB02",
            "GROUP": "PERUCONT",
            "NAME": "D3G-060",
            "DATETIME": "220506120157"
        },
        {
            "CODE": "LB16",
            "GROUP": "T.CALDER",
            "NAME": "V7E-849",
            "DATETIME": "220506113954"
        },
        {
            "CODE": "LB1J",
            "GROUP": "CORMEI",
            "NAME": "C8J-814",
            "DATETIME": "220506081500"
        },
        {
            "CODE": "LBG7",
            "GROUP": "QUALIT",
            "NAME": "F9D-819",
            "DATETIME": "220506115409"
        },
        {
            "CODE": "LBHL",
            "GROUP": "VANTICOP",
            "NAME": "AHN-712",
            "DATETIME": "220506120115"
        },
        {
            "CODE": "LBHN",
            "GROUP": "TCARRION",
            "NAME": "W2K-976",
            "DATETIME": "220324193121"
        },
        {
            "CODE": "LBJV",
            "GROUP": "GEMEVA",
            "NAME": "T5O-809",
            "DATETIME": "220506120309"
        },
        {
            "CODE": "LBJX",
            "GROUP": "T.CAMILA",
            "NAME": "W2H-990",
            "DATETIME": "220506114736"
        },
        {
            "CODE": "LEBP",
            "GROUP": "INVMARIA",
            "NAME": "F7B-767",
            "DATETIME": "220506075551"
        },
        {
            "CODE": "LEBQ",
            "GROUP": "TRANSGES",
            "NAME": "C0R-785",
            "DATETIME": "220506115621"
        },
        {
            "CODE": "LEBS",
            "GROUP": "REPARTO",
            "NAME": "F5W-871",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "LEBU",
            "GROUP": "PRONATUR",
            "NAME": "F5W-747",
            "DATETIME": "220505101503"
        },
        {
            "CODE": "LEBX",
            "GROUP": "VANTICOP",
            "NAME": "W4H-753",
            "DATETIME": "220419133627"
        },
        {
            "CODE": "LECF",
            "GROUP": "FANO",
            "NAME": "A5N-997",
            "DATETIME": "220503160421"
        },
        {
            "CODE": "LECH",
            "GROUP": "VANTICOP",
            "NAME": "F8A-911",
            "DATETIME": "220506114342"
        },
        {
            "CODE": "LECJ",
            "GROUP": "REPARTO",
            "NAME": "F5W-898",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "LECK",
            "GROUP": "STA-ROSA",
            "NAME": "F5M-733",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "LECL",
            "GROUP": "TRUCKTIR",
            "NAME": "C5H-181",
            "DATETIME": "220506120315"
        },
        {
            "CODE": "LECM",
            "GROUP": "TRUCKTIR",
            "NAME": "A5T-105",
            "DATETIME": "220506103848"
        },
        {
            "CODE": "LED4",
            "GROUP": "MUNDO",
            "NAME": "F6X-031",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "LEDC",
            "GROUP": "J.C.A.",
            "NAME": "F7B-889",
            "DATETIME": "220506110306"
        },
        {
            "CODE": "LEE1",
            "GROUP": "REPARTO",
            "NAME": "F5W-846",
            "DATETIME": "220506120018"
        },
        {
            "CODE": "LEE2",
            "GROUP": "TRABAJA",
            "NAME": "EGJ-578",
            "DATETIME": "220506114930"
        },
        {
            "CODE": "LEEJ",
            "GROUP": "REPARTO",
            "NAME": "F5W-896",
            "DATETIME": "220506113851"
        },
        {
            "CODE": "LEEP",
            "GROUP": "REPARTO",
            "NAME": "AAX-994",
            "DATETIME": "220504080406"
        },
        {
            "CODE": "LEF4",
            "GROUP": "TRABAJA",
            "NAME": "A1D-873",
            "DATETIME": "220404175424"
        },
        {
            "CODE": "LEF6",
            "GROUP": "TRABAJA",
            "NAME": "A1D-872",
            "DATETIME": "220506120351"
        },
        {
            "CODE": "LEFN",
            "GROUP": "ALFRANSA",
            "NAME": "F5U-916",
            "DATETIME": "220506111421"
        },
        {
            "CODE": "LEFQ",
            "GROUP": "ALFRANSA",
            "NAME": "C3X-798",
            "DATETIME": "220506115242"
        },
        {
            "CODE": "LEFS",
            "GROUP": "PROCARGO",
            "NAME": "B8H-739",
            "DATETIME": "220504190509"
        },
        {
            "CODE": "LEFV",
            "GROUP": "HUGAMOR",
            "NAME": "AJO-729",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "LEFY",
            "GROUP": "ALFRANSA",
            "NAME": "C7A-836",
            "DATETIME": "220506113912"
        },
        {
            "CODE": "LET0",
            "GROUP": "INTERBAN",
            "NAME": "C6M-228",
            "DATETIME": "220506115403"
        },
        {
            "CODE": "LETC",
            "GROUP": "INTERBAN",
            "NAME": "C6Y-509",
            "DATETIME": "220504195721"
        },
        {
            "CODE": "LEUV",
            "GROUP": "NEXUS T.",
            "NAME": "B5B-712",
            "DATETIME": "220506111436"
        },
        {
            "CODE": "LEUZ",
            "GROUP": "PART_BET",
            "NAME": "AAV-544",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "LEV8",
            "GROUP": "REPARTO",
            "NAME": "F5W-908",
            "DATETIME": "220422113751"
        },
        {
            "CODE": "LEVF",
            "GROUP": "ALFRANSA",
            "NAME": "F5U-800",
            "DATETIME": "220506115039"
        },
        {
            "CODE": "LEVG",
            "GROUP": "T.HILDA",
            "NAME": "F8H-913",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "LEVU",
            "GROUP": "REPARTO",
            "NAME": "F5Y-789",
            "DATETIME": "220505174933"
        },
        {
            "CODE": "LEVX",
            "GROUP": "TRABAJA",
            "NAME": "EGJ-576",
            "DATETIME": "220506114536"
        },
        {
            "CODE": "LEWB",
            "GROUP": "REPARTO",
            "NAME": "F5Y-790",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "LEWG",
            "GROUP": "REPARTO",
            "NAME": "F5W-909",
            "DATETIME": "220504095709"
        },
        {
            "CODE": "LGUN",
            "GROUP": "RIMAC",
            "NAME": "AAN-367",
            "DATETIME": "220505135139"
        },
        {
            "CODE": "LGVC",
            "GROUP": "PNP",
            "NAME": "BAO-504",
            "DATETIME": "220506112815"
        },
        {
            "CODE": "LGW9",
            "GROUP": "GILDEMEI",
            "NAME": "BCX-080",
            "DATETIME": "220506080654"
        },
        {
            "CODE": "LGX9",
            "GROUP": "MAPFRE",
            "NAME": "EGZ-633",
            "DATETIME": "220505130918"
        },
        {
            "CODE": "LGXH",
            "GROUP": "MAPFRE",
            "NAME": "AYN-172",
            "DATETIME": "220503180748"
        },
        {
            "CODE": "LJHX",
            "GROUP": "NILFISK",
            "NAME": "AWO-719",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "LJJ1",
            "GROUP": "PACIFICO",
            "NAME": "ADA-663",
            "DATETIME": "220506113512"
        },
        {
            "CODE": "LPB7",
            "GROUP": "PETROL-C",
            "NAME": "AER-998",
            "DATETIME": "220506120527"
        },
        {
            "CODE": "LPDX",
            "GROUP": "PROCARGO",
            "NAME": "F9X-064",
            "DATETIME": "220506120003"
        },
        {
            "CODE": "LPEA",
            "GROUP": "SUEROS",
            "NAME": "V6Q-929",
            "DATETIME": "220506114957"
        },
        {
            "CODE": "LPEH",
            "GROUP": "SUEROS",
            "NAME": "V6Q-949",
            "DATETIME": "220506115812"
        },
        {
            "CODE": "LPEU",
            "GROUP": "T.CALDER",
            "NAME": "V6Z-730",
            "DATETIME": "220503135206"
        },
        {
            "CODE": "LPEY",
            "GROUP": "SUEROS",
            "NAME": "V6T-702",
            "DATETIME": "220506113915"
        },
        {
            "CODE": "LPF4",
            "GROUP": "G.ATICO",
            "NAME": "V3V-989",
            "DATETIME": "220505154039"
        },
        {
            "CODE": "LPF6",
            "GROUP": "HUGAMOR",
            "NAME": "C2B-940",
            "DATETIME": "220506110806"
        },
        {
            "CODE": "LPF7",
            "GROUP": "OROZCO",
            "NAME": "V9D-737",
            "DATETIME": "220506114915"
        },
        {
            "CODE": "LPF8",
            "GROUP": "G.ATICO",
            "NAME": "V2B-973",
            "DATETIME": "220504072354"
        },
        {
            "CODE": "LPFC",
            "GROUP": "PORRAS",
            "NAME": "C5Z-904",
            "DATETIME": "220506115536"
        },
        {
            "CODE": "LT6X",
            "GROUP": "STA-ROSA",
            "NAME": "ADZ-770",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "LT6Z",
            "GROUP": "POLMAR",
            "NAME": "D4H-780",
            "DATETIME": "220506113957"
        },
        {
            "CODE": "LT7C",
            "GROUP": "SOLGASTR",
            "NAME": "B4K-994",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "LX6C",
            "GROUP": "VILCA",
            "NAME": "W5C-877",
            "DATETIME": "220506113921"
        },
        {
            "CODE": "LX6V",
            "GROUP": "ALCIDESF",
            "NAME": "D0X-295",
            "DATETIME": "220505160418"
        },
        {
            "CODE": "LX6Z",
            "GROUP": "VILCA",
            "NAME": "W5C-883",
            "DATETIME": "220506114130"
        },
        {
            "CODE": "LX7H",
            "GROUP": "VILCA",
            "NAME": "W5C-882",
            "DATETIME": "220506114209"
        },
        {
            "CODE": "LX7Y",
            "GROUP": "M.INFANT",
            "NAME": "C0R-268",
            "DATETIME": "220506051045"
        },
        {
            "CODE": "LX81",
            "GROUP": "M.INFANT",
            "NAME": "D7E-844",
            "DATETIME": "220506113451"
        },
        {
            "CODE": "LX9A",
            "GROUP": "PART BET",
            "NAME": "F7D-501",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "LX9B",
            "GROUP": "TAXISAT",
            "NAME": "ACF-103",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "LXA4",
            "GROUP": "SISSA",
            "NAME": "AUT-916",
            "DATETIME": "220506113803"
        },
        {
            "CODE": "LXAK",
            "GROUP": "GENEIST",
            "NAME": "C8U-707",
            "DATETIME": "220506110742"
        },
        {
            "CODE": "LXAY",
            "GROUP": "JMT OUT",
            "NAME": "ABM-947",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "LXBF",
            "GROUP": "MAPFRE",
            "NAME": "ABL-429",
            "DATETIME": "220506084757"
        },
        {
            "CODE": "LXBJ",
            "GROUP": "QANTU",
            "NAME": "F5Z-833",
            "DATETIME": "220506074806"
        },
        {
            "CODE": "LXC3",
            "GROUP": "FONSECA",
            "NAME": "BDU-206",
            "DATETIME": "220420144727"
        },
        {
            "CODE": "LXCB",
            "GROUP": "RIMAC",
            "NAME": "B7R-412",
            "DATETIME": "220505193715"
        },
        {
            "CODE": "LXCP",
            "GROUP": "NOR OIL",
            "NAME": "T7F-949",
            "DATETIME": "220330134551"
        },
        {
            "CODE": "LXDJ",
            "GROUP": "PACIFICO",
            "NAME": "D6L-450",
            "DATETIME": "220506114718"
        },
        {
            "CODE": "LXE4",
            "GROUP": "PART BET",
            "NAME": "ACJ-284",
            "DATETIME": "220506120103"
        },
        {
            "CODE": "M0PR",
            "GROUP": "MARYORIC",
            "NAME": "C4Q-793",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "M0PS",
            "GROUP": "PACIFICO",
            "NAME": "AWE-641",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "M0PW",
            "GROUP": "LISTOTAX",
            "NAME": "BTL-386",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "M0QE",
            "GROUP": "LISTOTAX",
            "NAME": "BBA-569",
            "DATETIME": "220506092524"
        },
        {
            "CODE": "M0RB",
            "GROUP": "MOVIL.GA",
            "NAME": "C6I-991",
            "DATETIME": "220506113212"
        },
        {
            "CODE": "M0RQ",
            "GROUP": "INTERAME",
            "NAME": "T8U-825",
            "DATETIME": "220505174827"
        },
        {
            "CODE": "M0RY",
            "GROUP": "SHILCAYO",
            "NAME": "ATA-844",
            "DATETIME": "220504191442"
        },
        {
            "CODE": "M0S4",
            "GROUP": "REPARTO",
            "NAME": "ANO-894",
            "DATETIME": "220506114209"
        },
        {
            "CODE": "M0S8",
            "GROUP": "POSITIVA",
            "NAME": "AVO-595",
            "DATETIME": "220506101124"
        },
        {
            "CODE": "M0SP",
            "GROUP": "SAN MART",
            "NAME": "B4F-821",
            "DATETIME": "220506072842"
        },
        {
            "CODE": "M0SS",
            "GROUP": "PROCARGO",
            "NAME": "C8N-933",
            "DATETIME": "220505211454"
        },
        {
            "CODE": "M0SU",
            "GROUP": "GILDEMEI",
            "NAME": "BEQ-608",
            "DATETIME": "220401153930"
        },
        {
            "CODE": "M0TH",
            "GROUP": "PART BET",
            "NAME": "AWP-338",
            "DATETIME": "220506115748"
        },
        {
            "CODE": "M0UL",
            "GROUP": "LISTOTAX",
            "NAME": "BBB-425",
            "DATETIME": "220506040012"
        },
        {
            "CODE": "M0VM",
            "GROUP": "RENTING",
            "NAME": "AXC-935",
            "DATETIME": "220506111824"
        },
        {
            "CODE": "M0VW",
            "GROUP": "LISTOTAX",
            "NAME": "BBB-000",
            "DATETIME": "220506062903"
        },
        {
            "CODE": "M0WB",
            "GROUP": "CONDOR.T",
            "NAME": "F2L-957",
            "DATETIME": "220506073921"
        },
        {
            "CODE": "M0WH",
            "GROUP": "POLMAR",
            "NAME": "ADP-999",
            "DATETIME": "220506115448"
        },
        {
            "CODE": "M0WN",
            "GROUP": "OREPAL",
            "NAME": "ASG-887",
            "DATETIME": "220505221121"
        },
        {
            "CODE": "M0WW",
            "GROUP": "RENTANOR",
            "NAME": "T8K-919",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "M0WZ",
            "GROUP": "POLMAR",
            "NAME": "D7M-799",
            "DATETIME": "220506115542"
        },
        {
            "CODE": "M0X2",
            "GROUP": "RENTANOR",
            "NAME": "T8K-898",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "M0X7",
            "GROUP": "AUTONORT",
            "NAME": "T4E-405",
            "DATETIME": "220506115542"
        },
        {
            "CODE": "M0XA",
            "GROUP": "SHILCAYO",
            "NAME": "C6N-974",
            "DATETIME": "220409174709"
        },
        {
            "CODE": "M0XD",
            "GROUP": "BIDDLE",
            "NAME": "D6B-178",
            "DATETIME": "220409065148"
        },
        {
            "CODE": "M0XK",
            "GROUP": "GILDEMEI",
            "NAME": "AWL-693",
            "DATETIME": "220506105245"
        },
        {
            "CODE": "M0XS",
            "GROUP": "FAMESA",
            "NAME": "AYY-844",
            "DATETIME": "220422101618"
        },
        {
            "CODE": "M2LE",
            "GROUP": "GRUAS SA",
            "NAME": "AJS-907",
            "DATETIME": "220503085645"
        },
        {
            "CODE": "M2N6",
            "GROUP": "RENTINCA",
            "NAME": "C4C-727",
            "DATETIME": "220506113633"
        },
        {
            "CODE": "M2N7",
            "GROUP": "PART BET",
            "NAME": "BSB-674",
            "DATETIME": "220506115527"
        },
        {
            "CODE": "M2NG",
            "GROUP": "MACHA ",
            "NAME": "F1A-714",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "M2P5",
            "GROUP": "GREMPOL",
            "NAME": "A2T-988",
            "DATETIME": "220506115427"
        },
        {
            "CODE": "M2P9",
            "GROUP": "PART BET",
            "NAME": "AWP-613",
            "DATETIME": "220506114657"
        },
        {
            "CODE": "M2PC",
            "GROUP": "GILDEMEI",
            "NAME": "AWV-542",
            "DATETIME": "220506114621"
        },
        {
            "CODE": "M2PK",
            "GROUP": "GILDEMEI",
            "NAME": "AWT-576",
            "DATETIME": "220503174954"
        },
        {
            "CODE": "M2PR",
            "GROUP": "ENERLETR",
            "NAME": "AWJ-860",
            "DATETIME": "220506115421"
        },
        {
            "CODE": "M2Q0",
            "GROUP": "CONDOR.T",
            "NAME": "D0Y-952",
            "DATETIME": "220125094330"
        },
        {
            "CODE": "M2QU",
            "GROUP": "LISTOTAX",
            "NAME": "BXO-057",
            "DATETIME": "220506115542"
        },
        {
            "CODE": "M2QW",
            "GROUP": "MOVIL.GA",
            "NAME": "D3C-757",
            "DATETIME": "220506094603"
        },
        {
            "CODE": "M2QZ",
            "GROUP": "LISTOTAX",
            "NAME": "BNE-301",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "M2R3",
            "GROUP": "SAN IGNA",
            "NAME": "C3A-863",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "M2R4",
            "GROUP": "CARGO WP",
            "NAME": "ARH-774",
            "DATETIME": "220506102945"
        },
        {
            "CODE": "M2R6",
            "GROUP": "ESPAR ",
            "NAME": "AWY-075",
            "DATETIME": "220506080554"
        },
        {
            "CODE": "M2RJ",
            "GROUP": "LISTOTAX",
            "NAME": "BHZ-345",
            "DATETIME": "220506115724"
        },
        {
            "CODE": "M2RV",
            "GROUP": "CONDOR.T",
            "NAME": "F1Z-960",
            "DATETIME": "220113100703"
        },
        {
            "CODE": "M2SC",
            "GROUP": "LAN XING",
            "NAME": "ASM-817",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "M2SJ",
            "GROUP": "ALCIDESF",
            "NAME": "AWX-166",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "M2SK",
            "GROUP": "RENTING",
            "NAME": "AXQ-818",
            "DATETIME": "220504173703"
        },
        {
            "CODE": "M2SS",
            "GROUP": "MAPFRE",
            "NAME": "ASG-836",
            "DATETIME": "220505183812"
        },
        {
            "CODE": "M2SY",
            "GROUP": "BONALIS",
            "NAME": "RQ-7975",
            "DATETIME": "220506113009"
        },
        {
            "CODE": "M2TC",
            "GROUP": "PACIFICO",
            "NAME": "ALD-035",
            "DATETIME": "220505212033"
        },
        {
            "CODE": "M2TH",
            "GROUP": "FAMHORA",
            "NAME": "ACG-876",
            "DATETIME": "220505222600"
        },
        {
            "CODE": "M2TS",
            "GROUP": "FAMHORA ",
            "NAME": "ASE-796",
            "DATETIME": "220506101703"
        },
        {
            "CODE": "M2TY",
            "GROUP": "GILDEMEI",
            "NAME": "AWS-020",
            "DATETIME": "220506083736"
        },
        {
            "CODE": "M2UA",
            "GROUP": "GEMEVA",
            "NAME": "T8R-922",
            "DATETIME": "220506120127"
        },
        {
            "CODE": "M2UP",
            "GROUP": "GEMEVA",
            "NAME": "T8R-913",
            "DATETIME": "220506093454"
        },
        {
            "CODE": "M3S8",
            "GROUP": "SHILCAYO",
            "NAME": "B8G-995",
            "DATETIME": "220506110018"
        },
        {
            "CODE": "M3T8",
            "GROUP": "LISTOTAX",
            "NAME": "BBA-207",
            "DATETIME": "220506093251"
        },
        {
            "CODE": "M3TQ",
            "GROUP": "ALCIDESF",
            "NAME": "AWZ-051",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "M3TT",
            "GROUP": "GILDEMEI",
            "NAME": "AST-817",
            "DATETIME": "220506120306"
        },
        {
            "CODE": "M3UA",
            "GROUP": "T.CARLOS",
            "NAME": "F3H-884",
            "DATETIME": "220506063700"
        },
        {
            "CODE": "M3UH",
            "GROUP": "RENTINLE",
            "NAME": "BHB-501",
            "DATETIME": "220506001212"
        },
        {
            "CODE": "M3US",
            "GROUP": "RIMAC",
            "NAME": "AXB-522",
            "DATETIME": "220506082633"
        },
        {
            "CODE": "M3UW",
            "GROUP": "T.CARLOS",
            "NAME": "B5Z-884",
            "DATETIME": "220506114333"
        },
        {
            "CODE": "M3ZV",
            "GROUP": "RENTINLE",
            "NAME": "BLM-097",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "M3ZZ",
            "GROUP": "BELLASUR",
            "NAME": "ASK-796",
            "DATETIME": "220506115851"
        },
        {
            "CODE": "M404",
            "GROUP": "BELLASUR",
            "NAME": "C6I-948",
            "DATETIME": "220505170454"
        },
        {
            "CODE": "M406",
            "GROUP": "RENTING",
            "NAME": "AXX-743",
            "DATETIME": "220506082715"
        },
        {
            "CODE": "M40H",
            "GROUP": "THEM",
            "NAME": "T4E-836",
            "DATETIME": "220506093600"
        },
        {
            "CODE": "M41Q",
            "GROUP": "POSITIVA",
            "NAME": "ASH-726",
            "DATETIME": "220505122636"
        },
        {
            "CODE": "M41R",
            "GROUP": "RENTINLE",
            "NAME": "BES-194",
            "DATETIME": "220408102142"
        },
        {
            "CODE": "M41S",
            "GROUP": "LISTOTAX",
            "NAME": "BNG-331",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "M41X",
            "GROUP": "AUTONORT",
            "NAME": "M5Z-764",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "M427",
            "GROUP": "ENERLETR",
            "NAME": "BHY-912",
            "DATETIME": "220506115115"
        },
        {
            "CODE": "M42B",
            "GROUP": "AUTONORT",
            "NAME": "F0J-848",
            "DATETIME": "220506120339"
        },
        {
            "CODE": "M42R",
            "GROUP": "YUCRA",
            "NAME": "V1X-936",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "M42X",
            "GROUP": "STA-ROSA",
            "NAME": "D4R-781",
            "DATETIME": "220506114754"
        },
        {
            "CODE": "M43J",
            "GROUP": "BIDDLE",
            "NAME": "BEA-723",
            "DATETIME": "220506120351"
        },
        {
            "CODE": "M441",
            "GROUP": "PACIFICO",
            "NAME": "APO-374",
            "DATETIME": "220505142748"
        },
        {
            "CODE": "M444",
            "GROUP": "GEMINIS",
            "NAME": "F5E-778",
            "DATETIME": "220406143757"
        },
        {
            "CODE": "M44Y",
            "GROUP": "GILDEMEI",
            "NAME": "AWW-666",
            "DATETIME": "220506090809"
        },
        {
            "CODE": "M451",
            "GROUP": "STA-ROSA",
            "NAME": "AJX-771",
            "DATETIME": "220506102857"
        },
        {
            "CODE": "M457",
            "GROUP": "POSITIVA",
            "NAME": "AWO-405",
            "DATETIME": "220506113424"
        },
        {
            "CODE": "M45C",
            "GROUP": "RIMAC",
            "NAME": "AXX-193",
            "DATETIME": "220505184936"
        },
        {
            "CODE": "M59G",
            "GROUP": "POSITIVA",
            "NAME": "ASO-813",
            "DATETIME": "220506072403"
        },
        {
            "CODE": "M59R",
            "GROUP": "CONDOR.T",
            "NAME": "F1E-968",
            "DATETIME": "220506072215"
        },
        {
            "CODE": "M59V",
            "GROUP": "SHILCAYO",
            "NAME": "BET-809",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "M59Y",
            "GROUP": "GILDEMEI",
            "NAME": "AXH-436",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "M5A0",
            "GROUP": "RENTINLE",
            "NAME": "BLM-100",
            "DATETIME": "220506115400"
        },
        {
            "CODE": "M5A5",
            "GROUP": "GILDEMEI",
            "NAME": "AXL-054",
            "DATETIME": "220506114733"
        },
        {
            "CODE": "M5A7",
            "GROUP": "PART-BET",
            "NAME": "T8V-803",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "M5AG",
            "GROUP": "GILDEMEI",
            "NAME": "AXL-156",
            "DATETIME": "220506075000"
        },
        {
            "CODE": "M5AT",
            "GROUP": "PETROL-C",
            "NAME": "BJV-946",
            "DATETIME": "220506092839"
        },
        {
            "CODE": "M5B3",
            "GROUP": "TICLAVIL",
            "NAME": "C5Q-990",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "M5BY",
            "GROUP": "SANTO DO",
            "NAME": "ATH-738",
            "DATETIME": "220320075003"
        },
        {
            "CODE": "M5C2",
            "GROUP": "VIPAUR",
            "NAME": "T8U-930",
            "DATETIME": "220506061312"
        },
        {
            "CODE": "M5C7",
            "GROUP": "B.AIRES",
            "NAME": "AKX-971",
            "DATETIME": "220505120515"
        },
        {
            "CODE": "M5CC",
            "GROUP": "PRIMERA",
            "NAME": "ASW-911",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "M5CD",
            "GROUP": "LISTOTAX",
            "NAME": "BBA-668",
            "DATETIME": "220506094542"
        },
        {
            "CODE": "M5CZ",
            "GROUP": "RIMAC",
            "NAME": "AXW-543",
            "DATETIME": "220505204154"
        },
        {
            "CODE": "M5D1",
            "GROUP": "LISTOTAX",
            "NAME": "BXM-650",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "M5D7",
            "GROUP": "MORALES",
            "NAME": "D2W-789",
            "DATETIME": "220506120315"
        },
        {
            "CODE": "M5DE",
            "GROUP": "YUCRA",
            "NAME": "VAU-911",
            "DATETIME": "220506114857"
        },
        {
            "CODE": "M5DK",
            "GROUP": "SOLHYM",
            "NAME": "BBM-939",
            "DATETIME": "220506120300"
        },
        {
            "CODE": "M5E0",
            "GROUP": "PORRAS",
            "NAME": "BDY-719",
            "DATETIME": "220506115645"
        },
        {
            "CODE": "M5E8",
            "GROUP": "MAFISA",
            "NAME": "ATF-932",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "M5EC",
            "GROUP": "MANT ING",
            "NAME": "ATC-949",
            "DATETIME": "220506114530"
        },
        {
            "CODE": "M5EE",
            "GROUP": "LISTOTAX",
            "NAME": "BNF-036",
            "DATETIME": "220506112712"
        },
        {
            "CODE": "M5EK",
            "GROUP": "YUCRA",
            "NAME": "V9T-728",
            "DATETIME": "220506114727"
        },
        {
            "CODE": "M5J6",
            "GROUP": "AUTONORT",
            "NAME": "T4J-435",
            "DATETIME": "220506011000"
        },
        {
            "CODE": "M5JE",
            "GROUP": "LISTOTAX",
            "NAME": "BLB-684",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "M5K0",
            "GROUP": "POSITIVA",
            "NAME": "AXO-126",
            "DATETIME": "220506073642"
        },
        {
            "CODE": "M5K7",
            "GROUP": "B VISTA",
            "NAME": "V9F-872",
            "DATETIME": "220506120348"
        },
        {
            "CODE": "M5KE",
            "GROUP": "GILDEMEI",
            "NAME": "AXT-051",
            "DATETIME": "220505180927"
        },
        {
            "CODE": "M5KJ",
            "GROUP": "FAMESA",
            "NAME": "ASZ-847",
            "DATETIME": "220503215824"
        },
        {
            "CODE": "M5KK",
            "GROUP": "TRANSGES",
            "NAME": "AJD-895",
            "DATETIME": "220506120348"
        },
        {
            "CODE": "M5L1",
            "GROUP": "TINOCO",
            "NAME": "BTL-579",
            "DATETIME": "220506090533"
        },
        {
            "CODE": "M5LC",
            "GROUP": "TRANSGES",
            "NAME": "AJD-880",
            "DATETIME": "220506080054"
        },
        {
            "CODE": "M5LG",
            "GROUP": "TRANSGES",
            "NAME": "AJD-924",
            "DATETIME": "220506115530"
        },
        {
            "CODE": "M5LH",
            "GROUP": "TRANSGES",
            "NAME": "AJD-808",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "M5LN",
            "GROUP": "YUCRA",
            "NAME": "V7H-910",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "M5LY",
            "GROUP": "SOLGASAL",
            "NAME": "F6A-986",
            "DATETIME": "220506114815"
        },
        {
            "CODE": "M5LZ",
            "GROUP": "TRANSGES",
            "NAME": "AJE-705",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "M5M6",
            "GROUP": "GILDEMEI",
            "NAME": "AYB-211",
            "DATETIME": "220506090857"
        },
        {
            "CODE": "M5MD",
            "GROUP": "GILDEMEI",
            "NAME": "AXX-656",
            "DATETIME": "220505221245"
        },
        {
            "CODE": "M5MF",
            "GROUP": "LYM",
            "NAME": "BFS-876",
            "DATETIME": "220506113903"
        },
        {
            "CODE": "M5MH",
            "GROUP": "JAIPLAST",
            "NAME": "WGB-592",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "M5ML",
            "GROUP": "GILDEMEI",
            "NAME": "AXY-098",
            "DATETIME": "220222172115"
        },
        {
            "CODE": "M5MN",
            "GROUP": "MINERA T",
            "NAME": "C4Y-774",
            "DATETIME": "220506115739"
        },
        {
            "CODE": "M5MR",
            "GROUP": "TICLAVIL",
            "NAME": "C6V-980",
            "DATETIME": "220304233718"
        },
        {
            "CODE": "M5MW",
            "GROUP": "GREMPOL",
            "NAME": "D9A-990",
            "DATETIME": "220506112006"
        },
        {
            "CODE": "M5N8",
            "GROUP": "LISTOTAX",
            "NAME": "BUC-240",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "M5N9",
            "GROUP": "MAFISA",
            "NAME": "BHA-777",
            "DATETIME": "220506110206"
        },
        {
            "CODE": "M5NB",
            "GROUP": "SHILCAYO",
            "NAME": "ABZ-988",
            "DATETIME": "220506120409"
        },
        {
            "CODE": "M5NC",
            "GROUP": "LISTOTAX",
            "NAME": "BNG-515",
            "DATETIME": "220506115212"
        },
        {
            "CODE": "M5NF",
            "GROUP": "GILDEMEI",
            "NAME": "AXV-578",
            "DATETIME": "220505214024"
        },
        {
            "CODE": "M5NN",
            "GROUP": "NOR OIL",
            "NAME": "T8C-869",
            "DATETIME": "220506120306"
        },
        {
            "CODE": "M5NP",
            "GROUP": "YUCRA",
            "NAME": "V5K-867",
            "DATETIME": "220506115915"
        },
        {
            "CODE": "M5NS",
            "GROUP": "AUTONORT",
            "NAME": "H2C-196",
            "DATETIME": "220506104618"
        },
        {
            "CODE": "M5NY",
            "GROUP": "GILDEMEI",
            "NAME": "AXW-167",
            "DATETIME": "220129072951"
        },
        {
            "CODE": "M5PQ",
            "GROUP": "INTERAME",
            "NAME": "H3A-642",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "M5QP",
            "GROUP": "SHILCAYO",
            "NAME": "ABZ-989",
            "DATETIME": "220506111048"
        },
        {
            "CODE": "M5QW",
            "GROUP": "BERTASOL",
            "NAME": "C5M-795",
            "DATETIME": "220504032109"
        },
        {
            "CODE": "M5QY",
            "GROUP": "RENTINLE",
            "NAME": "BHA-689",
            "DATETIME": "220506115509"
        },
        {
            "CODE": "M5R8",
            "GROUP": "DEMO",
            "NAME": "H2Z-697",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "M5RG",
            "GROUP": "COMASUR",
            "NAME": "D3T-816",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "M5RH",
            "GROUP": "RENTINLE",
            "NAME": "BLL-345",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "M5RL",
            "GROUP": "AUTONORT",
            "NAME": "H3B-633",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "M5RZ",
            "GROUP": "LISTOTAX",
            "NAME": "BWV-462",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "M5SE",
            "GROUP": "A&S OPER",
            "NAME": "DOÑASOCO",
            "DATETIME": "220506084603"
        },
        {
            "CODE": "M5SM",
            "GROUP": "GILDEMEI",
            "NAME": "AXM-409",
            "DATETIME": "220506090942"
        },
        {
            "CODE": "M5SN",
            "GROUP": "MORALES",
            "NAME": "AHJ-723",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "M5SX",
            "GROUP": "TS.MULTI",
            "NAME": "F2G-825",
            "DATETIME": "220506114336"
        },
        {
            "CODE": "M70D",
            "GROUP": "INTI",
            "NAME": "F4L-984",
            "DATETIME": "220506114309"
        },
        {
            "CODE": "M70F",
            "GROUP": "ADUANDIN",
            "NAME": "AWX-907",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "M8CM",
            "GROUP": "ENERLETR",
            "NAME": "W5R-807",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "M8CR",
            "GROUP": "ENERLETR",
            "NAME": "AWK-719",
            "DATETIME": "220506101230"
        },
        {
            "CODE": "M8CS",
            "GROUP": "ENERLETR",
            "NAME": "W5R-816",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "M8CW",
            "GROUP": "ENERLETR",
            "NAME": "AWJ-752",
            "DATETIME": "220506102648"
        },
        {
            "CODE": "M8D3",
            "GROUP": "ENERLETR",
            "NAME": "W5R-806",
            "DATETIME": "220506120106"
        },
        {
            "CODE": "M8D6",
            "GROUP": "ENERLETR",
            "NAME": "AWK-717",
            "DATETIME": "220506115948"
        },
        {
            "CODE": "M8D7",
            "GROUP": "ENERLETR",
            "NAME": "AWJ-822",
            "DATETIME": "220506102124"
        },
        {
            "CODE": "M8DA",
            "GROUP": "RENTING",
            "NAME": "AXX-906",
            "DATETIME": "220506111445"
        },
        {
            "CODE": "M8DK",
            "GROUP": "AUTONORT",
            "NAME": "T4N-231",
            "DATETIME": "220506115924"
        },
        {
            "CODE": "M8DV",
            "GROUP": "LISTOTAX",
            "NAME": "BNG-223",
            "DATETIME": "220506104945"
        },
        {
            "CODE": "M8E7",
            "GROUP": "CORMEI",
            "NAME": "ANA-874",
            "DATETIME": "220506070318"
        },
        {
            "CODE": "M8EC",
            "GROUP": "AUTONORT",
            "NAME": "T8S-816",
            "DATETIME": "220506115324"
        },
        {
            "CODE": "M8ED",
            "GROUP": "STA-ROSA",
            "NAME": "B0A-988",
            "DATETIME": "220506105542"
        },
        {
            "CODE": "M8EJ",
            "GROUP": "RENTING",
            "NAME": "AXW-897",
            "DATETIME": "220506110048"
        },
        {
            "CODE": "M8F7",
            "GROUP": "GILDEMEI",
            "NAME": "AYI-579",
            "DATETIME": "220505133118"
        },
        {
            "CODE": "M8FB",
            "GROUP": "GILDEMEI",
            "NAME": "AXO-012",
            "DATETIME": "220505223045"
        },
        {
            "CODE": "M8FH",
            "GROUP": "PART BET",
            "NAME": "AYM-528",
            "DATETIME": "220506120151"
        },
        {
            "CODE": "M8FU",
            "GROUP": "GILDEMEI",
            "NAME": "AYR-548",
            "DATETIME": "220506081118"
        },
        {
            "CODE": "M8G2",
            "GROUP": "VILLANUE",
            "NAME": "AYS-261",
            "DATETIME": "220506110015"
        },
        {
            "CODE": "M8G6",
            "GROUP": "GEMEVA",
            "NAME": "T9B-845",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "M8G8",
            "GROUP": "GILDEMEI",
            "NAME": "AYU-612",
            "DATETIME": "220506085851"
        },
        {
            "CODE": "M8GA",
            "GROUP": "ESPIBAS",
            "NAME": "W3K-993",
            "DATETIME": "220506120318"
        },
        {
            "CODE": "M8GM",
            "GROUP": "POSITIVA",
            "NAME": "H2R-873",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "M8GQ",
            "GROUP": "MAPFRE",
            "NAME": "AYT-646",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "M8GV",
            "GROUP": "PART BET",
            "NAME": "Y1W-089",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "M8HJ",
            "GROUP": "RIMAC",
            "NAME": "AYO-511",
            "DATETIME": "220505184339"
        },
        {
            "CODE": "M8HK",
            "GROUP": "RIMAC",
            "NAME": "AYR-011",
            "DATETIME": "220505212706"
        },
        {
            "CODE": "M8HX",
            "GROUP": "AUTONORT",
            "NAME": "T4K-535",
            "DATETIME": "220506111830"
        },
        {
            "CODE": "M8J9",
            "GROUP": "IMPROVEK",
            "NAME": "AYE-017",
            "DATETIME": "220505221939"
        },
        {
            "CODE": "M8JH",
            "GROUP": "REPARTO",
            "NAME": "AYW-729",
            "DATETIME": "220506054027"
        },
        {
            "CODE": "M8JP",
            "GROUP": "A&J",
            "NAME": "ANF-823",
            "DATETIME": "220506115354"
        },
        {
            "CODE": "M8JU",
            "GROUP": "A&J",
            "NAME": "ANF-942",
            "DATETIME": "220506120015"
        },
        {
            "CODE": "M8K4",
            "GROUP": "MAPFRE",
            "NAME": "ATD-809",
            "DATETIME": "220505140536"
        },
        {
            "CODE": "M8KA",
            "GROUP": "SAN MART",
            "NAME": "B0E-708",
            "DATETIME": "220506120224"
        },
        {
            "CODE": "M8KB",
            "GROUP": "GILDEMEI",
            "NAME": "AYW-084",
            "DATETIME": "220505214827"
        },
        {
            "CODE": "M8KU",
            "GROUP": "SHILCAYO",
            "NAME": "ASW-928",
            "DATETIME": "220506094318"
        },
        {
            "CODE": "M8KZ",
            "GROUP": "MORALES",
            "NAME": "ATB-918",
            "DATETIME": "220506120212"
        },
        {
            "CODE": "M8L0",
            "GROUP": "MORALES",
            "NAME": "ATB-808",
            "DATETIME": "220506114712"
        },
        {
            "CODE": "M8L1",
            "GROUP": "STA ANA",
            "NAME": "F0Z-989",
            "DATETIME": "220506115436"
        },
        {
            "CODE": "M8L2",
            "GROUP": "SAN MART",
            "NAME": "D4G-865",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "M8L5",
            "GROUP": "MORALES ",
            "NAME": "ATC-788",
            "DATETIME": "220506113827"
        },
        {
            "CODE": "M8L7",
            "GROUP": "SHILCAYO",
            "NAME": "ASU-709",
            "DATETIME": "220506111906"
        },
        {
            "CODE": "M8L9",
            "GROUP": "MORALES",
            "NAME": "ATB-938",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "M8LB",
            "GROUP": "LOSTAUNA",
            "NAME": "BAE-169",
            "DATETIME": "220506120103"
        },
        {
            "CODE": "M8LN",
            "GROUP": "COMASUR",
            "NAME": "C4B-848",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "M8M4",
            "GROUP": "ENERLETR",
            "NAME": "AWJ-886",
            "DATETIME": "220505123936"
        },
        {
            "CODE": "M8MF",
            "GROUP": "GILDEMEI",
            "NAME": "AYD-421",
            "DATETIME": "220505172700"
        },
        {
            "CODE": "M8MS",
            "GROUP": "GILDEMEI",
            "NAME": "AYK-087",
            "DATETIME": "220505175433"
        },
        {
            "CODE": "M8NN",
            "GROUP": "GILDEMEI",
            "NAME": "AYU-319",
            "DATETIME": "220506112515"
        },
        {
            "CODE": "M8NX",
            "GROUP": "TICLAVIL",
            "NAME": "F9R-981",
            "DATETIME": "220506085739"
        },
        {
            "CODE": "M8NZ",
            "GROUP": "COMASUR",
            "NAME": "D3R-823",
            "DATETIME": "220506115124"
        },
        {
            "CODE": "M8P7",
            "GROUP": "SAN MART",
            "NAME": "F8G-810",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "M8PC",
            "GROUP": "COMASUR",
            "NAME": "D6Q-757",
            "DATETIME": "220502175827"
        },
        {
            "CODE": "M8PM",
            "GROUP": "G.GEMEVA",
            "NAME": "T3O-921",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "M8PV",
            "GROUP": "GILDEMEI",
            "NAME": "AYI-343",
            "DATETIME": "220506084515"
        },
        {
            "CODE": "M8Q1",
            "GROUP": "RENTING",
            "NAME": "AWC-854",
            "DATETIME": "220506111148"
        },
        {
            "CODE": "M8Q5",
            "GROUP": "GILDEMEI",
            "NAME": "BCU-305",
            "DATETIME": "220505160836"
        },
        {
            "CODE": "M8Q7",
            "GROUP": "AUTONORT",
            "NAME": "ASR-826",
            "DATETIME": "220505161412"
        },
        {
            "CODE": "M8QD",
            "GROUP": "RIMAC ",
            "NAME": "AYH-385",
            "DATETIME": "220505192306"
        },
        {
            "CODE": "M8QE",
            "GROUP": "GILDEMEI",
            "NAME": "AYM-259",
            "DATETIME": "220505185336"
        },
        {
            "CODE": "M8R5",
            "GROUP": "SUEROS",
            "NAME": "V9H-899",
            "DATETIME": "220506103957"
        },
        {
            "CODE": "M8RN",
            "GROUP": "SUEROS",
            "NAME": "V9J-938",
            "DATETIME": "220506093339"
        },
        {
            "CODE": "M8S7",
            "GROUP": "RENTING",
            "NAME": "AYN-839",
            "DATETIME": "220417182342"
        },
        {
            "CODE": "M8SB",
            "GROUP": "RIMAC",
            "NAME": "AYO-616",
            "DATETIME": "220505210251"
        },
        {
            "CODE": "M8SJ",
            "GROUP": "MORALES",
            "NAME": "AHI-941",
            "DATETIME": "220506120203"
        },
        {
            "CODE": "M8YF",
            "GROUP": "T.SANTAM",
            "NAME": "D8T-806",
            "DATETIME": "220506085351"
        },
        {
            "CODE": "M8YG",
            "GROUP": "T.SANTAM",
            "NAME": "D8T-853",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "M8YM",
            "GROUP": "STA-ROSA",
            "NAME": "D1D-823",
            "DATETIME": "220505162548"
        },
        {
            "CODE": "M8YR",
            "GROUP": "RENTINLE",
            "NAME": "BLL-660",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "M8YY",
            "GROUP": "MINCO",
            "NAME": "AVG-822",
            "DATETIME": "220422130621"
        },
        {
            "CODE": "M8ZY",
            "GROUP": "MYI GLO",
            "NAME": "A2G-831",
            "DATETIME": "220506114242"
        },
        {
            "CODE": "M902",
            "GROUP": "MOVILGAS",
            "NAME": "AYJ-879",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "M90A",
            "GROUP": "TICLAVIL",
            "NAME": "F7G-975",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "M90B",
            "GROUP": "ALCOHOL",
            "NAME": "BBN-167",
            "DATETIME": "220505163142"
        },
        {
            "CODE": "M90G",
            "GROUP": "MAFISA",
            "NAME": "ATF-929",
            "DATETIME": "220410071512"
        },
        {
            "CODE": "M90R",
            "GROUP": "JM PANDU",
            "NAME": "A9E-936",
            "DATETIME": "220506115036"
        },
        {
            "CODE": "M91G",
            "GROUP": "FAMESA",
            "NAME": "AUQ-832",
            "DATETIME": "220503101751"
        },
        {
            "CODE": "M91L",
            "GROUP": "MORALES",
            "NAME": "F7F-920",
            "DATETIME": "220506120348"
        },
        {
            "CODE": "M91N",
            "GROUP": "YUCRA",
            "NAME": "V3R-932",
            "DATETIME": "220506115215"
        },
        {
            "CODE": "M91X",
            "GROUP": "RIMAC",
            "NAME": "AZL-691",
            "DATETIME": "220430204006"
        },
        {
            "CODE": "M923",
            "GROUP": "FAMESA",
            "NAME": "AUQ-773",
            "DATETIME": "220503215003"
        },
        {
            "CODE": "M92C",
            "GROUP": "TRCEXPRE",
            "NAME": "T8L-820",
            "DATETIME": "220506115939"
        },
        {
            "CODE": "M92F",
            "GROUP": "MAPFRE",
            "NAME": "AZX-690",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "M92M",
            "GROUP": "LISTOTAX",
            "NAME": "BAQ-045",
            "DATETIME": "220506115730"
        },
        {
            "CODE": "M92Q",
            "GROUP": "LISTOTAX",
            "NAME": "BBB-426",
            "DATETIME": "220506112933"
        },
        {
            "CODE": "M92T",
            "GROUP": "PART-BET",
            "NAME": "D5H-373",
            "DATETIME": "220506111306"
        },
        {
            "CODE": "M935",
            "GROUP": "RIMAC ",
            "NAME": "AZI-658",
            "DATETIME": "220505134712"
        },
        {
            "CODE": "M93K",
            "GROUP": "SAN DIEG",
            "NAME": "AMB-900",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "M93L",
            "GROUP": "GILDEMEI",
            "NAME": "AYZ-613",
            "DATETIME": "220506082354"
        },
        {
            "CODE": "M93P",
            "GROUP": "VILLENA",
            "NAME": "A7Z-806",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "M93T",
            "GROUP": "TRANSEL",
            "NAME": "BSB-042",
            "DATETIME": "220506113415"
        },
        {
            "CODE": "M93X",
            "GROUP": "GILDEMEI",
            "NAME": "AYZ-605",
            "DATETIME": "220506120348"
        },
        {
            "CODE": "M93Z",
            "GROUP": "VILLENA",
            "NAME": "AUF-825",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "M950",
            "GROUP": "GILDEMEI",
            "NAME": "AYS-302",
            "DATETIME": "220506070036"
        },
        {
            "CODE": "M95H",
            "GROUP": "LISTOTAX",
            "NAME": "APL-444",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "M95S",
            "GROUP": "AUTONORT",
            "NAME": "T4M-091",
            "DATETIME": "220506100012"
        },
        {
            "CODE": "M95X",
            "GROUP": "MAPFRE",
            "NAME": "D7J-327",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "M96E",
            "GROUP": "RENTINCA",
            "NAME": "T1R-855",
            "DATETIME": "220506102103"
        },
        {
            "CODE": "M96J",
            "GROUP": "NOR OIL",
            "NAME": "T4O-008",
            "DATETIME": "220506115454"
        },
        {
            "CODE": "M96N",
            "GROUP": "GILDEMEI",
            "NAME": "AZC-611",
            "DATETIME": "220506000409"
        },
        {
            "CODE": "M96P",
            "GROUP": "NOR OIL",
            "NAME": "P2H-736",
            "DATETIME": "220506115542"
        },
        {
            "CODE": "M96Q",
            "GROUP": "POMA",
            "NAME": "A6U-863",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "M96S",
            "GROUP": "GILDEMEI",
            "NAME": "AZD-459",
            "DATETIME": "220506115724"
        },
        {
            "CODE": "M96U",
            "GROUP": "CUPERTIN",
            "NAME": "AXS-497",
            "DATETIME": "220506113709"
        },
        {
            "CODE": "M96W",
            "GROUP": "SOLGASTR",
            "NAME": "F3M-992",
            "DATETIME": "220506120333"
        },
        {
            "CODE": "M96Z",
            "GROUP": "T.CORREA",
            "NAME": "F7I-975",
            "DATETIME": "220506115639"
        },
        {
            "CODE": "M971",
            "GROUP": "SOLGASER",
            "NAME": "C4V-988",
            "DATETIME": "220506120330"
        },
        {
            "CODE": "M973",
            "GROUP": "MORALES",
            "NAME": "F6G-768",
            "DATETIME": "220506115530"
        },
        {
            "CODE": "M975",
            "GROUP": "RENTINCA",
            "NAME": "C1H-777",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "M976",
            "GROUP": "TAXI AH",
            "NAME": "AEM-026",
            "DATETIME": "220506115742"
        },
        {
            "CODE": "M977",
            "GROUP": "T.ZEVALL",
            "NAME": "BJT-752",
            "DATETIME": "220506081442"
        },
        {
            "CODE": "M978",
            "GROUP": "RENTINCA",
            "NAME": "C1C-714",
            "DATETIME": "220506114157"
        },
        {
            "CODE": "M97C",
            "GROUP": "LISTOTAX",
            "NAME": "BLB-501",
            "DATETIME": "220506053921"
        },
        {
            "CODE": "M97N",
            "GROUP": "FAMESA",
            "NAME": "AVG-840",
            "DATETIME": "220505171318"
        },
        {
            "CODE": "M97Y",
            "GROUP": "GEMEVA",
            "NAME": "T5O-811",
            "DATETIME": "220506104645"
        },
        {
            "CODE": "M98B",
            "GROUP": "ROQUE",
            "NAME": "B1Y-941",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "M98R",
            "GROUP": "PROCARGO",
            "NAME": "C7J-829",
            "DATETIME": "220506115709"
        },
        {
            "CODE": "M98S",
            "GROUP": "LISTOTAX",
            "NAME": "BEF-034",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "M991",
            "GROUP": "LISTOTAX",
            "NAME": "BUB-475",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "M992",
            "GROUP": "GILDEMEI",
            "NAME": "AZD-641",
            "DATETIME": "220506111915"
        },
        {
            "CODE": "M994",
            "GROUP": "LISTOTAX",
            "NAME": "BHD-484",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "M99E",
            "GROUP": "SAN MART",
            "NAME": "MO-23",
            "DATETIME": "220506120333"
        },
        {
            "CODE": "M99G",
            "GROUP": "LISTOTAX",
            "NAME": "BNG-179",
            "DATETIME": "220506014754"
        },
        {
            "CODE": "M99M",
            "GROUP": "MAPFRE",
            "NAME": "640014",
            "DATETIME": "220110060221"
        },
        {
            "CODE": "M99T",
            "GROUP": "SHILCAYO",
            "NAME": "ATD-972",
            "DATETIME": "220506115815"
        },
        {
            "CODE": "M99W",
            "GROUP": "LISTOTAX",
            "NAME": "BAO-144",
            "DATETIME": "220506112739"
        },
        {
            "CODE": "M99Y",
            "GROUP": "RENTINCA",
            "NAME": "T6O-922",
            "DATETIME": "220506103200"
        },
        {
            "CODE": "M99Z",
            "GROUP": "NOR OIL",
            "NAME": "T6F-923",
            "DATETIME": "220506104057"
        },
        {
            "CODE": "M9A1",
            "GROUP": "LISTOTAX",
            "NAME": "BMA-356",
            "DATETIME": "220506115727"
        },
        {
            "CODE": "M9A2",
            "GROUP": "LISTO",
            "NAME": "BNF-493",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "M9A5",
            "GROUP": "COMASUR",
            "NAME": "BBR-934",
            "DATETIME": "220506093812"
        },
        {
            "CODE": "M9A6",
            "GROUP": "RIMAC ",
            "NAME": "ATA-200",
            "DATETIME": "220506092706"
        },
        {
            "CODE": "M9A7",
            "GROUP": "RENTINCA",
            "NAME": "C1H-743",
            "DATETIME": "220505214642"
        },
        {
            "CODE": "M9A8",
            "GROUP": "RENTINCA",
            "NAME": "T6O-931",
            "DATETIME": "220506114739"
        },
        {
            "CODE": "M9A9",
            "GROUP": "RENTINCA",
            "NAME": "C4H-709",
            "DATETIME": "220506110330"
        },
        {
            "CODE": "M9AB",
            "GROUP": "SOLGASER",
            "NAME": "B6H-979",
            "DATETIME": "220506112751"
        },
        {
            "CODE": "M9AF",
            "GROUP": "MINERA O",
            "NAME": "AUZ-820",
            "DATETIME": "220506121036"
        },
        {
            "CODE": "M9AJ",
            "GROUP": "MORALES",
            "NAME": "F6G-808",
            "DATETIME": "220506120345"
        },
        {
            "CODE": "M9AM",
            "GROUP": "RENTINCA",
            "NAME": "C4C-728",
            "DATETIME": "220506103806"
        },
        {
            "CODE": "M9AN",
            "GROUP": "RENTINCA",
            "NAME": "C4Y-795",
            "DATETIME": "220427154209"
        },
        {
            "CODE": "M9AS",
            "GROUP": "RENTINCA",
            "NAME": "C5C-764",
            "DATETIME": "220506083730"
        },
        {
            "CODE": "M9AU",
            "GROUP": "LISTOTAX",
            "NAME": "BTP-046",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "M9AV",
            "GROUP": "MYI GLO",
            "NAME": "C9K-928",
            "DATETIME": "220429151251"
        },
        {
            "CODE": "M9AW",
            "GROUP": "LISTOTAX",
            "NAME": "BTM-555",
            "DATETIME": "220506120318"
        },
        {
            "CODE": "M9AX",
            "GROUP": "RENTINCA",
            "NAME": "C1J-773",
            "DATETIME": "220505091824"
        },
        {
            "CODE": "M9AZ",
            "GROUP": "ASZTRANS",
            "NAME": "F0S-823",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "M9B0",
            "GROUP": "ENMANUEL",
            "NAME": "ARC-823",
            "DATETIME": "220506112333"
        },
        {
            "CODE": "M9B2",
            "GROUP": "SLI",
            "NAME": "AFX-915",
            "DATETIME": "220506115657"
        },
        {
            "CODE": "M9B6",
            "GROUP": "RENTINCA",
            "NAME": "T6O-926",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "M9B7",
            "GROUP": "RENTINCA",
            "NAME": "C4V-765",
            "DATETIME": "220505144342"
        },
        {
            "CODE": "M9B9",
            "GROUP": "YEKARE",
            "NAME": "D0A-949",
            "DATETIME": "220506071639"
        },
        {
            "CODE": "M9BB",
            "GROUP": "LISTOTAX",
            "NAME": "BTL-698",
            "DATETIME": "220506120309"
        },
        {
            "CODE": "M9BD",
            "GROUP": "MAPFRE",
            "NAME": "H2C-449",
            "DATETIME": "220505224027"
        },
        {
            "CODE": "M9BG",
            "GROUP": "LISTOTAX",
            "NAME": "BWS-323",
            "DATETIME": "220506104836"
        },
        {
            "CODE": "M9BH",
            "GROUP": "RENTINCA",
            "NAME": "T6O-948",
            "DATETIME": "220506115900"
        },
        {
            "CODE": "M9BM",
            "GROUP": "CALDERON",
            "NAME": "V6O-847",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "M9BP",
            "GROUP": "LISTOTAX",
            "NAME": "BPC-246",
            "DATETIME": "220506120412"
        },
        {
            "CODE": "M9BQ",
            "GROUP": "RENTING",
            "NAME": "AUN-807",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "M9BT",
            "GROUP": "MARTINEZ",
            "NAME": "ANC-902",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "M9BU",
            "GROUP": "YUCRA",
            "NAME": "V8U-710",
            "DATETIME": "220506115939"
        },
        {
            "CODE": "M9BW",
            "GROUP": "AXON",
            "NAME": "A1L-927",
            "DATETIME": "220506115757"
        },
        {
            "CODE": "M9BX",
            "GROUP": "RENTING",
            "NAME": "AUN-794",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "M9BY",
            "GROUP": "ADUANDIN",
            "NAME": "D3E-869",
            "DATETIME": "220505150230"
        },
        {
            "CODE": "M9C2",
            "GROUP": "AXON",
            "NAME": "A7C-920",
            "DATETIME": "220506115515"
        },
        {
            "CODE": "M9C3",
            "GROUP": "RENTING",
            "NAME": "AUN-803",
            "DATETIME": "220506114000"
        },
        {
            "CODE": "M9C4",
            "GROUP": "RENTING",
            "NAME": "AUV-749",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "M9C5",
            "GROUP": "YUCRA",
            "NAME": "V8L-851",
            "DATETIME": "220506115903"
        },
        {
            "CODE": "M9C7",
            "GROUP": "RENTINCA",
            "NAME": "T6O-917",
            "DATETIME": "220505161639"
        },
        {
            "CODE": "M9C8",
            "GROUP": "RAVELO",
            "NAME": "A3N-928",
            "DATETIME": "220505153348"
        },
        {
            "CODE": "M9CA",
            "GROUP": "VILLENA",
            "NAME": "AUF-842",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "MA8P",
            "GROUP": "T. WILL",
            "NAME": "BFY-769",
            "DATETIME": "220417101130"
        },
        {
            "CODE": "MA9U",
            "GROUP": "GILDEMEI",
            "NAME": "BBX-279",
            "DATETIME": "220506083724"
        },
        {
            "CODE": "MA9V",
            "GROUP": "INTI ",
            "NAME": "ANX-775",
            "DATETIME": "220506115236"
        },
        {
            "CODE": "MAA2",
            "GROUP": "AGREVO",
            "NAME": "AWB-751",
            "DATETIME": "220506114000"
        },
        {
            "CODE": "MATZ",
            "GROUP": "GILDEMEI",
            "NAME": "BAD-218",
            "DATETIME": "220506085103"
        },
        {
            "CODE": "MAUB",
            "GROUP": "RIMAC",
            "NAME": "BAC-020",
            "DATETIME": "220506115912"
        },
        {
            "CODE": "MAUH",
            "GROUP": "GILDEMEI",
            "NAME": "BAH-313",
            "DATETIME": "220505220709"
        },
        {
            "CODE": "MAUY",
            "GROUP": "GILDEMEI",
            "NAME": "BAD-622",
            "DATETIME": "220505194345"
        },
        {
            "CODE": "MAV0",
            "GROUP": "GILDEMEI",
            "NAME": "BAH-042",
            "DATETIME": "220506113218"
        },
        {
            "CODE": "MAV7",
            "GROUP": "BIDDLE",
            "NAME": "C5R-700",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "MAVG",
            "GROUP": "ESPAR",
            "NAME": "AZY-663",
            "DATETIME": "220506083733"
        },
        {
            "CODE": "MAVP",
            "GROUP": "PASQUEL",
            "NAME": "BBF-027",
            "DATETIME": "220506120057"
        },
        {
            "CODE": "MAVU",
            "GROUP": "GILDEMEI",
            "NAME": "BAC-565",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "MAVW",
            "GROUP": "GILDEMEI",
            "NAME": "BAF-320",
            "DATETIME": "220506114306"
        },
        {
            "CODE": "MAXB",
            "GROUP": "STA-ROSA",
            "NAME": "ADY-709 ",
            "DATETIME": "220506114518"
        },
        {
            "CODE": "MAXH",
            "GROUP": "T.FLORES",
            "NAME": "C8R-937",
            "DATETIME": "220506102545"
        },
        {
            "CODE": "MAXV",
            "GROUP": "RIMAC",
            "NAME": "AZS-677",
            "DATETIME": "220506073021"
        },
        {
            "CODE": "MAXY",
            "GROUP": "T.FLORES",
            "NAME": "C9I-942",
            "DATETIME": "220503202339"
        },
        {
            "CODE": "MAYB",
            "GROUP": "RIMAC",
            "NAME": "BAE-411",
            "DATETIME": "220506113206"
        },
        {
            "CODE": "MAYC",
            "GROUP": "MORAN",
            "NAME": "D2R-881",
            "DATETIME": "220506120345"
        },
        {
            "CODE": "MAYD",
            "GROUP": "TCARRANZ",
            "NAME": "B6I-764",
            "DATETIME": "220302192333"
        },
        {
            "CODE": "MAYF",
            "GROUP": "GILDEMEI",
            "NAME": "AZW-285",
            "DATETIME": "220506002136"
        },
        {
            "CODE": "MAYH",
            "GROUP": "RIMAC ",
            "NAME": "BAF-489",
            "DATETIME": "220506103157"
        },
        {
            "CODE": "MAYM",
            "GROUP": "GILDEMEI",
            "NAME": "AZZ-313",
            "DATETIME": "220505222336"
        },
        {
            "CODE": "MAZ5",
            "GROUP": "NETZSCH",
            "NAME": "ASR-287",
            "DATETIME": "220505190709"
        },
        {
            "CODE": "MAZ6",
            "GROUP": "NETZSCH",
            "NAME": "F5Y-232",
            "DATETIME": "220504171745"
        },
        {
            "CODE": "MAZA",
            "GROUP": "MAPFRE",
            "NAME": "AZT-598",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "MAZC",
            "GROUP": "GILDEMEI",
            "NAME": "AZW-069",
            "DATETIME": "220506084530"
        },
        {
            "CODE": "MAZL",
            "GROUP": "STA-ROSA",
            "NAME": "AWV-925",
            "DATETIME": "220506120351"
        },
        {
            "CODE": "MAZP",
            "GROUP": "MARYORIC",
            "NAME": "AZZ-439",
            "DATETIME": "220505180212"
        },
        {
            "CODE": "MB0J",
            "GROUP": "RENTING",
            "NAME": "AZF-766",
            "DATETIME": "220506115318"
        },
        {
            "CODE": "MB1A",
            "GROUP": "BONALIS",
            "NAME": "B9V-858",
            "DATETIME": "220506120042"
        },
        {
            "CODE": "MB1M",
            "GROUP": "AUTONORT",
            "NAME": "H3D-617",
            "DATETIME": "220506120242"
        },
        {
            "CODE": "MB1Q",
            "GROUP": "GARCIA",
            "NAME": "AKA-868",
            "DATETIME": "220504143606"
        },
        {
            "CODE": "MB1W",
            "GROUP": "RENTING",
            "NAME": "AUO-920",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "MB1Y",
            "GROUP": "GILDEMEI",
            "NAME": "AZU-358",
            "DATETIME": "220506104318"
        },
        {
            "CODE": "MB23",
            "GROUP": "GILDEMEI",
            "NAME": "AZX-456",
            "DATETIME": "220505164200"
        },
        {
            "CODE": "MB24",
            "GROUP": "GILDEMEI",
            "NAME": "AZS-193",
            "DATETIME": "220505173915"
        },
        {
            "CODE": "MB2A",
            "GROUP": "NAVARRO",
            "NAME": "B5E-920",
            "DATETIME": "220506120248"
        },
        {
            "CODE": "MB2C",
            "GROUP": "RENTING",
            "NAME": "AUP-744",
            "DATETIME": "220506120351"
        },
        {
            "CODE": "MB2S",
            "GROUP": "GEMEVA",
            "NAME": "C7P-882",
            "DATETIME": "220506115748"
        },
        {
            "CODE": "MB2T",
            "GROUP": "RENTING",
            "NAME": "AZL-017",
            "DATETIME": "220506095648"
        },
        {
            "CODE": "MB2U",
            "GROUP": "POWERBLU",
            "NAME": "T1F-835",
            "DATETIME": "220506120109"
        },
        {
            "CODE": "MB2V",
            "GROUP": "FERREYRO",
            "NAME": "26026",
            "DATETIME": "220506120233"
        },
        {
            "CODE": "MB2X",
            "GROUP": "RENTING",
            "NAME": "BER-175",
            "DATETIME": "220411102948"
        },
        {
            "CODE": "MB2Y",
            "GROUP": "T.WEIGHT",
            "NAME": "BTE-585",
            "DATETIME": "220506120221"
        },
        {
            "CODE": "MB34",
            "GROUP": "GEMEVA",
            "NAME": "T7F-915",
            "DATETIME": "220506115842"
        },
        {
            "CODE": "MB37",
            "GROUP": "PART BET",
            "NAME": "BFM-766",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "MB3B",
            "GROUP": "TRANSGES",
            "NAME": "A8E-838",
            "DATETIME": "220506104130"
        },
        {
            "CODE": "MB3J",
            "GROUP": "LINCUNA",
            "NAME": "AHN-701",
            "DATETIME": "220506120324"
        },
        {
            "CODE": "MB48",
            "GROUP": "TRUCKTIR",
            "NAME": "AVW-942",
            "DATETIME": "220505161515"
        },
        {
            "CODE": "MB49",
            "GROUP": "LOAYZA",
            "NAME": "BDL-754",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "MB4H",
            "GROUP": "GRAMA",
            "NAME": "4298-BB",
            "DATETIME": "220506120257"
        },
        {
            "CODE": "MB4T",
            "GROUP": "MAPFRE",
            "NAME": "AZI-405",
            "DATETIME": "220506115945"
        },
        {
            "CODE": "MB4Y",
            "GROUP": "JDM",
            "NAME": "V8L-900",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "MB5L",
            "GROUP": "RIMAC",
            "NAME": "AZS-397",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "MB5P",
            "GROUP": "RIMAC",
            "NAME": "AZN-623",
            "DATETIME": "220505165618"
        },
        {
            "CODE": "MB5V",
            "GROUP": "T.SANTOS",
            "NAME": "AHJ-938",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "MB5Z",
            "GROUP": "TRABAJA ",
            "NAME": "EGZ-029",
            "DATETIME": "220505193527"
        },
        {
            "CODE": "MB6D",
            "GROUP": "TRABAJA",
            "NAME": "EGZ-026",
            "DATETIME": "220506114000"
        },
        {
            "CODE": "MB6S",
            "GROUP": "CABALLER",
            "NAME": "TAD-946",
            "DATETIME": "220506061609"
        },
        {
            "CODE": "MB6T",
            "GROUP": "GILDEMEI",
            "NAME": "AZO-255",
            "DATETIME": "220505212027"
        },
        {
            "CODE": "MB70",
            "GROUP": "ESPAR",
            "NAME": "BJE-819",
            "DATETIME": "220506120033"
        },
        {
            "CODE": "MB79",
            "GROUP": "GILDEMEI",
            "NAME": "AZS-487",
            "DATETIME": "220505221542"
        },
        {
            "CODE": "MB7D",
            "GROUP": "PACIFICO",
            "NAME": "F9Y-275",
            "DATETIME": "220506105857"
        },
        {
            "CODE": "MB7M",
            "GROUP": "SOBERON",
            "NAME": "AZM-319",
            "DATETIME": "220506092930"
        },
        {
            "CODE": "MB7V",
            "GROUP": "PART BET",
            "NAME": "BTS-024",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "MB7W",
            "GROUP": "CABALLER",
            "NAME": "TAB-914",
            "DATETIME": "220506120400"
        },
        {
            "CODE": "MB84",
            "GROUP": "ALCIDESF",
            "NAME": "BCC-201",
            "DATETIME": "220506112845"
        },
        {
            "CODE": "MB87",
            "GROUP": "POSITIVA",
            "NAME": "AZH-186",
            "DATETIME": "220506104936"
        },
        {
            "CODE": "MB8H",
            "GROUP": "GILDEMEI",
            "NAME": "AZT-302",
            "DATETIME": "220506084551"
        },
        {
            "CODE": "MB8K",
            "GROUP": "T.HILDA",
            "NAME": "B7N-928",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "MB8L",
            "GROUP": "RENTING",
            "NAME": "AUN-712",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "MB9C",
            "GROUP": "FAMESA",
            "NAME": "AVH-867",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "MB9F",
            "GROUP": "GILDEMEI",
            "NAME": "BAZ-050",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "MB9K",
            "GROUP": "SALUD",
            "NAME": "EUD-177",
            "DATETIME": "220506080009"
        },
        {
            "CODE": "MB9U",
            "GROUP": "GILDEMEI",
            "NAME": "BBG-434",
            "DATETIME": "220506090706"
        },
        {
            "CODE": "MB9X",
            "GROUP": "GILDEMEI",
            "NAME": "BAV-346",
            "DATETIME": "220505174603"
        },
        {
            "CODE": "MBAN",
            "GROUP": "CASTRO",
            "NAME": "F9S-599",
            "DATETIME": "220506120303"
        },
        {
            "CODE": "MBAS",
            "GROUP": "FERREYRO",
            "NAME": "21017",
            "DATETIME": "220506120403"
        },
        {
            "CODE": "MBBF",
            "GROUP": "BASILIO",
            "NAME": "ADS-921",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "MBBV",
            "GROUP": "PACIFICO",
            "NAME": "BAO-192",
            "DATETIME": "220505230936"
        },
        {
            "CODE": "MBBX",
            "GROUP": "GILDEMEI",
            "NAME": "BAW-414",
            "DATETIME": "220506094315"
        },
        {
            "CODE": "MBC1",
            "GROUP": "SSAT",
            "NAME": "2725-0C",
            "DATETIME": "220506112518"
        },
        {
            "CODE": "MBC7",
            "GROUP": "PART BET",
            "NAME": "BAU-015",
            "DATETIME": "220506120115"
        },
        {
            "CODE": "MBCG",
            "GROUP": "GILDEMEI",
            "NAME": "AVJ-904",
            "DATETIME": "220418152230"
        },
        {
            "CODE": "MBCR",
            "GROUP": "GILDEMEI",
            "NAME": "BAY-285",
            "DATETIME": "220506082806"
        },
        {
            "CODE": "MBCZ",
            "GROUP": "GILDEMEI",
            "NAME": "BBD-430",
            "DATETIME": "220506025515"
        },
        {
            "CODE": "MBDA",
            "GROUP": "RIMAC",
            "NAME": "BAU-250",
            "DATETIME": "220506073327"
        },
        {
            "CODE": "MBDM",
            "GROUP": "MAPFRE",
            "NAME": "BAU-234",
            "DATETIME": "220506115239"
        },
        {
            "CODE": "MBDQ",
            "GROUP": "RIMAC",
            "NAME": "BCH-607",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "MBDR",
            "GROUP": "LINCUNA",
            "NAME": "AHM-929",
            "DATETIME": "220317163006"
        },
        {
            "CODE": "MBES",
            "GROUP": "PORTALES",
            "NAME": "AVH-801",
            "DATETIME": "220506105309"
        },
        {
            "CODE": "MBEX",
            "GROUP": "AGREVO",
            "NAME": "AVH-837",
            "DATETIME": "220409043315"
        },
        {
            "CODE": "MBFF",
            "GROUP": "RENTING",
            "NAME": "BEY-596",
            "DATETIME": "220506093245"
        },
        {
            "CODE": "MBFY",
            "GROUP": "GILDEMEI",
            "NAME": "BAT-386",
            "DATETIME": "220506115351"
        },
        {
            "CODE": "MBGG",
            "GROUP": "T.WDJC",
            "NAME": "D1U-835",
            "DATETIME": "220506120036"
        },
        {
            "CODE": "MBGV",
            "GROUP": "DELGADO",
            "NAME": "C2E-906",
            "DATETIME": "220322114812"
        },
        {
            "CODE": "MBH0",
            "GROUP": "NT MARKE",
            "NAME": "BTY-399",
            "DATETIME": "220504121015"
        },
        {
            "CODE": "MBHB",
            "GROUP": "GILDEMEI",
            "NAME": "BAR-470",
            "DATETIME": "220505132612"
        },
        {
            "CODE": "MBHJ",
            "GROUP": "RIMAC",
            "NAME": "BAO-204",
            "DATETIME": "220506120206"
        },
        {
            "CODE": "MBHT",
            "GROUP": "GILDEMEI",
            "NAME": "BAR-258",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "MBHV",
            "GROUP": "GILDEMEI",
            "NAME": "BAP-405",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "MBJ0",
            "GROUP": "LAN XING",
            "NAME": "BDC-038",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "MBJ9",
            "GROUP": "GILDEMEI",
            "NAME": "BAK-569",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "MBJE",
            "GROUP": "S&R",
            "NAME": "ASQ-871",
            "DATETIME": "220506120206"
        },
        {
            "CODE": "MBJL",
            "GROUP": "RIMAC",
            "NAME": "T4N-176",
            "DATETIME": "220505223312"
        },
        {
            "CODE": "MBJP",
            "GROUP": "MAPFRE",
            "NAME": "AVO-576",
            "DATETIME": "220506115551"
        },
        {
            "CODE": "MBKB",
            "GROUP": "RIMAC",
            "NAME": "BAJ-480",
            "DATETIME": "220506113430"
        },
        {
            "CODE": "MBKD",
            "GROUP": "GILDEMEI",
            "NAME": "AUY-861",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "MBKR",
            "GROUP": "PART-BET",
            "NAME": "BAN-214",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "MBKT",
            "GROUP": "RIMAC",
            "NAME": "BAO-295",
            "DATETIME": "220506114127"
        },
        {
            "CODE": "MBL5",
            "GROUP": "T.FLORES",
            "NAME": "C1R-929",
            "DATETIME": "220505104245"
        },
        {
            "CODE": "MBLA",
            "GROUP": "GILDEMEI",
            "NAME": "BAI-339",
            "DATETIME": "220506114615"
        },
        {
            "CODE": "MBLE",
            "GROUP": "GILDEMEI",
            "NAME": "BAM-260",
            "DATETIME": "220505174357"
        },
        {
            "CODE": "MBLN",
            "GROUP": "MAPFRE",
            "NAME": "BUS-203",
            "DATETIME": "220506113327"
        },
        {
            "CODE": "MBLX",
            "GROUP": "PORTALES",
            "NAME": "AUW-834",
            "DATETIME": "220506120527"
        },
        {
            "CODE": "MBMD",
            "GROUP": "RIMAC",
            "NAME": "123220",
            "DATETIME": "220506095224"
        },
        {
            "CODE": "MBMG",
            "GROUP": "RENTING",
            "NAME": "BAM-225",
            "DATETIME": "220506093006"
        },
        {
            "CODE": "MBNG",
            "GROUP": "RENTING",
            "NAME": "BEW-573",
            "DATETIME": "220506110145"
        },
        {
            "CODE": "MBQ6",
            "GROUP": "TICLAVIL",
            "NAME": "AKX-970",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "MBQB",
            "GROUP": "INTI",
            "NAME": "V3F-739",
            "DATETIME": "220506114215"
        },
        {
            "CODE": "MBQK",
            "GROUP": "INTI",
            "NAME": "C3W-970",
            "DATETIME": "220506114512"
        },
        {
            "CODE": "MBQL",
            "GROUP": "RIMAC",
            "NAME": "AVJ-923",
            "DATETIME": "220506112257"
        },
        {
            "CODE": "MBQP",
            "GROUP": "INTI",
            "NAME": "AAD-985",
            "DATETIME": "220506114227"
        },
        {
            "CODE": "MBQZ",
            "GROUP": "INTI",
            "NAME": "ANY-903",
            "DATETIME": "220506083630"
        },
        {
            "CODE": "MHEL",
            "GROUP": "GILDEMEI",
            "NAME": "BBT-422",
            "DATETIME": "220505142945"
        },
        {
            "CODE": "MHEQ",
            "GROUP": "GRAMA",
            "NAME": "0396-JB",
            "DATETIME": "220506082221"
        },
        {
            "CODE": "MHEY",
            "GROUP": "RENTING",
            "NAME": "AZJ-899",
            "DATETIME": "220506113327"
        },
        {
            "CODE": "MHEZ",
            "GROUP": "AUTONORT",
            "NAME": "T9F-802",
            "DATETIME": "220505183836"
        },
        {
            "CODE": "MHFG",
            "GROUP": "AGAD OL",
            "NAME": "AMI-867",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "MHFH",
            "GROUP": "SHILCAYO",
            "NAME": "ASY-824",
            "DATETIME": "220505175621"
        },
        {
            "CODE": "MHFJ",
            "GROUP": "TAXI AH",
            "NAME": "BLC-398",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "MHFK",
            "GROUP": "PART BET",
            "NAME": "M3X-701",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "MHFL",
            "GROUP": "TRADESUR",
            "NAME": "BHP-861",
            "DATETIME": "220506120239"
        },
        {
            "CODE": "MHFN",
            "GROUP": "GILDEMEI",
            "NAME": "BBW-536",
            "DATETIME": "220505232030"
        },
        {
            "CODE": "MHFU",
            "GROUP": "PACIFICO",
            "NAME": "AUU-625",
            "DATETIME": "220506101139"
        },
        {
            "CODE": "MHG4",
            "GROUP": "PART BET",
            "NAME": "BTQ-297",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "MHGE",
            "GROUP": "PART BET",
            "NAME": "AVQ-916",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "MHGF",
            "GROUP": "GILDEMEI",
            "NAME": "BBY-441",
            "DATETIME": "220506114321"
        },
        {
            "CODE": "MHHB",
            "GROUP": "CONTRATI",
            "NAME": "BBW-670",
            "DATETIME": "220506113133"
        },
        {
            "CODE": "MHHJ",
            "GROUP": "OLIVOS S",
            "NAME": "F0J-841",
            "DATETIME": "220506120315"
        },
        {
            "CODE": "MHHW",
            "GROUP": "CASTRO",
            "NAME": "BBJ-029",
            "DATETIME": "220506102809"
        },
        {
            "CODE": "MHJ4",
            "GROUP": "ELECTRO",
            "NAME": "AVN-710",
            "DATETIME": "220506115627"
        },
        {
            "CODE": "MHJP",
            "GROUP": "T.SANTOS",
            "NAME": "BHB-842",
            "DATETIME": "220506120215"
        },
        {
            "CODE": "MHJQ",
            "GROUP": "PART BET",
            "NAME": "BFB-920",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "MHJY",
            "GROUP": "PART BET",
            "NAME": "BBH-638",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "MHKE",
            "GROUP": "MAPFRE",
            "NAME": "ANT-894",
            "DATETIME": "220506034709"
        },
        {
            "CODE": "MHKL",
            "GROUP": "MAPFRE",
            "NAME": "BBD-693",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "MHKM",
            "GROUP": "AGRO",
            "NAME": "D8L-763",
            "DATETIME": "220506120312"
        },
        {
            "CODE": "MHKW",
            "GROUP": "GILDEMEI",
            "NAME": "BBQ-434",
            "DATETIME": "220506084721"
        },
        {
            "CODE": "MHL3",
            "GROUP": "POSITIVA",
            "NAME": "M4M-080",
            "DATETIME": "220506114109"
        },
        {
            "CODE": "MHLS",
            "GROUP": "AUTONORT",
            "NAME": "T4P-255",
            "DATETIME": "220506080457"
        },
        {
            "CODE": "MHLX",
            "GROUP": "ALCIDESF",
            "NAME": "BAS-297",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "MHLY",
            "GROUP": "GILDEMEI",
            "NAME": "BBP-527",
            "DATETIME": "220506080527"
        },
        {
            "CODE": "MHM9",
            "GROUP": "TAXI",
            "NAME": "BBH-463",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "MHMN",
            "GROUP": "RIMAC",
            "NAME": "AVK-866",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "MHMP",
            "GROUP": "LINCUNA",
            "NAME": "F0U-884",
            "DATETIME": "220506120124"
        },
        {
            "CODE": "MLVC",
            "GROUP": "GRAMA",
            "NAME": "0400-JB",
            "DATETIME": "220506082454"
        },
        {
            "CODE": "MLVE",
            "GROUP": "JESHUA",
            "NAME": "P1K-941",
            "DATETIME": "220506013757"
        },
        {
            "CODE": "MMGF",
            "GROUP": "AUTOFOND",
            "NAME": "BCJ-622",
            "DATETIME": "220506071851"
        },
        {
            "CODE": "MMGK",
            "GROUP": "VILCA",
            "NAME": "AWG-767",
            "DATETIME": "220428163421"
        },
        {
            "CODE": "MMGU",
            "GROUP": "VILCA",
            "NAME": "AWG-745",
            "DATETIME": "220506055248"
        },
        {
            "CODE": "MMGV",
            "GROUP": "CMIJ",
            "NAME": "B8H-943",
            "DATETIME": "220506115830"
        },
        {
            "CODE": "MMH0",
            "GROUP": "GILDEMEI",
            "NAME": "BCO-674",
            "DATETIME": "220505160651"
        },
        {
            "CODE": "MMH3",
            "GROUP": "VILCA",
            "NAME": "AWG-839",
            "DATETIME": "220505161521"
        },
        {
            "CODE": "MMH5",
            "GROUP": "VILCA",
            "NAME": "AWG-827",
            "DATETIME": "220506120106"
        },
        {
            "CODE": "MMHA",
            "GROUP": "VILCA",
            "NAME": "AWG-800",
            "DATETIME": "220424085212"
        },
        {
            "CODE": "MMHF",
            "GROUP": "VILCA",
            "NAME": "AWF-919",
            "DATETIME": "220506120321"
        },
        {
            "CODE": "MMHK",
            "GROUP": "GOO TRIP",
            "NAME": "W3Z-241",
            "DATETIME": "220505183633"
        },
        {
            "CODE": "MMHS",
            "GROUP": "GILDEMEI",
            "NAME": "BDW-553",
            "DATETIME": "220506113830"
        },
        {
            "CODE": "MMHT",
            "GROUP": "SELGAS",
            "NAME": "A7B-985",
            "DATETIME": "220506114754"
        },
        {
            "CODE": "MMHZ",
            "GROUP": "GILDEMEI",
            "NAME": "BCB-419",
            "DATETIME": "220506072103"
        },
        {
            "CODE": "MMJ9",
            "GROUP": "VIA FOOD",
            "NAME": "AVW-948",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "MMJA",
            "GROUP": "J&JTRANS",
            "NAME": "T1P-886",
            "DATETIME": "220506081151"
        },
        {
            "CODE": "MMJF",
            "GROUP": "J&JTRANS",
            "NAME": "B4G-818",
            "DATETIME": "220506112642"
        },
        {
            "CODE": "MMJL",
            "GROUP": "SHILCAYO",
            "NAME": "C4L-748",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "MMJP",
            "GROUP": "LISTOTAX",
            "NAME": "BPC-250",
            "DATETIME": "220506092045"
        },
        {
            "CODE": "MMJX",
            "GROUP": "GILDEMEI",
            "NAME": "BCG-519",
            "DATETIME": "220506111636"
        },
        {
            "CODE": "MMK2",
            "GROUP": "MAFISA",
            "NAME": "X4A-714",
            "DATETIME": "220506115218"
        },
        {
            "CODE": "MMK4",
            "GROUP": "GILDEMEI",
            "NAME": "672720",
            "DATETIME": "220505190621"
        },
        {
            "CODE": "MMK5",
            "GROUP": "EMTRACOM",
            "NAME": "ALM-992",
            "DATETIME": "220416074848"
        },
        {
            "CODE": "MMK8",
            "GROUP": "RENPA",
            "NAME": "B6J-724",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "MMKC",
            "GROUP": "GAS IVON",
            "NAME": "F3N-990",
            "DATETIME": "220506114154"
        },
        {
            "CODE": "MMKH",
            "GROUP": "VILLENA",
            "NAME": "H2A-821",
            "DATETIME": "220505050645"
        },
        {
            "CODE": "MMKM",
            "GROUP": "PART BET",
            "NAME": "C7Y-612",
            "DATETIME": "220506094912"
        },
        {
            "CODE": "MMKV",
            "GROUP": "TRUCKTEA",
            "NAME": "V9T-719",
            "DATETIME": "220505210521"
        },
        {
            "CODE": "MMKZ",
            "GROUP": "LISTOTAX",
            "NAME": "BPC-248",
            "DATETIME": "220506103439"
        },
        {
            "CODE": "MML2",
            "GROUP": "VILLENA",
            "NAME": "H1J-884",
            "DATETIME": "220505181248"
        },
        {
            "CODE": "MMLC",
            "GROUP": "AYBARGUI",
            "NAME": "AWX-830",
            "DATETIME": "220506075506"
        },
        {
            "CODE": "MMLD",
            "GROUP": "SUEROS",
            "NAME": "V9Q-797",
            "DATETIME": "220506093412"
        },
        {
            "CODE": "MMLM",
            "GROUP": "MCM STUD",
            "NAME": "BCD-262",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "MMLQ",
            "GROUP": "MAPFRE",
            "NAME": "BBU-382",
            "DATETIME": "220506120251"
        },
        {
            "CODE": "MMLR",
            "GROUP": "RENTING",
            "NAME": "AYM-794",
            "DATETIME": "220505183742"
        },
        {
            "CODE": "MMLU",
            "GROUP": "T.WDJC",
            "NAME": "B7L-878",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "MMLY",
            "GROUP": "SLI",
            "NAME": "D3M-796",
            "DATETIME": "220506120009"
        },
        {
            "CODE": "MMM8",
            "GROUP": "RENPA",
            "NAME": "ACQ-843",
            "DATETIME": "220506092048"
        },
        {
            "CODE": "MMM9",
            "GROUP": "SAN MART",
            "NAME": "AJJ-871",
            "DATETIME": "220506120303"
        },
        {
            "CODE": "MMMQ",
            "GROUP": "BIDDLE",
            "NAME": "AWZ-871",
            "DATETIME": "220506120227"
        },
        {
            "CODE": "MMMR",
            "GROUP": "M&I GLO",
            "NAME": "B9W-930",
            "DATETIME": "220506080703"
        },
        {
            "CODE": "MMMT",
            "GROUP": "G.ROMERO",
            "NAME": "C9P-833",
            "DATETIME": "220506115548"
        },
        {
            "CODE": "MMMU",
            "GROUP": "G.ROMERO",
            "NAME": "AMJ-722",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "MMN2",
            "GROUP": "PART BET",
            "NAME": "AWC-735",
            "DATETIME": "220506120215"
        },
        {
            "CODE": "MMNT",
            "GROUP": "SOLGASTR",
            "NAME": "B4Q-986",
            "DATETIME": "220506120021"
        },
        {
            "CODE": "MMNX",
            "GROUP": "LISTOTAX",
            "NAME": "BTM-442",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "MMNZ",
            "GROUP": "EMTRACOM",
            "NAME": "ALM-993",
            "DATETIME": "220427123618"
        },
        {
            "CODE": "MMP1",
            "GROUP": "REP_GALL",
            "NAME": "D8C-730",
            "DATETIME": "220506113048"
        },
        {
            "CODE": "MMP7",
            "GROUP": "PART BET",
            "NAME": "Y2C-195",
            "DATETIME": "220506115921"
        },
        {
            "CODE": "MMPG",
            "GROUP": "FAMESA",
            "NAME": "AVY-722",
            "DATETIME": "220506084830"
        },
        {
            "CODE": "MMPJ",
            "GROUP": "G.ROMERO",
            "NAME": "C9S-892",
            "DATETIME": "220506100503"
        },
        {
            "CODE": "MMPR",
            "GROUP": "BIDDLE",
            "NAME": "AFS-713",
            "DATETIME": "220504101039"
        },
        {
            "CODE": "MMQ1",
            "GROUP": "ALCIDESF",
            "NAME": "D5I-471",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "MMQ9",
            "GROUP": "HUGAMOR",
            "NAME": "AWO-837",
            "DATETIME": "220506120145"
        },
        {
            "CODE": "MMQD",
            "GROUP": "GILDEMEI",
            "NAME": "BCL-152",
            "DATETIME": "220506113324"
        },
        {
            "CODE": "MMQM",
            "GROUP": "GEMEVA",
            "NAME": "T3A-866",
            "DATETIME": "220506065612"
        },
        {
            "CODE": "MMQW",
            "GROUP": "MOVILGAS",
            "NAME": "BCS-140",
            "DATETIME": "220506112527"
        },
        {
            "CODE": "MMQX",
            "GROUP": "FLACCON",
            "NAME": "BCK-403",
            "DATETIME": "220505225921"
        },
        {
            "CODE": "MMQY",
            "GROUP": "SHILCAYO",
            "NAME": "S1R-850",
            "DATETIME": "220506101721"
        },
        {
            "CODE": "MVKA",
            "GROUP": "RENTING",
            "NAME": "BHK-450",
            "DATETIME": "220423001136"
        },
        {
            "CODE": "MVKC",
            "GROUP": "CIMSA",
            "NAME": "F4G-905",
            "DATETIME": "220506120036"
        },
        {
            "CODE": "MVKD",
            "GROUP": "PART BET",
            "NAME": "BHI-072",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "MVKK",
            "GROUP": "JDM SAC",
            "NAME": "V0X-865",
            "DATETIME": "220506120227"
        },
        {
            "CODE": "MVKR",
            "GROUP": "JESHUA",
            "NAME": "P3M-888",
            "DATETIME": "220506092315"
        },
        {
            "CODE": "MVKS",
            "GROUP": "JESHUA",
            "NAME": "M6D-790",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "MVKV",
            "GROUP": "FERREYRO",
            "NAME": "21016",
            "DATETIME": "220506115500"
        },
        {
            "CODE": "MVL5",
            "GROUP": "GRAMA",
            "NAME": "1582-JB",
            "DATETIME": "220506085921"
        },
        {
            "CODE": "MVL9",
            "GROUP": "RENTING",
            "NAME": "AZD-835",
            "DATETIME": "220505143912"
        },
        {
            "CODE": "MVLC",
            "GROUP": "RENTING",
            "NAME": "BHK-505",
            "DATETIME": "220418113024"
        },
        {
            "CODE": "MVLG",
            "GROUP": "RENTINLE",
            "NAME": "BHB-562",
            "DATETIME": "220506120330"
        },
        {
            "CODE": "MVLH",
            "GROUP": "RENTINLE",
            "NAME": "BHB-356",
            "DATETIME": "220506113012"
        },
        {
            "CODE": "MVLJ",
            "GROUP": "GRAMA",
            "NAME": "1783-HA",
            "DATETIME": "220317233203"
        },
        {
            "CODE": "MVLS",
            "GROUP": "PACIFICO",
            "NAME": "BHG-587",
            "DATETIME": "220506090612"
        },
        {
            "CODE": "MVLX",
            "GROUP": "JESHUA",
            "NAME": "P3M-830",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "MVLY",
            "GROUP": "JESHUA",
            "NAME": "P3Y-779",
            "DATETIME": "220506120400"
        },
        {
            "CODE": "MVM4",
            "GROUP": "RENTINLE",
            "NAME": "BKL-171",
            "DATETIME": "220506095139"
        },
        {
            "CODE": "MVM5",
            "GROUP": "RENTING",
            "NAME": "AYN-714",
            "DATETIME": "220506085227"
        },
        {
            "CODE": "MVM6",
            "GROUP": "CMIJ",
            "NAME": "T2Q-816",
            "DATETIME": "220506120324"
        },
        {
            "CODE": "MVM9",
            "GROUP": "JDM SAC",
            "NAME": "V0X-849",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "MVMA",
            "GROUP": "JESHUA",
            "NAME": "P3O-812",
            "DATETIME": "220506114300"
        },
        {
            "CODE": "MVMD",
            "GROUP": "INTERSEN",
            "NAME": "AYP-803",
            "DATETIME": "220506120312"
        },
        {
            "CODE": "MVMQ",
            "GROUP": "RENTING",
            "NAME": "AYN-782",
            "DATETIME": "220505205209"
        },
        {
            "CODE": "MVMR",
            "GROUP": "JESHUA",
            "NAME": "P3Y-894",
            "DATETIME": "220506120415"
        },
        {
            "CODE": "MVMW",
            "GROUP": "JESHUA G",
            "NAME": "P3Y-846",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "MVN0",
            "GROUP": "JDM",
            "NAME": "VAP-774",
            "DATETIME": "220506120412"
        },
        {
            "CODE": "MVN3",
            "GROUP": "RENTINLE",
            "NAME": "BHB-376",
            "DATETIME": "220506120230"
        },
        {
            "CODE": "MVN4",
            "GROUP": "DE LA O",
            "NAME": "B1A-826",
            "DATETIME": "220506092536"
        },
        {
            "CODE": "MVN8",
            "GROUP": "RENTINLE",
            "NAME": "BER-458",
            "DATETIME": "220408094645"
        },
        {
            "CODE": "MVNG",
            "GROUP": "T.WEIGHT",
            "NAME": "BRE-491",
            "DATETIME": "220329062042"
        },
        {
            "CODE": "MVNK",
            "GROUP": "SOUTHERN",
            "NAME": "B8L-711",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "MVNM",
            "GROUP": "GRAMA",
            "NAME": "5753-BB",
            "DATETIME": "220506082333"
        },
        {
            "CODE": "MVNT",
            "GROUP": "JESHUA",
            "NAME": "F5A-726",
            "DATETIME": "220506115451"
        },
        {
            "CODE": "MVNU",
            "GROUP": "REPARTO",
            "NAME": "C3I-729",
            "DATETIME": "220506110103"
        },
        {
            "CODE": "MVNV",
            "GROUP": "RENTING",
            "NAME": "AYO-769",
            "DATETIME": "220505154430"
        },
        {
            "CODE": "MVNW",
            "GROUP": "JDM SAC",
            "NAME": "M-2",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "MVP1",
            "GROUP": "GRAMA",
            "NAME": "4882-BB",
            "DATETIME": "220506074942"
        },
        {
            "CODE": "MVP2",
            "GROUP": "DE BARI",
            "NAME": "AZV-762",
            "DATETIME": "220506120054"
        },
        {
            "CODE": "MVP3",
            "GROUP": "MORAN",
            "NAME": "BAA-906",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "MVP4",
            "GROUP": "GRAMA",
            "NAME": "5585-BB",
            "DATETIME": "220506083930"
        },
        {
            "CODE": "MVP6",
            "GROUP": "GRAMA",
            "NAME": "5079-BB",
            "DATETIME": "220506081024"
        },
        {
            "CODE": "MVP7",
            "GROUP": "RENTING",
            "NAME": "AYN-783",
            "DATETIME": "220505200554"
        },
        {
            "CODE": "MVP9",
            "GROUP": "PART BET",
            "NAME": "BEK-264",
            "DATETIME": "220506115018"
        },
        {
            "CODE": "MVPA",
            "GROUP": "DE BARI",
            "NAME": "F7B-964",
            "DATETIME": "220506120218"
        },
        {
            "CODE": "MVPH",
            "GROUP": "SOUTHERN",
            "NAME": "B8W-866",
            "DATETIME": "220426123227"
        },
        {
            "CODE": "MVPK",
            "GROUP": "TRADESUR",
            "NAME": "C0T-938",
            "DATETIME": "220506110639"
        },
        {
            "CODE": "MVPN",
            "GROUP": "SSAT",
            "NAME": "9791-ZA",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "MVPP",
            "GROUP": "GRAMA",
            "NAME": "5752-BB",
            "DATETIME": "220506082133"
        },
        {
            "CODE": "MVPR",
            "GROUP": "RENTINLE",
            "NAME": "BER-174",
            "DATETIME": "220503100224"
        },
        {
            "CODE": "MVPS",
            "GROUP": "TRADESUR",
            "NAME": "BHO-903",
            "DATETIME": "220506120221"
        },
        {
            "CODE": "MVPT",
            "GROUP": "REPARTO",
            "NAME": "C3X-777",
            "DATETIME": "220506120324"
        },
        {
            "CODE": "MVPW",
            "GROUP": "JDM SAC",
            "NAME": "M-1",
            "DATETIME": "220428230330"
        },
        {
            "CODE": "MVPX",
            "GROUP": "RENTING",
            "NAME": "AYN-914",
            "DATETIME": "220506111251"
        },
        {
            "CODE": "MVPY",
            "GROUP": "REPARTO",
            "NAME": "C3Y-710",
            "DATETIME": "220506120015"
        },
        {
            "CODE": "MVQ0",
            "GROUP": "HILARIO",
            "NAME": "ASR-744",
            "DATETIME": "220506120039"
        },
        {
            "CODE": "MVQ2",
            "GROUP": "TAXI AH",
            "NAME": "F7F-249",
            "DATETIME": "220506120245"
        },
        {
            "CODE": "MVQ4",
            "GROUP": "GRAMA",
            "NAME": "5586-BB",
            "DATETIME": "220506120124"
        },
        {
            "CODE": "MVQA",
            "GROUP": "RENTING",
            "NAME": "AYN-847",
            "DATETIME": "220506082257"
        },
        {
            "CODE": "MVQB",
            "GROUP": "REPARTO",
            "NAME": "C3V-783",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "MVQE",
            "GROUP": "JDM",
            "NAME": "VAP-920",
            "DATETIME": "220506110348"
        },
        {
            "CODE": "MVQF",
            "GROUP": "DMV SERV",
            "NAME": "T7Y-921",
            "DATETIME": "220502182454"
        },
        {
            "CODE": "MVQG",
            "GROUP": "GARCIA",
            "NAME": "C1K-721",
            "DATETIME": "220506111954"
        },
        {
            "CODE": "MVR0",
            "GROUP": "PART BET",
            "NAME": "BRE-187",
            "DATETIME": "220506120236"
        },
        {
            "CODE": "MVR1",
            "GROUP": "JESHUA",
            "NAME": "P3M-895",
            "DATETIME": "220506112239"
        },
        {
            "CODE": "MVR2",
            "GROUP": "GRAMA ",
            "NAME": "4482-BB ",
            "DATETIME": "220506074230"
        },
        {
            "CODE": "MVR6",
            "GROUP": "JESHUA",
            "NAME": "P1L-824",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "MVR7",
            "GROUP": "JESHUA",
            "NAME": "P1S-819",
            "DATETIME": "220506120121"
        },
        {
            "CODE": "MVRA",
            "GROUP": "S&R",
            "NAME": "AXL-260",
            "DATETIME": "220506120357"
        },
        {
            "CODE": "MVRD",
            "GROUP": "GRAMA",
            "NAME": "9272-OA",
            "DATETIME": "220420234218"
        },
        {
            "CODE": "MVRL",
            "GROUP": "JDM SAC",
            "NAME": "V0Z-848",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "MVRS",
            "GROUP": "JEHSUA G",
            "NAME": "P3Y-828",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "MVRX",
            "GROUP": "JESHUA",
            "NAME": "P1J-874",
            "DATETIME": "220506120345"
        },
        {
            "CODE": "MVRY",
            "GROUP": "GILDEMEI",
            "NAME": "BDA-692",
            "DATETIME": "220506080227"
        },
        {
            "CODE": "MVS0",
            "GROUP": "DIAG.UAL",
            "NAME": "AMS-780",
            "DATETIME": "220420133500"
        },
        {
            "CODE": "MVS2",
            "GROUP": "GRAMA",
            "NAME": "4605-BB",
            "DATETIME": "220319201724"
        },
        {
            "CODE": "MVS3",
            "GROUP": "GRAMA",
            "NAME": "4299-BB",
            "DATETIME": "220506094457"
        },
        {
            "CODE": "MVS8",
            "GROUP": "JDM",
            "NAME": "VAP-963",
            "DATETIME": "220505161509"
        },
        {
            "CODE": "MVSB",
            "GROUP": "JESHUA",
            "NAME": "P3Y-915",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "MVSC",
            "GROUP": "JESHUA",
            "NAME": "P3O-833",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "MVSD",
            "GROUP": "JESHUA",
            "NAME": "P3Y-827",
            "DATETIME": "220503150757"
        },
        {
            "CODE": "MVSE",
            "GROUP": "JESHUA",
            "NAME": "P3Y-829",
            "DATETIME": "220318191312"
        },
        {
            "CODE": "MVSG",
            "GROUP": "JESHUA",
            "NAME": "P2K-708",
            "DATETIME": "220505012948"
        },
        {
            "CODE": "MVSW",
            "GROUP": "JESHUA",
            "NAME": "P3Y-824",
            "DATETIME": "220506120257"
        },
        {
            "CODE": "MVT8",
            "GROUP": "JDM SAC",
            "NAME": "V8M-886",
            "DATETIME": "220211105033"
        },
        {
            "CODE": "MVT9",
            "GROUP": "JESHUA",
            "NAME": "P2G-890",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "MVTA",
            "GROUP": "JESHUA",
            "NAME": "P3Y-847",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "MVTC",
            "GROUP": "JDM SAC",
            "NAME": "VAL-865",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "MVTD",
            "GROUP": "LINCUNA",
            "NAME": "AUD-893",
            "DATETIME": "220506114336"
        },
        {
            "CODE": "MVTF",
            "GROUP": "JESHUA",
            "NAME": "P3M-816",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "MVTG",
            "GROUP": "JESHUA",
            "NAME": "P1J-875",
            "DATETIME": "220503150300"
        },
        {
            "CODE": "MVTN",
            "GROUP": "JESHUA",
            "NAME": "P3Y-805",
            "DATETIME": "220506120309"
        },
        {
            "CODE": "MVTT",
            "GROUP": "TRADESUR",
            "NAME": "BHO-925",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "MVTU",
            "GROUP": "JESHUA",
            "NAME": "P3O-851",
            "DATETIME": "220506101918"
        },
        {
            "CODE": "MVTV",
            "GROUP": "NEXUS",
            "NAME": "BFY-006",
            "DATETIME": "220506073809"
        },
        {
            "CODE": "MVTX",
            "GROUP": "JDM SAC",
            "NAME": "V0X-833",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "MWHZ",
            "GROUP": "SOUTHERN",
            "NAME": "AMQ-917",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "MWJD",
            "GROUP": "NEGERIB",
            "NAME": "AVK-788",
            "DATETIME": "220506115809"
        },
        {
            "CODE": "MWJK",
            "GROUP": "PAREDES",
            "NAME": "T3X-926",
            "DATETIME": "220505164257"
        },
        {
            "CODE": "MWJL",
            "GROUP": "SHILCAYO",
            "NAME": "B8H-972",
            "DATETIME": "220506114000"
        },
        {
            "CODE": "MWJM",
            "GROUP": "HUGAMOR",
            "NAME": "AXB-863",
            "DATETIME": "220506093924"
        },
        {
            "CODE": "MWJP",
            "GROUP": "T ACOSTA",
            "NAME": "ATF-915",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "MWJR",
            "GROUP": "NOR OIL",
            "NAME": "T7S-897",
            "DATETIME": "220506120324"
        },
        {
            "CODE": "MWJT",
            "GROUP": "NEGERIB",
            "NAME": "AHQ-977",
            "DATETIME": "220504071009"
        },
        {
            "CODE": "MWK3",
            "GROUP": "REPARTO",
            "NAME": "BAO-855",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "MWK4",
            "GROUP": "REPARTO",
            "NAME": "ABT-746",
            "DATETIME": "220506111057"
        },
        {
            "CODE": "MWK7",
            "GROUP": "GOLDEN C",
            "NAME": "AWZ-775",
            "DATETIME": "220506105818"
        },
        {
            "CODE": "MWK8",
            "GROUP": "TAMBOGRA",
            "NAME": "AYM-781",
            "DATETIME": "220506114721"
        },
        {
            "CODE": "MWKU",
            "GROUP": "TAMBOGRA",
            "NAME": "AYJ-787",
            "DATETIME": "220505161051"
        },
        {
            "CODE": "MWKV",
            "GROUP": "TAMBOGRA",
            "NAME": "AYI-755",
            "DATETIME": "220325112242"
        },
        {
            "CODE": "MWKW",
            "GROUP": "THEM",
            "NAME": "T4H-861",
            "DATETIME": "220505163836"
        },
        {
            "CODE": "MWKZ",
            "GROUP": "R Y J",
            "NAME": "AYG-857",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "MWL0",
            "GROUP": "R Y J ",
            "NAME": "AYH-748",
            "DATETIME": "220324141915"
        },
        {
            "CODE": "MWL9",
            "GROUP": "TICLAVIL",
            "NAME": "F9R-980",
            "DATETIME": "220504114230"
        },
        {
            "CODE": "MWLC",
            "GROUP": "TAMBOGRA",
            "NAME": "AYH-802",
            "DATETIME": "220505161400"
        },
        {
            "CODE": "MWLG",
            "GROUP": "ALCOHOL",
            "NAME": "BDP-849",
            "DATETIME": "220506105115"
        },
        {
            "CODE": "MWLH",
            "GROUP": "TAMBOGRA",
            "NAME": "AYL-864",
            "DATETIME": "220506070606"
        },
        {
            "CODE": "MWLQ",
            "GROUP": "REPARTO",
            "NAME": "AYL-751",
            "DATETIME": "220505083354"
        },
        {
            "CODE": "MWLY",
            "GROUP": "TICLAVIL",
            "NAME": "F8B-991",
            "DATETIME": "220502081700"
        },
        {
            "CODE": "MWM7",
            "GROUP": "G.ATICO",
            "NAME": "VDI-975",
            "DATETIME": "220426185245"
        },
        {
            "CODE": "MWMD",
            "GROUP": "TICLAVIL",
            "NAME": "ABK-972",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "MWME",
            "GROUP": "NOR OIL",
            "NAME": "T8C-863",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "MWMH",
            "GROUP": "R Y J",
            "NAME": "BFE-522",
            "DATETIME": "220506092936"
        },
        {
            "CODE": "MWMV",
            "GROUP": "NOR OIL",
            "NAME": "T4D-308",
            "DATETIME": "220506120000"
        },
        {
            "CODE": "MWN3",
            "GROUP": "R Y J",
            "NAME": "AYG-807",
            "DATETIME": "220506115833"
        },
        {
            "CODE": "MWN7",
            "GROUP": "MANDUJAN",
            "NAME": "AYC-931",
            "DATETIME": "220506114542"
        },
        {
            "CODE": "MWNF",
            "GROUP": "REPARTO",
            "NAME": "AAJ-978",
            "DATETIME": "220411213845"
        },
        {
            "CODE": "MWNG",
            "GROUP": "T.EMNA",
            "NAME": "AWW-898",
            "DATETIME": "220506103451"
        },
        {
            "CODE": "MWP4",
            "GROUP": "MANDUJAN",
            "NAME": "TCS-970",
            "DATETIME": "220505201257"
        },
        {
            "CODE": "MWPE",
            "GROUP": "ORETEL",
            "NAME": "AXQ-920",
            "DATETIME": "220503105857"
        },
        {
            "CODE": "MWPY",
            "GROUP": "RODUL",
            "NAME": "D4R-942",
            "DATETIME": "220506104206"
        },
        {
            "CODE": "MWQ5",
            "GROUP": "G CHIRA",
            "NAME": "P3V-936",
            "DATETIME": "220506105024"
        },
        {
            "CODE": "MWQA",
            "GROUP": "T.CORREA",
            "NAME": "AFG-972",
            "DATETIME": "220506114357"
        },
        {
            "CODE": "MWQD",
            "GROUP": "L & M",
            "NAME": "C3V-866",
            "DATETIME": "220506084509"
        },
        {
            "CODE": "MWQG",
            "GROUP": "SAN DIEG",
            "NAME": "ANJ-943",
            "DATETIME": "220505184839"
        },
        {
            "CODE": "MWQR",
            "GROUP": "SAN MART",
            "NAME": "AAO-701",
            "DATETIME": "220506120357"
        },
        {
            "CODE": "MWQV",
            "GROUP": "SELGAS",
            "NAME": "F9B-982",
            "DATETIME": "220506054242"
        },
        {
            "CODE": "MWQZ",
            "GROUP": "TMC",
            "NAME": "AHW-862",
            "DATETIME": "220202100154"
        },
        {
            "CODE": "MWR0",
            "GROUP": "SANDOVAL",
            "NAME": "M1K-994",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "MWR7",
            "GROUP": "REPARTO",
            "NAME": "ANO-840",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "MWRB",
            "GROUP": "QANTU ",
            "NAME": "F2D-882",
            "DATETIME": "220505191548"
        },
        {
            "CODE": "MWRC",
            "GROUP": "DIAZ HAR",
            "NAME": "BDZ-369",
            "DATETIME": "220506094657"
        },
        {
            "CODE": "MWRE",
            "GROUP": "CONDOR.T",
            "NAME": "F2N-952",
            "DATETIME": "220506073945"
        },
        {
            "CODE": "MWRM",
            "GROUP": "EMTRACOM",
            "NAME": "ALM-991",
            "DATETIME": "220104082439"
        },
        {
            "CODE": "MWRS",
            "GROUP": "TAXI AH",
            "NAME": "AZV-572",
            "DATETIME": "220506115312"
        },
        {
            "CODE": "MWRT",
            "GROUP": "ALCOHOL",
            "NAME": "AWY-901",
            "DATETIME": "220505130330"
        },
        {
            "CODE": "MWRZ",
            "GROUP": "LISTOTAX",
            "NAME": "BWQ-425",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "MWS5",
            "GROUP": "RENTANOR",
            "NAME": "T6B-880",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "MWS7",
            "GROUP": "PART BET",
            "NAME": "BCN-118",
            "DATETIME": "220506073615"
        },
        {
            "CODE": "MWS8",
            "GROUP": "RENTANOR",
            "NAME": "T8Z-969",
            "DATETIME": "220418115200"
        },
        {
            "CODE": "MWS9",
            "GROUP": "CAMDE",
            "NAME": "AYI-706",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "MWSP",
            "GROUP": "SAVIA",
            "NAME": "PARINAS",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "MWSV",
            "GROUP": "SAVIA",
            "NAME": "VILMA",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "MWSX",
            "GROUP": "A&S OPER",
            "NAME": "ANDINOII",
            "DATETIME": "220506063812"
        },
        {
            "CODE": "MWSY",
            "GROUP": "SAVIA",
            "NAME": "OLYMPIC",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "MWT0",
            "GROUP": "SOLGASAL",
            "NAME": "F6B-972",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "MWT1",
            "GROUP": "SAVIA",
            "NAME": "CHIP II",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "MWT3",
            "GROUP": "SAVIA",
            "NAME": "TALARA",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "MWT4",
            "GROUP": "SAVIA",
            "NAME": "ODIN",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "MWT6",
            "GROUP": "SAVIA",
            "NAME": "DONALD R",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "MWT7",
            "GROUP": "SAVIA",
            "NAME": "NEPTUNO",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "MWT8",
            "GROUP": "SAVIA",
            "NAME": "SHEILA",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "MWTA",
            "GROUP": "SAVIA",
            "NAME": "MR. MATT",
            "DATETIME": "220506115254"
        },
        {
            "CODE": "MWTB",
            "GROUP": "SAVIA",
            "NAME": "ROSLYN",
            "DATETIME": "220506120400"
        },
        {
            "CODE": "MWTQ",
            "GROUP": "SLI",
            "NAME": "A1M-979",
            "DATETIME": "220311075042"
        },
        {
            "CODE": "MWTS",
            "GROUP": "LISTOTAX",
            "NAME": "BTP-407",
            "DATETIME": "220505142948"
        },
        {
            "CODE": "MWTT",
            "GROUP": "LISTOTAX",
            "NAME": "BTO-556",
            "DATETIME": "220505231606"
        },
        {
            "CODE": "MWTU",
            "GROUP": "T.INCHE",
            "NAME": "AUL-700",
            "DATETIME": "220506120233"
        },
        {
            "CODE": "MWTV",
            "GROUP": "SAVIA",
            "NAME": "LOBITOS",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "MWTW",
            "GROUP": "SAVIA",
            "NAME": "ELIZABET",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "MWU0",
            "GROUP": "LINARES",
            "NAME": "RODOLFO",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "MWU1",
            "GROUP": "SAVIA",
            "NAME": "BULKEY",
            "DATETIME": "220506113557"
        },
        {
            "CODE": "MWU2",
            "GROUP": "SAVIA",
            "NAME": "CBLANCO",
            "DATETIME": "220506104239"
        },
        {
            "CODE": "MWU3",
            "GROUP": "LINARES",
            "NAME": "RODRIGO",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "MWUB",
            "GROUP": "LINARES",
            "NAME": "LINARESV",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "MWUF",
            "GROUP": "SOLGASTR",
            "NAME": "B5Z-972",
            "DATETIME": "220506120415"
        },
        {
            "CODE": "MWUJ",
            "GROUP": "INACTIVO",
            "NAME": "V8C-898",
            "DATETIME": "220506120309"
        },
        {
            "CODE": "MWUK",
            "GROUP": "SAVIA",
            "NAME": "ZULUF EX",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "MWUP",
            "GROUP": "RENTINLE",
            "NAME": "BHA-685",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "MWUR",
            "GROUP": "SHILCAYO",
            "NAME": "ATD-971",
            "DATETIME": "220506084712"
        },
        {
            "CODE": "MWUS",
            "GROUP": "A&S OPER",
            "NAME": "JESSICA",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "MWUT",
            "GROUP": "SOLGASER",
            "NAME": "C4V-989",
            "DATETIME": "220502140127"
        },
        {
            "CODE": "MWV2",
            "GROUP": "LINARES",
            "NAME": "MIA VALE",
            "DATETIME": "220420022612"
        },
        {
            "CODE": "MWV4",
            "GROUP": "LINARES",
            "NAME": "3REYES",
            "DATETIME": "220505045942"
        },
        {
            "CODE": "MWV6",
            "GROUP": "SOLGASTR",
            "NAME": "D1J-994",
            "DATETIME": "220421001618"
        },
        {
            "CODE": "MWV9",
            "GROUP": "LISTOTAX",
            "NAME": "BTP-048",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "MWVA",
            "GROUP": "LISTOTAX",
            "NAME": "BTN-504",
            "DATETIME": "220505125042"
        },
        {
            "CODE": "MWVB",
            "GROUP": "DE LA O",
            "NAME": "AJE-739",
            "DATETIME": "220505153027"
        },
        {
            "CODE": "MWVC",
            "GROUP": "SAVIA",
            "NAME": "CHIRIBAY",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "MWVF",
            "GROUP": "LINARES",
            "NAME": "MAESTRO",
            "DATETIME": "220306121457"
        },
        {
            "CODE": "MWVH",
            "GROUP": "LINARES",
            "NAME": "STAMARTA",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "NC1C",
            "GROUP": "PAREDES",
            "NAME": "T4Q-822",
            "DATETIME": "220506094541"
        },
        {
            "CODE": "NCH3",
            "GROUP": "MAYER SA",
            "NAME": "A1E-878",
            "DATETIME": "220506115051"
        },
        {
            "CODE": "NCQ3",
            "GROUP": "G.ATICO",
            "NAME": "V4B-818",
            "DATETIME": "220505154205"
        },
        {
            "CODE": "NCSQ",
            "GROUP": "ESPINOZA",
            "NAME": "A0D-824",
            "DATETIME": "220506115308"
        },
        {
            "CODE": "NE87",
            "GROUP": "GEMEVA",
            "NAME": "T5O-810",
            "DATETIME": "220506102555"
        },
        {
            "CODE": "NE91",
            "GROUP": "STA-ROSA",
            "NAME": "F5U-786",
            "DATETIME": "220506090744"
        },
        {
            "CODE": "NEBQ",
            "GROUP": "GBORRA",
            "NAME": "C0A-293",
            "DATETIME": "220506093415"
        },
        {
            "CODE": "NEEU",
            "GROUP": "V.CASTRO",
            "NAME": "A9R-618",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "NPLF",
            "GROUP": "ELECTRO",
            "NAME": "SIX-583",
            "DATETIME": "220506114141"
        },
        {
            "CODE": "NPLV",
            "GROUP": "AXON",
            "NAME": "A6G-888",
            "DATETIME": "220506114724"
        },
        {
            "CODE": "NRXD",
            "GROUP": "CESEL",
            "NAME": "A3V-331",
            "DATETIME": "220506055654"
        },
        {
            "CODE": "P0DD",
            "GROUP": "SUEROS",
            "NAME": "V2J-814",
            "DATETIME": "220506120405"
        },
        {
            "CODE": "P0GV",
            "GROUP": "VENTURA",
            "NAME": "V5D-751",
            "DATETIME": "220506114300"
        },
        {
            "CODE": "P3ZW",
            "GROUP": "G.ATICO",
            "NAME": "YH-4848",
            "DATETIME": "220504084958"
        },
        {
            "CODE": "P5E5",
            "GROUP": "ISIL",
            "NAME": "ASO-538",
            "DATETIME": "220505115425"
        },
        {
            "CODE": "P5WT",
            "GROUP": "EMCOMER",
            "NAME": "B1Q-869",
            "DATETIME": "220506114910"
        },
        {
            "CODE": "PJ78",
            "GROUP": "GEMEVA",
            "NAME": "T2G-892",
            "DATETIME": "220503081311"
        },
        {
            "CODE": "PJ9N",
            "GROUP": "ENMANUEL",
            "NAME": "D7O-719",
            "DATETIME": "220506114210"
        },
        {
            "CODE": "PJ9X",
            "GROUP": "SUEROS",
            "NAME": "V8U-786",
            "DATETIME": "220506082428"
        },
        {
            "CODE": "PY67",
            "GROUP": "TAXI",
            "NAME": "F3B-411",
            "DATETIME": "220506120450"
        },
        {
            "CODE": "Q6UL",
            "GROUP": "NEXUS T",
            "NAME": "BMT-910",
            "DATETIME": "220506120455"
        },
        {
            "CODE": "Q70X",
            "GROUP": "NEXUS T",
            "NAME": "BMJ-723",
            "DATETIME": "220504075013"
        },
        {
            "CODE": "Q7ZW",
            "GROUP": "ELECTRO",
            "NAME": "ROY-827",
            "DATETIME": "220111214527"
        },
        {
            "CODE": "S2VV",
            "GROUP": "VILLENA",
            "NAME": "F1R-936",
            "DATETIME": "220506115627"
        },
        {
            "CODE": "S4EA",
            "GROUP": "SAN DIEG",
            "NAME": "F6O-991",
            "DATETIME": "220502191942"
        },
        {
            "CODE": "S4F3",
            "GROUP": "VILLENA",
            "NAME": "F2R-789",
            "DATETIME": "220506115603"
        },
        {
            "CODE": "S4FG",
            "GROUP": "GILDEMEI",
            "NAME": "AVU-278",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "S4FM",
            "GROUP": "VILLENA ",
            "NAME": "D5G-915",
            "DATETIME": "220506094103"
        },
        {
            "CODE": "S9FB",
            "GROUP": "ELECTRO",
            "NAME": "A8A-366",
            "DATETIME": "220413222248"
        },
        {
            "CODE": "S9FT",
            "GROUP": "AUTOESPA",
            "NAME": "C1V-826",
            "DATETIME": "220506084539"
        },
        {
            "CODE": "SBGY",
            "GROUP": "REPARTO ",
            "NAME": "ANJ-874",
            "DATETIME": "220504113842"
        },
        {
            "CODE": "SBP1",
            "GROUP": "ENMANUEL",
            "NAME": "AUS-881",
            "DATETIME": "220506115230"
        },
        {
            "CODE": "SBP5",
            "GROUP": "AUTOESPA",
            "NAME": "C9P-927",
            "DATETIME": "220506111251"
        },
        {
            "CODE": "SBP8",
            "GROUP": "AUTOESPA",
            "NAME": "C1V-827",
            "DATETIME": "220506094303"
        },
        {
            "CODE": "SCHX",
            "GROUP": "AUTOESPA",
            "NAME": "F0T-811",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "SCJB",
            "GROUP": "AUTOESPA",
            "NAME": "C8H-826",
            "DATETIME": "220506114509"
        },
        {
            "CODE": "SCJZ",
            "GROUP": "T.ROCHA",
            "NAME": "D8E-880",
            "DATETIME": "220430114806"
        },
        {
            "CODE": "SCK0",
            "GROUP": "TRANSGES",
            "NAME": "C5L-850",
            "DATETIME": "220506120057"
        },
        {
            "CODE": "SCK9",
            "GROUP": "ALCIDESF",
            "NAME": "X2W-651",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "SJ2B",
            "GROUP": "TRANSGES",
            "NAME": "C5L-858",
            "DATETIME": "220505164757"
        },
        {
            "CODE": "SJ2R",
            "GROUP": "REPARTO",
            "NAME": "ANJ-863",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "SJ3G",
            "GROUP": "SOLGASER",
            "NAME": "B6B-978",
            "DATETIME": "220506120136"
        },
        {
            "CODE": "SKRB",
            "GROUP": "GILDEMEI",
            "NAME": "AVF-478",
            "DATETIME": "220506111642"
        },
        {
            "CODE": "SKSM",
            "GROUP": "SOLGASTR",
            "NAME": "C4Q-975",
            "DATETIME": "220506120221"
        },
        {
            "CODE": "SKSX",
            "GROUP": "VILLENA",
            "NAME": "ABP-897",
            "DATETIME": "220506072827"
        },
        {
            "CODE": "SKTK",
            "GROUP": "RIMAC ",
            "NAME": "AFA-361",
            "DATETIME": "220506083839"
        },
        {
            "CODE": "SKTL",
            "GROUP": "MORALES",
            "NAME": "F7F-806",
            "DATETIME": "220506114442"
        },
        {
            "CODE": "SKTP",
            "GROUP": "PART BET",
            "NAME": "BSB-130",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "SKU0",
            "GROUP": "PART BET",
            "NAME": "AVJ-067",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "SKVK",
            "GROUP": "ESPAR",
            "NAME": "AVS-610",
            "DATETIME": "220505171733"
        },
        {
            "CODE": "SN38",
            "GROUP": "HUGAMOR",
            "NAME": "ACU-747",
            "DATETIME": "220506115954"
        },
        {
            "CODE": "SN6Z",
            "GROUP": "SUEROS",
            "NAME": "V6R-738",
            "DATETIME": "220506084103"
        },
        {
            "CODE": "SN7B",
            "GROUP": "ARYUNA",
            "NAME": "D0D-796",
            "DATETIME": "220506114612"
        },
        {
            "CODE": "SQ29",
            "GROUP": "REPARTO",
            "NAME": "AAX-993",
            "DATETIME": "220330160621"
        },
        {
            "CODE": "SQ2W",
            "GROUP": "ALCIDESF",
            "NAME": "C1C-376",
            "DATETIME": "220505192254"
        },
        {
            "CODE": "SRT3",
            "GROUP": "ARYUNA",
            "NAME": "C0K-738",
            "DATETIME": "220506114742"
        },
        {
            "CODE": "SRU4",
            "GROUP": "ENMANUEL",
            "NAME": "AKO-752",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "SRXV",
            "GROUP": "ALCIDESF",
            "NAME": "C7A-582",
            "DATETIME": "220506115839"
        },
        {
            "CODE": "SRYV",
            "GROUP": "STA-ROSA",
            "NAME": "C0G-904",
            "DATETIME": "220506120045"
        },
        {
            "CODE": "ST5U",
            "GROUP": "REPARTO",
            "NAME": "D6G-827",
            "DATETIME": "220422173318"
        },
        {
            "CODE": "ST6E",
            "GROUP": "TILIN",
            "NAME": "V3F-743",
            "DATETIME": "220505130406"
        },
        {
            "CODE": "ST6K",
            "GROUP": "M.INFANT",
            "NAME": "C7L-909",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "ST6W",
            "GROUP": "ARYUNA",
            "NAME": "C4A-916",
            "DATETIME": "220506112603"
        },
        {
            "CODE": "ST89",
            "GROUP": "VIPAUR",
            "NAME": "T4E-930",
            "DATETIME": "220506113548"
        },
        {
            "CODE": "STEB",
            "GROUP": "MORAN",
            "NAME": "F4F-847",
            "DATETIME": "220506074536"
        },
        {
            "CODE": "STFQ",
            "GROUP": "ENMANUEL",
            "NAME": "AKO-754",
            "DATETIME": "220504172530"
        },
        {
            "CODE": "STQ5",
            "GROUP": "REPARTO",
            "NAME": "AAJ-983",
            "DATETIME": "220503163554"
        },
        {
            "CODE": "STRL",
            "GROUP": "PART BET",
            "NAME": "BMD-660",
            "DATETIME": "220427110400"
        },
        {
            "CODE": "SYQC",
            "GROUP": "M.INFANT",
            "NAME": "A2F-831",
            "DATETIME": "220506120009"
        },
        {
            "CODE": "SZA7",
            "GROUP": "GILDEMEI",
            "NAME": "AVU-002",
            "DATETIME": "220506115600"
        },
        {
            "CODE": "SZCE",
            "GROUP": "SOLGASER",
            "NAME": "B4P-999",
            "DATETIME": "220506120309"
        },
        {
            "CODE": "SZCZ",
            "GROUP": "GILDEMEI",
            "NAME": "AVR-353",
            "DATETIME": "220506113903"
        },
        {
            "CODE": "SZF2",
            "GROUP": "RIMAC",
            "NAME": "AVS-052",
            "DATETIME": "220506115045"
        },
        {
            "CODE": "SZVW",
            "GROUP": "LISTOTAX",
            "NAME": "BJL-111",
            "DATETIME": "220506114748"
        },
        {
            "CODE": "SZW2",
            "GROUP": "MOVILGAS",
            "NAME": "F9W-979",
            "DATETIME": "220506120148"
        },
        {
            "CODE": "SZW3",
            "GROUP": "SOLGASTR",
            "NAME": "C6R-982",
            "DATETIME": "220506110709"
        },
        {
            "CODE": "SZW4",
            "GROUP": "SOLGASER",
            "NAME": "B4O-999",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "SZW5",
            "GROUP": "SOLGASTR",
            "NAME": "D1K-980",
            "DATETIME": "220418112157"
        },
        {
            "CODE": "SZWA",
            "GROUP": "LISTOTAX",
            "NAME": "BHZ-552",
            "DATETIME": "220506080924"
        },
        {
            "CODE": "SZWE",
            "GROUP": "C.NEYRA",
            "NAME": "BEU-946",
            "DATETIME": "220506094039"
        },
        {
            "CODE": "SZWL",
            "GROUP": "SOLGASER",
            "NAME": "B6J-971",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "SZWN",
            "GROUP": "T.SANTOS",
            "NAME": "C9N-836",
            "DATETIME": "220506114533"
        },
        {
            "CODE": "SZWS",
            "GROUP": "SOLGASTR",
            "NAME": "F3Z-993",
            "DATETIME": "220503210512"
        },
        {
            "CODE": "SZWT",
            "GROUP": "SHILCAYO",
            "NAME": "C6N-977",
            "DATETIME": "220506085218"
        },
        {
            "CODE": "SZWU",
            "GROUP": "SOLGASTR",
            "NAME": "F4A-982",
            "DATETIME": "220506120151"
        },
        {
            "CODE": "SZX4",
            "GROUP": "PORTALES",
            "NAME": "BCZ-701",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "SZX6",
            "GROUP": "LISTOTAX",
            "NAME": "BTF-696",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "SZX7",
            "GROUP": "LISTOTAX",
            "NAME": "BLB-030",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "SZXE",
            "GROUP": "SOLGASTR",
            "NAME": "C5D-970",
            "DATETIME": "220506115048"
        },
        {
            "CODE": "SZXG",
            "GROUP": "SOLGASER",
            "NAME": "C4V-991",
            "DATETIME": "220506092712"
        },
        {
            "CODE": "SZXP",
            "GROUP": "SOLGASTR",
            "NAME": "D1J-997",
            "DATETIME": "220506114333"
        },
        {
            "CODE": "SZXU",
            "GROUP": "MONTALVA",
            "NAME": "B6L-718",
            "DATETIME": "220505210724"
        },
        {
            "CODE": "U2MN",
            "GROUP": "TCARRION",
            "NAME": "W3H-995",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "U2MQ",
            "GROUP": "LISTOTAX",
            "NAME": "BXM-095",
            "DATETIME": "220506115051"
        },
        {
            "CODE": "U2MW",
            "GROUP": "LISTOTAX",
            "NAME": "BJA-408",
            "DATETIME": "220418125248"
        },
        {
            "CODE": "U2MY",
            "GROUP": "SAGA",
            "NAME": "BSC-583",
            "DATETIME": "220506113848"
        },
        {
            "CODE": "U2N0",
            "GROUP": "TRANSCA1",
            "NAME": "C9R-749",
            "DATETIME": "220506115154"
        },
        {
            "CODE": "U2N3",
            "GROUP": "MOVIL.GA",
            "NAME": "AMR-728",
            "DATETIME": "220505161133"
        },
        {
            "CODE": "U2N7",
            "GROUP": "LISTOTAX",
            "NAME": "BTO-557",
            "DATETIME": "220506115830"
        },
        {
            "CODE": "U2NA",
            "GROUP": "MAPFRE",
            "NAME": "X4U-845",
            "DATETIME": "220506111257"
        },
        {
            "CODE": "U2NJ",
            "GROUP": "SOUTHERN",
            "NAME": "AYD-922",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "U2NU",
            "GROUP": "AUTONORT",
            "NAME": "AMZ-816",
            "DATETIME": "220505124318"
        },
        {
            "CODE": "U2PA",
            "GROUP": "POMA",
            "NAME": "C8S-818",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "U2PB",
            "GROUP": "POMA",
            "NAME": "F9V-758",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "U2PL",
            "GROUP": "ENERLETR",
            "NAME": "W5R-813",
            "DATETIME": "220506102048"
        },
        {
            "CODE": "U2PM",
            "GROUP": "SUEROS",
            "NAME": "V8L-906",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "U2QP",
            "GROUP": "RENTINLE",
            "NAME": "BLK-677",
            "DATETIME": "220506115927"
        },
        {
            "CODE": "U2SE",
            "GROUP": "SANTAINE",
            "NAME": "D8O-913",
            "DATETIME": "220506115739"
        },
        {
            "CODE": "U2TA",
            "GROUP": "MAPFRE",
            "NAME": "ARO-497",
            "DATETIME": "220506115718"
        },
        {
            "CODE": "U2TT",
            "GROUP": "RIMAC",
            "NAME": "ARK-387",
            "DATETIME": "220506091036"
        },
        {
            "CODE": "U2TW",
            "GROUP": "RIMAC",
            "NAME": "APX-531",
            "DATETIME": "220506112621"
        },
        {
            "CODE": "U2UB",
            "GROUP": "T.EMNA",
            "NAME": "T5Z-850",
            "DATETIME": "220506114215"
        },
        {
            "CODE": "U2UK",
            "GROUP": "AUTONORT",
            "NAME": "T3Z-174",
            "DATETIME": "220506115236"
        },
        {
            "CODE": "U2UP",
            "GROUP": "CALEXA",
            "NAME": "C2Q-826",
            "DATETIME": "220506113745"
        },
        {
            "CODE": "U2US",
            "GROUP": "RIMAC",
            "NAME": "ARA-199",
            "DATETIME": "220505175339"
        },
        {
            "CODE": "U2V2",
            "GROUP": "T.FLORES",
            "NAME": "D2S-827",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "U2V5",
            "GROUP": "MAPFRE",
            "NAME": "D8S-820",
            "DATETIME": "220506114530"
        },
        {
            "CODE": "U2V8",
            "GROUP": "REPARTO",
            "NAME": "AYU-816",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "U2VA",
            "GROUP": "BIDDLE",
            "NAME": "A0O-711",
            "DATETIME": "220428112715"
        },
        {
            "CODE": "U2VM",
            "GROUP": "ESPAR",
            "NAME": "ARV-497",
            "DATETIME": "220506113251"
        },
        {
            "CODE": "U2VN",
            "GROUP": "ESPAR",
            "NAME": "ARX-057",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "U2VS",
            "GROUP": "ESPAR",
            "NAME": "ASH-622",
            "DATETIME": "220426040721"
        },
        {
            "CODE": "U2WL",
            "GROUP": "NOR OIL",
            "NAME": "BJK-826",
            "DATETIME": "220506120251"
        },
        {
            "CODE": "U2X0",
            "GROUP": "ESPAR",
            "NAME": "ASF-611",
            "DATETIME": "220506120036"
        },
        {
            "CODE": "U2XA",
            "GROUP": "POMA",
            "NAME": "C6D-856",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "U2YM",
            "GROUP": "RODUL",
            "NAME": "V5F-834",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "U2ZD",
            "GROUP": "POSITIVA",
            "NAME": "H2O-919",
            "DATETIME": "220506115251"
        },
        {
            "CODE": "U3R7",
            "GROUP": "FAMESA",
            "NAME": "ANY-945",
            "DATETIME": "220506114706"
        },
        {
            "CODE": "U3R9",
            "GROUP": "LYM",
            "NAME": "AKB-779",
            "DATETIME": "220506120345"
        },
        {
            "CODE": "U3RP",
            "GROUP": "RENTING",
            "NAME": "AWL-718",
            "DATETIME": "220506113727"
        },
        {
            "CODE": "U3RT",
            "GROUP": "IMPROVEK",
            "NAME": "ANN-912",
            "DATETIME": "220506114115"
        },
        {
            "CODE": "U3S1",
            "GROUP": "GIANT",
            "NAME": "D6U-916",
            "DATETIME": "220503105721"
        },
        {
            "CODE": "U3SG",
            "GROUP": "AUTONORT",
            "NAME": "M4D-301",
            "DATETIME": "220506113818"
        },
        {
            "CODE": "U3SK",
            "GROUP": "LISTOTAX",
            "NAME": "BLB-554",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "U3ST",
            "GROUP": "AUTONORT",
            "NAME": "M4D-408",
            "DATETIME": "220506115418"
        },
        {
            "CODE": "U3SV",
            "GROUP": "ESPAR",
            "NAME": "ASV-298",
            "DATETIME": "220506114830"
        },
        {
            "CODE": "U3SX",
            "GROUP": "AUTONORT",
            "NAME": "M4D-199",
            "DATETIME": "220506120412"
        },
        {
            "CODE": "U3T7",
            "GROUP": "PART BET",
            "NAME": "ASN-569",
            "DATETIME": "220506115200"
        },
        {
            "CODE": "U3T9",
            "GROUP": "POSITIVA",
            "NAME": "ASJ-242",
            "DATETIME": "220506115748"
        },
        {
            "CODE": "U3TD",
            "GROUP": "RENTINCA",
            "NAME": "AWC-948",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "U3TN",
            "GROUP": "AUTOESPA",
            "NAME": "ASI-541",
            "DATETIME": "220506114057"
        },
        {
            "CODE": "U3TR",
            "GROUP": "POSITIVA",
            "NAME": "ANQ-728",
            "DATETIME": "220506115657"
        },
        {
            "CODE": "U3TT",
            "GROUP": "POSITIVA",
            "NAME": "ANP-719",
            "DATETIME": "220506115518"
        },
        {
            "CODE": "U3UB",
            "GROUP": "RIMAC",
            "NAME": "ASR-340",
            "DATETIME": "220504132239"
        },
        {
            "CODE": "U3UL",
            "GROUP": "AUTOESPA",
            "NAME": "ASN-488",
            "DATETIME": "220506114239"
        },
        {
            "CODE": "U3V1",
            "GROUP": "A&J",
            "NAME": "ANF-821",
            "DATETIME": "220506113339"
        },
        {
            "CODE": "U3V5",
            "GROUP": "PART BET",
            "NAME": "ABD-572",
            "DATETIME": "220506120409"
        },
        {
            "CODE": "U3V9",
            "GROUP": "MADIE",
            "NAME": "ANL-713",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "U3VJ",
            "GROUP": "REPARTO",
            "NAME": "AMB-804",
            "DATETIME": "220506102509"
        },
        {
            "CODE": "U3VK",
            "GROUP": "REPARTO",
            "NAME": "AMA-827",
            "DATETIME": "220506115921"
        },
        {
            "CODE": "U3VV",
            "GROUP": "POLMAR",
            "NAME": "F8Q-972",
            "DATETIME": "220426201724"
        },
        {
            "CODE": "U3WY",
            "GROUP": "AUTONORT",
            "NAME": "P2T-432",
            "DATETIME": "220506113603"
        },
        {
            "CODE": "U3X2",
            "GROUP": "REPARTO",
            "NAME": "AMC-722",
            "DATETIME": "220506114918"
        },
        {
            "CODE": "U3X3",
            "GROUP": "VILLENA",
            "NAME": "ADN-706",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "U3X7",
            "GROUP": "RENTINLE",
            "NAME": "BHA-540",
            "DATETIME": "220506004539"
        },
        {
            "CODE": "U3XP",
            "GROUP": "ESPAR",
            "NAME": "ASQ-238",
            "DATETIME": "220506114839"
        },
        {
            "CODE": "U3XX",
            "GROUP": "RENTING",
            "NAME": "AXQ-733",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "U3XY",
            "GROUP": "AUTONORT",
            "NAME": "T4B-055",
            "DATETIME": "220506115324"
        },
        {
            "CODE": "U3YC",
            "GROUP": "GEMINIS",
            "NAME": "F5E-783",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "U3YG",
            "GROUP": "LISTOTAX",
            "NAME": "BXO-042",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "U3YH",
            "GROUP": "ESPAR",
            "NAME": "ASZ-095",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "U3YY",
            "GROUP": "ADUANDIN",
            "NAME": "A7K-846",
            "DATETIME": "220506113642"
        },
        {
            "CODE": "U3Z2",
            "GROUP": "T.CALDER",
            "NAME": "V3Y-879",
            "DATETIME": "220506114736"
        },
        {
            "CODE": "U3ZR",
            "GROUP": "PACIFICO",
            "NAME": "AKN-365",
            "DATETIME": "220505145148"
        },
        {
            "CODE": "U3ZX",
            "GROUP": "T.BALDEO",
            "NAME": "D3H-954",
            "DATETIME": "220506114757"
        },
        {
            "CODE": "U401",
            "GROUP": "MINERA",
            "NAME": "AAN-900",
            "DATETIME": "220506115200"
        },
        {
            "CODE": "U406",
            "GROUP": "MINERA",
            "NAME": "A1A-855",
            "DATETIME": "220506120209"
        },
        {
            "CODE": "U408",
            "GROUP": "OLIVARES",
            "NAME": "AYT-751",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "U40E",
            "GROUP": "TUME",
            "NAME": "ASG-665",
            "DATETIME": "220506115833"
        },
        {
            "CODE": "U40F",
            "GROUP": "RODUL",
            "NAME": "C4H-733",
            "DATETIME": "220505003709"
        },
        {
            "CODE": "U40G",
            "GROUP": "LISTOTAX",
            "NAME": "BWQ-428",
            "DATETIME": "220506114900"
        },
        {
            "CODE": "U40P",
            "GROUP": "TOÑITO",
            "NAME": "V8L-719",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "U40Q",
            "GROUP": "FCG",
            "NAME": "ANH-712",
            "DATETIME": "220506120324"
        },
        {
            "CODE": "U40S",
            "GROUP": "MINERA",
            "NAME": "AMX-924",
            "DATETIME": "220506114209"
        },
        {
            "CODE": "U40T",
            "GROUP": "SHILCAYO",
            "NAME": "ABZ-990",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "U40U",
            "GROUP": "REPARTO",
            "NAME": "AMB-903",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "U40X",
            "GROUP": "TOMACITO",
            "NAME": "A1P-901",
            "DATETIME": "220506120409"
        },
        {
            "CODE": "U410",
            "GROUP": "FAMESA",
            "NAME": "ANT-923",
            "DATETIME": "220421111206"
        },
        {
            "CODE": "U418",
            "GROUP": "FAMESA",
            "NAME": "APA-811",
            "DATETIME": "220429094506"
        },
        {
            "CODE": "U41B",
            "GROUP": "HILARIO",
            "NAME": "AYQ-722",
            "DATETIME": "220506112515"
        },
        {
            "CODE": "U41D",
            "GROUP": "BIDDLE",
            "NAME": "C4W-786",
            "DATETIME": "220506120339"
        },
        {
            "CODE": "U41G",
            "GROUP": "MYI GLO",
            "NAME": "F2T-781",
            "DATETIME": "220506120406"
        },
        {
            "CODE": "U41L",
            "GROUP": "REPARTO",
            "NAME": "AMB-838",
            "DATETIME": "220506113612"
        },
        {
            "CODE": "U41P",
            "GROUP": "REPARTO",
            "NAME": "AMA-860",
            "DATETIME": "220506120124"
        },
        {
            "CODE": "U41R",
            "GROUP": "BIDDLE",
            "NAME": "C4Y-729",
            "DATETIME": "220506113630"
        },
        {
            "CODE": "U41T",
            "GROUP": "CORPESA",
            "NAME": "C4Z-748",
            "DATETIME": "220504172006"
        },
        {
            "CODE": "U41U",
            "GROUP": "REPARTO",
            "NAME": "AMA-920",
            "DATETIME": "220506115327"
        },
        {
            "CODE": "U41Y",
            "GROUP": "REPARTO",
            "NAME": "AMA-942",
            "DATETIME": "220506114527"
        },
        {
            "CODE": "U42F",
            "GROUP": "ADUANDIN",
            "NAME": "BHR-743",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "U42K",
            "GROUP": "REPARTO",
            "NAME": "AMA-927",
            "DATETIME": "220506113936"
        },
        {
            "CODE": "U4UM",
            "GROUP": "SHILCAYO",
            "NAME": "B8B-971",
            "DATETIME": "220506120409"
        },
        {
            "CODE": "U4UY",
            "GROUP": "PISCIFAC",
            "NAME": "V9N-863",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "U4V8",
            "GROUP": "POSITIVA",
            "NAME": "T6Y-931",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "U4VC",
            "GROUP": "MORALES",
            "NAME": "F7F-915",
            "DATETIME": "220506115636"
        },
        {
            "CODE": "U4VU",
            "GROUP": "LISTOTAX",
            "NAME": "BWQ-410",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "U4W8",
            "GROUP": "CONDOR.T",
            "NAME": "D4G-968",
            "DATETIME": "220506073027"
        },
        {
            "CODE": "U4WP",
            "GROUP": "OLIVARES",
            "NAME": "AAG-944",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "U4X4",
            "GROUP": "RIMAC",
            "NAME": "ATD-336",
            "DATETIME": "220504162951"
        },
        {
            "CODE": "U4XE",
            "GROUP": "ADUANDIN",
            "NAME": "B6I-985",
            "DATETIME": "220505222057"
        },
        {
            "CODE": "U4Y5",
            "GROUP": "LISTOTAX",
            "NAME": "BRA-024",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "U4YC",
            "GROUP": "RENTINCA",
            "NAME": "AVQ-897",
            "DATETIME": "220506114233"
        },
        {
            "CODE": "U4YF",
            "GROUP": "LISTOTAX",
            "NAME": "BWQ-411",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "U4ZU",
            "GROUP": "SUEROS",
            "NAME": "V8R-940",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "U4ZV",
            "GROUP": "CORPESA",
            "NAME": "C4W-784",
            "DATETIME": "220506120403"
        },
        {
            "CODE": "U4ZW",
            "GROUP": "SOLGASTR",
            "NAME": "B4K-995",
            "DATETIME": "220506120348"
        },
        {
            "CODE": "U500",
            "GROUP": "TOÑITO",
            "NAME": "F0T-991",
            "DATETIME": "220505050803"
        },
        {
            "CODE": "U505",
            "GROUP": "SAN MART",
            "NAME": "ACT-904",
            "DATETIME": "220505151709"
        },
        {
            "CODE": "U50A",
            "GROUP": "CONDOR.T",
            "NAME": "D0Y-960",
            "DATETIME": "220506072312"
        },
        {
            "CODE": "U50B",
            "GROUP": "NOR OIL",
            "NAME": "P3Z-850",
            "DATETIME": "220506115545"
        },
        {
            "CODE": "U51P",
            "GROUP": "LISTOTAX",
            "NAME": "BLB-688",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "U520",
            "GROUP": "MAFISA",
            "NAME": "ASU-759",
            "DATETIME": "220506101851"
        },
        {
            "CODE": "U525",
            "GROUP": "SOLGASTR",
            "NAME": "D1J-995",
            "DATETIME": "220425171742"
        },
        {
            "CODE": "U52G",
            "GROUP": "FIERRO",
            "NAME": "BDK-755",
            "DATETIME": "220506120233"
        },
        {
            "CODE": "U52L",
            "GROUP": "RENTINLE",
            "NAME": "BLL-346",
            "DATETIME": "220506113548"
        },
        {
            "CODE": "U52T",
            "GROUP": "ADUANDIN",
            "NAME": "D7N-878",
            "DATETIME": "220506113921"
        },
        {
            "CODE": "U530",
            "GROUP": "LISTOTAX",
            "NAME": "BXM-456",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "U54P",
            "GROUP": "KAMITAL",
            "NAME": "F6H-717",
            "DATETIME": "220506084915"
        },
        {
            "CODE": "U550",
            "GROUP": "FERMINA",
            "NAME": "AZA-923",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "U5AP",
            "GROUP": "ESPAR",
            "NAME": "AVI-161",
            "DATETIME": "220505073754"
        },
        {
            "CODE": "U6PM",
            "GROUP": "FAMESA",
            "NAME": "APP-871",
            "DATETIME": "220506111409"
        },
        {
            "CODE": "U6PN",
            "GROUP": "MYI GLO",
            "NAME": "D2B-424",
            "DATETIME": "220506115454"
        },
        {
            "CODE": "U6PP",
            "GROUP": "NOR OIL",
            "NAME": "BJK-763",
            "DATETIME": "220506114348"
        },
        {
            "CODE": "U6PQ",
            "GROUP": "CONDOR.T",
            "NAME": "F1E-961",
            "DATETIME": "220506072215"
        },
        {
            "CODE": "U6PR",
            "GROUP": "V.CASTRO",
            "NAME": "D8W-389",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "U6PS",
            "GROUP": "MYI GLO",
            "NAME": "D6L-945",
            "DATETIME": "220506114942"
        },
        {
            "CODE": "U6Q3",
            "GROUP": "INTERSEN",
            "NAME": "D9P-922",
            "DATETIME": "220503195606"
        },
        {
            "CODE": "U6QT",
            "GROUP": "QANTU",
            "NAME": "D9A-937",
            "DATETIME": "220506120030"
        },
        {
            "CODE": "U6QY",
            "GROUP": "FAMESA",
            "NAME": "APP-865",
            "DATETIME": "220422142951"
        },
        {
            "CODE": "U6RN",
            "GROUP": "SAN MART",
            "NAME": "BCK-945",
            "DATETIME": "220506120415"
        },
        {
            "CODE": "U6SN",
            "GROUP": "INTERSEN",
            "NAME": "D9Q-729",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "U6SP",
            "GROUP": "FAMESA",
            "NAME": "APP-746",
            "DATETIME": "220503133403"
        },
        {
            "CODE": "U6TD",
            "GROUP": "ESPAR",
            "NAME": "ATI-446",
            "DATETIME": "220506084000"
        },
        {
            "CODE": "U6TE",
            "GROUP": "ESPAR",
            "NAME": "ATP-276",
            "DATETIME": "220506104345"
        },
        {
            "CODE": "U6UQ",
            "GROUP": "ADUANDIN",
            "NAME": "A7N-886",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "U6UZ",
            "GROUP": "COMASUR",
            "NAME": "D1G-765",
            "DATETIME": "220311161200"
        },
        {
            "CODE": "U6V2",
            "GROUP": "TRANSOIL",
            "NAME": "BFS-921",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "U6V9",
            "GROUP": "RENTING",
            "NAME": "AXW-851",
            "DATETIME": "220221180624"
        },
        {
            "CODE": "U6XM",
            "GROUP": "RIMAC",
            "NAME": "AUO-384",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "U6Y2",
            "GROUP": "RIMAC",
            "NAME": "ATU-111",
            "DATETIME": "220505170551"
        },
        {
            "CODE": "U6YA",
            "GROUP": "FORTALEZ",
            "NAME": "AMA-902",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "U6Z8",
            "GROUP": "ACEROS C",
            "NAME": "V9U-787",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "U6ZQ",
            "GROUP": "RENTING",
            "NAME": "AYT-868",
            "DATETIME": "220406163700"
        },
        {
            "CODE": "U701",
            "GROUP": "SELGAS",
            "NAME": "ABO-893",
            "DATETIME": "220505103539"
        },
        {
            "CODE": "U70D",
            "GROUP": "AUTONORT",
            "NAME": "S1V-895",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "U70H",
            "GROUP": "CONDOR.T",
            "NAME": "D0Z-956",
            "DATETIME": "220506075254"
        },
        {
            "CODE": "U70T",
            "GROUP": "PETROL-C",
            "NAME": "ATI-867",
            "DATETIME": "220506112800"
        },
        {
            "CODE": "U713",
            "GROUP": "ENMANUEL",
            "NAME": "ALM-814",
            "DATETIME": "220409112227"
        },
        {
            "CODE": "U8A9",
            "GROUP": "SAN MART",
            "NAME": "F8G-805",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "U8AE",
            "GROUP": "NOR OIL",
            "NAME": "T4U-900",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "U8AG",
            "GROUP": "CARTER",
            "NAME": "BJI-895",
            "DATETIME": "220506073045"
        },
        {
            "CODE": "U8AL",
            "GROUP": "ADUANDIN",
            "NAME": "AHN-772",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "U8AV",
            "GROUP": "RENTING",
            "NAME": "T9H-800",
            "DATETIME": "220506085051"
        },
        {
            "CODE": "U8AZ",
            "GROUP": "SOUTHERN",
            "NAME": "AYQ-797",
            "DATETIME": "220506120336"
        },
        {
            "CODE": "U8B3",
            "GROUP": "ZUÑIGA",
            "NAME": "B6G-835",
            "DATETIME": "220506115121"
        },
        {
            "CODE": "U8BF",
            "GROUP": "PACIFICO",
            "NAME": "ATV-280",
            "DATETIME": "220506120224"
        },
        {
            "CODE": "U8BH",
            "GROUP": "T.FLORES",
            "NAME": "C2B-755",
            "DATETIME": "220506115054"
        },
        {
            "CODE": "U8BR",
            "GROUP": "MORALES",
            "NAME": "F6G-887",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "U8BW",
            "GROUP": "T.FLORES",
            "NAME": "C1R-928",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "U8BX",
            "GROUP": "PAREDES",
            "NAME": "T6V-822",
            "DATETIME": "220506085342"
        },
        {
            "CODE": "U8C5",
            "GROUP": "RENTING",
            "NAME": "BHA-686",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "U8C7",
            "GROUP": "ECONO",
            "NAME": "BAB-771",
            "DATETIME": "220506120400"
        },
        {
            "CODE": "U8CC",
            "GROUP": "SVS TRAN",
            "NAME": "V8W-703",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "U8CE",
            "GROUP": "PART BET",
            "NAME": "V2D-900",
            "DATETIME": "220506114757"
        },
        {
            "CODE": "U8D9",
            "GROUP": "STA ROSA",
            "NAME": "C5Q-986",
            "DATETIME": "220506113939"
        },
        {
            "CODE": "U8DB",
            "GROUP": "AGROTECN",
            "NAME": "T8M-811",
            "DATETIME": "220506120009"
        },
        {
            "CODE": "U8E2",
            "GROUP": "AUTONORT",
            "NAME": "T4D-592",
            "DATETIME": "220506082915"
        },
        {
            "CODE": "U8E6",
            "GROUP": "JESHUA",
            "NAME": "T4B-868",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "U8E8",
            "GROUP": "SOLGAS",
            "NAME": "AJH-843",
            "DATETIME": "220506115709"
        },
        {
            "CODE": "U8ET",
            "GROUP": "T.FLORES",
            "NAME": "C1R-930",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "U8F3",
            "GROUP": "RENTING",
            "NAME": "AWU-932",
            "DATETIME": "220506115218"
        },
        {
            "CODE": "U8F6",
            "GROUP": "GREMPOL",
            "NAME": "F7T-990",
            "DATETIME": "220506092315"
        },
        {
            "CODE": "U8G0",
            "GROUP": "PASQUEL",
            "NAME": "D6Z-494",
            "DATETIME": "220506084442"
        },
        {
            "CODE": "U8ZA",
            "GROUP": "TMC",
            "NAME": "ATN-823",
            "DATETIME": "220506115121"
        },
        {
            "CODE": "U8ZG",
            "GROUP": "TMC",
            "NAME": "ACC-784",
            "DATETIME": "220505190457"
        },
        {
            "CODE": "U8ZS",
            "GROUP": "TMC",
            "NAME": "ATO-825",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "U8ZW",
            "GROUP": "TMC",
            "NAME": "ACC-760",
            "DATETIME": "220506115636"
        },
        {
            "CODE": "U901",
            "GROUP": "TMC",
            "NAME": "APH-924",
            "DATETIME": "220506120033"
        },
        {
            "CODE": "U902",
            "GROUP": "TMC",
            "NAME": "ATN-847",
            "DATETIME": "220506110812"
        },
        {
            "CODE": "U906",
            "GROUP": "TMC",
            "NAME": "ATK-927",
            "DATETIME": "220506113003"
        },
        {
            "CODE": "U90F",
            "GROUP": "TMC",
            "NAME": "ATL-908",
            "DATETIME": "220506115454"
        },
        {
            "CODE": "U9MH",
            "GROUP": "ESPAR ",
            "NAME": "AUF-365",
            "DATETIME": "220505182124"
        },
        {
            "CODE": "U9P2",
            "GROUP": "RENTING",
            "NAME": "AWU-926",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "U9PB",
            "GROUP": "BONALIS",
            "NAME": "AXY-223",
            "DATETIME": "220505174036"
        },
        {
            "CODE": "U9PG",
            "GROUP": "GILDEMEI",
            "NAME": "AUZ-482",
            "DATETIME": "220505180112"
        },
        {
            "CODE": "U9PH",
            "GROUP": "BIDDLE",
            "NAME": "AFK-742",
            "DATETIME": "220506082651"
        },
        {
            "CODE": "U9PJ",
            "GROUP": "MAPFRE",
            "NAME": "AUB-031",
            "DATETIME": "220506120345"
        },
        {
            "CODE": "U9PQ",
            "GROUP": "LISTOTAX",
            "NAME": "BXL-631",
            "DATETIME": "220506115900"
        },
        {
            "CODE": "U9PT",
            "GROUP": "RENTING",
            "NAME": "AWU-883",
            "DATETIME": "220505144945"
        },
        {
            "CODE": "U9PU",
            "GROUP": "CORPESA",
            "NAME": "D4K-843",
            "DATETIME": "220505150415"
        },
        {
            "CODE": "U9Q8",
            "GROUP": "TOÑITO",
            "NAME": "V8V-884",
            "DATETIME": "220506080709"
        },
        {
            "CODE": "U9QH",
            "GROUP": "GILDEMEI",
            "NAME": "AUL-512",
            "DATETIME": "220506074442"
        },
        {
            "CODE": "U9SH",
            "GROUP": "ARYUNA",
            "NAME": "F3J-990",
            "DATETIME": "220506114739"
        },
        {
            "CODE": "U9SM",
            "GROUP": "STA-ROSA",
            "NAME": "AAB-980",
            "DATETIME": "220312203525"
        },
        {
            "CODE": "U9ST",
            "GROUP": "ARYUNA",
            "NAME": "D7T-996",
            "DATETIME": "220506115100"
        },
        {
            "CODE": "UACH",
            "GROUP": "LISTOTAX",
            "NAME": "AZA-393",
            "DATETIME": "220506110242"
        },
        {
            "CODE": "UACL",
            "GROUP": "AUTONORT",
            "NAME": "H2A-559",
            "DATETIME": "220503213939"
        },
        {
            "CODE": "UACR",
            "GROUP": "SHILCAYO",
            "NAME": "ANQ-983",
            "DATETIME": "220506114357"
        },
        {
            "CODE": "UACW",
            "GROUP": "BIDDLE",
            "NAME": "B6X-121",
            "DATETIME": "220219080218"
        },
        {
            "CODE": "UACX",
            "GROUP": "TAXISAT",
            "NAME": "AUA-523",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "UAD3",
            "GROUP": "SELGAS",
            "NAME": "B2W-987",
            "DATETIME": "220506053927"
        },
        {
            "CODE": "UAD5",
            "GROUP": "REPARTO",
            "NAME": "ANO-824",
            "DATETIME": "220506112703"
        },
        {
            "CODE": "UAD6",
            "GROUP": "RIMAC",
            "NAME": "ATY-185",
            "DATETIME": "220505143921"
        },
        {
            "CODE": "UADB",
            "GROUP": "ADUANDIN",
            "NAME": "F4J-998",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "UADG",
            "GROUP": "MAPFRE",
            "NAME": "APQ-870",
            "DATETIME": "220506120054"
        },
        {
            "CODE": "UADN",
            "GROUP": "T.FLORES",
            "NAME": "D2V-902",
            "DATETIME": "220506120133"
        },
        {
            "CODE": "UAED",
            "GROUP": "GILDEMEI",
            "NAME": "AUJ-692",
            "DATETIME": "220503093245"
        },
        {
            "CODE": "UAEL",
            "GROUP": "PRIMERA",
            "NAME": "AUB-319",
            "DATETIME": "220506090221"
        },
        {
            "CODE": "UAEX",
            "GROUP": "GILDEMEI",
            "NAME": "AUP-611",
            "DATETIME": "220506104448"
        },
        {
            "CODE": "UAF9",
            "GROUP": "RIMAC",
            "NAME": "AUM-644 ",
            "DATETIME": "220505184409"
        },
        {
            "CODE": "UAFB",
            "GROUP": "RENTING",
            "NAME": "T9G-931",
            "DATETIME": "220506110257"
        },
        {
            "CODE": "UAFL",
            "GROUP": "ESPAR",
            "NAME": "AUG-606",
            "DATETIME": "220506095821"
        },
        {
            "CODE": "UAFP",
            "GROUP": "CHAVEZ.B",
            "NAME": "AJD-310",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "UAFT",
            "GROUP": "STA-ROSA",
            "NAME": "TBT-979",
            "DATETIME": "220421102800"
        },
        {
            "CODE": "UAFW",
            "GROUP": "TRUCKTIR",
            "NAME": "F6I-400",
            "DATETIME": "220506115521"
        },
        {
            "CODE": "UAGK",
            "GROUP": "GILDEMEI",
            "NAME": "AUM-079",
            "DATETIME": "220505204503"
        },
        {
            "CODE": "UAGM",
            "GROUP": "LISTOTAX",
            "NAME": "BHY-326",
            "DATETIME": "220506120112"
        },
        {
            "CODE": "UAGN",
            "GROUP": "EMTRACOM",
            "NAME": "ANF-983",
            "DATETIME": "220502180606"
        },
        {
            "CODE": "UAGR",
            "GROUP": "TAXI AH",
            "NAME": "ALR-688",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "UAGT",
            "GROUP": "MINERALE",
            "NAME": "ANY-845",
            "DATETIME": "220506120418"
        },
        {
            "CODE": "UAGX",
            "GROUP": "SHILCAYO",
            "NAME": "BET-820",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "UAH2",
            "GROUP": "TRADESUR",
            "NAME": "BCZ-899",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "UAH3",
            "GROUP": "ANDINAPL",
            "NAME": "D2S-722",
            "DATETIME": "220506115600"
        },
        {
            "CODE": "UAH4",
            "GROUP": "LOGVILCH",
            "NAME": "W3C-784",
            "DATETIME": "220417063051"
        },
        {
            "CODE": "UAHB",
            "GROUP": "J LOPEZ",
            "NAME": "F2O-759",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "UAHE",
            "GROUP": "AGREVO",
            "NAME": "BP0-538",
            "DATETIME": "220506114209"
        },
        {
            "CODE": "UAHM",
            "GROUP": "RENTING",
            "NAME": "AWU-804",
            "DATETIME": "220506115809"
        },
        {
            "CODE": "UAHR",
            "GROUP": "SAN MART",
            "NAME": "T8Q-871",
            "DATETIME": "220506114339"
        },
        {
            "CODE": "UAHV",
            "GROUP": "AUTONORT",
            "NAME": "S1D-371",
            "DATETIME": "220501125715"
        },
        {
            "CODE": "UAHX",
            "GROUP": "GILDEMEI",
            "NAME": "AAZ-842",
            "DATETIME": "220506114027"
        },
        {
            "CODE": "UAJA",
            "GROUP": "DIAG.UAL",
            "NAME": "AZA-940",
            "DATETIME": "220506115506"
        },
        {
            "CODE": "UAJB",
            "GROUP": "AUTONORT",
            "NAME": "S1D-368",
            "DATETIME": "220410010718"
        },
        {
            "CODE": "UAJC",
            "GROUP": "ESPAR",
            "NAME": "APT-740",
            "DATETIME": "220506111803"
        },
        {
            "CODE": "UBDG",
            "GROUP": "ESPAR",
            "NAME": "AUL-363",
            "DATETIME": "220506120357"
        },
        {
            "CODE": "UBDU",
            "GROUP": "LINCUNA",
            "NAME": "BAY-863",
            "DATETIME": "220506115157"
        },
        {
            "CODE": "UBEV",
            "GROUP": "MACAVAL",
            "NAME": "BJW-739",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "UBF0",
            "GROUP": "ECOGRAFO",
            "NAME": "ECO1",
            "DATETIME": "220506115848"
        },
        {
            "CODE": "UBF1",
            "GROUP": "ARMI",
            "NAME": "ANR-819",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "UBFQ",
            "GROUP": "GILDEMEI",
            "NAME": "AUO-026",
            "DATETIME": "220506054006"
        },
        {
            "CODE": "UBHD",
            "GROUP": "CORPESA",
            "NAME": "AKI-938",
            "DATETIME": "220506120030"
        },
        {
            "CODE": "UBHE",
            "GROUP": "CORPESA",
            "NAME": "D2C-754",
            "DATETIME": "220315135148"
        },
        {
            "CODE": "UBHH",
            "GROUP": "PRIMERA",
            "NAME": "ARA-752",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "UBHK",
            "GROUP": "IMAN",
            "NAME": "AFQ-731",
            "DATETIME": "220506112857"
        },
        {
            "CODE": "UBHT",
            "GROUP": "GILDEMEI",
            "NAME": "AUS-425",
            "DATETIME": "220506051509"
        },
        {
            "CODE": "UBHV",
            "GROUP": "CORPESA",
            "NAME": "A1W-905",
            "DATETIME": "220506092451"
        },
        {
            "CODE": "UBJ7",
            "GROUP": "ESPAR",
            "NAME": "AUP-584",
            "DATETIME": "220505195830"
        },
        {
            "CODE": "UBJ8",
            "GROUP": "CHAVEZP",
            "NAME": "A8A-801",
            "DATETIME": "220506094957"
        },
        {
            "CODE": "UBJD",
            "GROUP": "ENERLETR",
            "NAME": "AWJ-856",
            "DATETIME": "220506092236"
        },
        {
            "CODE": "UBJZ",
            "GROUP": "INACTIVO",
            "NAME": "A0D-864",
            "DATETIME": "220429064224"
        },
        {
            "CODE": "UBK3",
            "GROUP": "ORETEL",
            "NAME": "D5O-979",
            "DATETIME": "220506115942"
        },
        {
            "CODE": "UC1S",
            "GROUP": "DIAG.UAL",
            "NAME": "BHE-205",
            "DATETIME": "220506114721"
        },
        {
            "CODE": "UC2C",
            "GROUP": "RENTING",
            "NAME": "AVU-724",
            "DATETIME": "220505153245"
        },
        {
            "CODE": "UC32",
            "GROUP": "RIMAC",
            "NAME": "AVG-327",
            "DATETIME": "220506094027"
        },
        {
            "CODE": "UC3G",
            "GROUP": "INTERSEN",
            "NAME": "C9Y-938",
            "DATETIME": "220427171327"
        },
        {
            "CODE": "UC3R",
            "GROUP": "GILDEMEI",
            "NAME": "AUU-450",
            "DATETIME": "220506073809"
        },
        {
            "CODE": "UC4E",
            "GROUP": "GILDEMEI",
            "NAME": "AUY-350",
            "DATETIME": "220505174857"
        },
        {
            "CODE": "UC4G",
            "GROUP": "PACIFICO",
            "NAME": "H1S-917",
            "DATETIME": "220506075209"
        },
        {
            "CODE": "UC4R",
            "GROUP": "POSITIVA",
            "NAME": "H2O-881",
            "DATETIME": "220506101306"
        },
        {
            "CODE": "UC54",
            "GROUP": "GILDEMEI",
            "NAME": "ARI-737",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "UC59",
            "GROUP": "GILDEMEI",
            "NAME": "AUX-685",
            "DATETIME": "220506065839"
        },
        {
            "CODE": "UC6H",
            "GROUP": "T.ZEVALL",
            "NAME": "573120",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "UC6L",
            "GROUP": "COMASUR",
            "NAME": "P4B-895",
            "DATETIME": "220506114115"
        },
        {
            "CODE": "UC7F",
            "GROUP": "MAPFRE",
            "NAME": "ARH-719",
            "DATETIME": "220506105624"
        },
        {
            "CODE": "UC7L",
            "GROUP": "FCG",
            "NAME": "F2K-935",
            "DATETIME": "220506120309"
        },
        {
            "CODE": "UC80",
            "GROUP": "SAGA",
            "NAME": "BHC-881",
            "DATETIME": "220506083218"
        },
        {
            "CODE": "UCAG",
            "GROUP": "ALCIDESF",
            "NAME": "AMP-614",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "UCAQ",
            "GROUP": "VILLENA",
            "NAME": "APK-703",
            "DATETIME": "220506120333"
        },
        {
            "CODE": "UCAU",
            "GROUP": "VILLENA",
            "NAME": "BEY-746",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "UCB3",
            "GROUP": "VILLENA",
            "NAME": "C9D-745",
            "DATETIME": "220503133151"
        },
        {
            "CODE": "UCBX",
            "GROUP": "RIMAC",
            "NAME": "AUM-432",
            "DATETIME": "220504104739"
        },
        {
            "CODE": "UCC8",
            "GROUP": "ESPAR",
            "NAME": "AUX-066",
            "DATETIME": "220506114527"
        },
        {
            "CODE": "UCD7",
            "GROUP": "OLIVARES",
            "NAME": "AAH-880",
            "DATETIME": "220506115251"
        },
        {
            "CODE": "UCDD",
            "GROUP": "OLIVARES",
            "NAME": "AAL-882",
            "DATETIME": "220506114254"
        },
        {
            "CODE": "UCDG",
            "GROUP": "LISTOTAX",
            "NAME": "BHD-306",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "UCE4",
            "GROUP": "MORALES",
            "NAME": "B6H-819",
            "DATETIME": "220506120436"
        },
        {
            "CODE": "UCEM",
            "GROUP": "RENTING",
            "NAME": "AWV-768",
            "DATETIME": "220506114739"
        },
        {
            "CODE": "UCEU",
            "GROUP": "PART BET",
            "NAME": "C5F-753",
            "DATETIME": "220506115148"
        },
        {
            "CODE": "UCF0",
            "GROUP": "EMTRACOM",
            "NAME": "ARC-995",
            "DATETIME": "220505182006"
        },
        {
            "CODE": "UCFF",
            "GROUP": "ESPAR",
            "NAME": "ARR-757",
            "DATETIME": "220506100209"
        },
        {
            "CODE": "UCFW",
            "GROUP": "LISTOTAX",
            "NAME": "BXO-220",
            "DATETIME": "220506115530"
        },
        {
            "CODE": "UCL0",
            "GROUP": "A&J",
            "NAME": "ANH-809",
            "DATETIME": "220506103733"
        },
        {
            "CODE": "UCL4",
            "GROUP": "OLIVARES",
            "NAME": "AAG-876",
            "DATETIME": "220506115154"
        },
        {
            "CODE": "UCL6",
            "GROUP": "LISTOTAX",
            "NAME": "BWU-302",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "UCL7",
            "GROUP": "OLIVARES",
            "NAME": "AAH-874",
            "DATETIME": "220506120130"
        },
        {
            "CODE": "UCLC",
            "GROUP": "CEDROS",
            "NAME": "B7Q-822",
            "DATETIME": "220506111636"
        },
        {
            "CODE": "UCLD",
            "GROUP": "RENTING",
            "NAME": "BFA-051",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "UCLF",
            "GROUP": "SELGAS",
            "NAME": "F7F-705",
            "DATETIME": "220506120157"
        },
        {
            "CODE": "UCLH",
            "GROUP": "OLIVARES",
            "NAME": "AYT-892",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "UCM5",
            "GROUP": "ESPAR",
            "NAME": "AVQ-594",
            "DATETIME": "220506075542"
        },
        {
            "CODE": "UCMM",
            "GROUP": "SELGAS",
            "NAME": "F6X-875",
            "DATETIME": "220505154018"
        },
        {
            "CODE": "UCN6",
            "GROUP": "PART BET",
            "NAME": "ARS-785",
            "DATETIME": "220506104536"
        },
        {
            "CODE": "UCPH",
            "GROUP": "OLIVARES",
            "NAME": "AYU-713",
            "DATETIME": "220506120248"
        },
        {
            "CODE": "UCQA",
            "GROUP": "INTERSEN",
            "NAME": "AYP-829",
            "DATETIME": "220506114421"
        },
        {
            "CODE": "UCQE",
            "GROUP": "RIMAC",
            "NAME": "AVC-593",
            "DATETIME": "220506105924"
        },
        {
            "CODE": "UCQH",
            "GROUP": "PART BET",
            "NAME": "ARU-777",
            "DATETIME": "220506114324"
        },
        {
            "CODE": "UCQR",
            "GROUP": "GBORRA",
            "NAME": "AUI-274",
            "DATETIME": "220505171236"
        },
        {
            "CODE": "UCQX",
            "GROUP": "MORALES",
            "NAME": "F6H-734",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "UCR4",
            "GROUP": "RENTING",
            "NAME": "AWO-898",
            "DATETIME": "220505134427"
        },
        {
            "CODE": "UCRC",
            "GROUP": "OLIVARES",
            "NAME": "AAH-819",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "UCS2",
            "GROUP": "IMARK",
            "NAME": "APS-879",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "UCS3",
            "GROUP": "ESPAR ",
            "NAME": "AVD-073",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "UCSJ",
            "GROUP": "MARYORIC",
            "NAME": "ARK-916",
            "DATETIME": "220506113909"
        },
        {
            "CODE": "UCTG",
            "GROUP": "PACIFICO",
            "NAME": "AVK-363",
            "DATETIME": "220505184233"
        },
        {
            "CODE": "UCTJ",
            "GROUP": "GILDEMEI",
            "NAME": "AVC-120",
            "DATETIME": "220505180903"
        },
        {
            "CODE": "UCTX",
            "GROUP": "ESPAR",
            "NAME": "AVE-046",
            "DATETIME": "220505232007"
        },
        {
            "CODE": "UCVF",
            "GROUP": "ESPAR",
            "NAME": "AVA-640",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "UDSX",
            "GROUP": "PART BET",
            "NAME": "AWS-144",
            "DATETIME": "220506114400"
        },
        {
            "CODE": "UDWS",
            "GROUP": "TYS ANA ",
            "NAME": "V5N-989",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "UEL1",
            "GROUP": "BEST POR",
            "NAME": "B4V-775",
            "DATETIME": "220109062727"
        },
        {
            "CODE": "UEL9",
            "GROUP": "RIMAC",
            "NAME": "AVS-223",
            "DATETIME": "220505140136"
        },
        {
            "CODE": "UELB",
            "GROUP": "PART BET",
            "NAME": "AWC-660",
            "DATETIME": "220505215124"
        },
        {
            "CODE": "UELS",
            "GROUP": "ALCIDESF",
            "NAME": "AWB-328",
            "DATETIME": "220505232430"
        },
        {
            "CODE": "UELW",
            "GROUP": "LISTOTAX",
            "NAME": "BAR-026",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "UEM0",
            "GROUP": "CRISTALU",
            "NAME": "BBP-141",
            "DATETIME": "220506110454"
        },
        {
            "CODE": "UEM3",
            "GROUP": "MACROSIG",
            "NAME": "BEY-706",
            "DATETIME": "220506102451"
        },
        {
            "CODE": "UEME",
            "GROUP": "POSITIVA",
            "NAME": "ANU-596",
            "DATETIME": "220506114333"
        },
        {
            "CODE": "UENP",
            "GROUP": "SHILCAYO",
            "NAME": "AVJ-817",
            "DATETIME": "220506114209"
        },
        {
            "CODE": "UEP0",
            "GROUP": "FAMAI",
            "NAME": "V9B-797",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "UEP3",
            "GROUP": "AUTONORT",
            "NAME": "T4H-381",
            "DATETIME": "220506112330"
        },
        {
            "CODE": "UEP7",
            "GROUP": "LINCUNA",
            "NAME": "BAZ-861",
            "DATETIME": "220506115839"
        },
        {
            "CODE": "UEPN",
            "GROUP": "FAMAI",
            "NAME": "V9B-739",
            "DATETIME": "220506084827"
        },
        {
            "CODE": "UEQG",
            "GROUP": "TRUCKTEA",
            "NAME": "V9S-860",
            "DATETIME": "220506120233"
        },
        {
            "CODE": "UEQH",
            "GROUP": "GILDEMEI",
            "NAME": "AVZ-510",
            "DATETIME": "220505211842"
        },
        {
            "CODE": "UER3",
            "GROUP": "RENTING",
            "NAME": "AUV-870",
            "DATETIME": "220506110742"
        },
        {
            "CODE": "UER9",
            "GROUP": "GILDEMEI",
            "NAME": "AVZ-125",
            "DATETIME": "220506094512"
        },
        {
            "CODE": "UERG",
            "GROUP": "DAGA",
            "NAME": "AWM-135",
            "DATETIME": "220506003409"
        },
        {
            "CODE": "UERP",
            "GROUP": "GILDEMEI",
            "NAME": "AVX-396",
            "DATETIME": "220506072651"
        },
        {
            "CODE": "UERW",
            "GROUP": "G.GEMEVA",
            "NAME": "T2G-909",
            "DATETIME": "220506070957"
        },
        {
            "CODE": "UERY",
            "GROUP": "EMTRACOM",
            "NAME": "ALM-990",
            "DATETIME": "220506113157"
        },
        {
            "CODE": "UES7",
            "GROUP": "SLI",
            "NAME": "AFZ-905",
            "DATETIME": "220505142157"
        },
        {
            "CODE": "UESH",
            "GROUP": "ORELLANA",
            "NAME": "A6M-989",
            "DATETIME": "220506104551"
        },
        {
            "CODE": "UESM",
            "GROUP": "LISTOTAX",
            "NAME": "BJK-238",
            "DATETIME": "220506120354"
        },
        {
            "CODE": "UESQ",
            "GROUP": "FCG",
            "NAME": "ASD-841",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "UESR",
            "GROUP": "LISTOTAX",
            "NAME": "BWS-325",
            "DATETIME": "220505165833"
        },
        {
            "CODE": "UET4",
            "GROUP": "GEMEVA",
            "NAME": "T3B-834",
            "DATETIME": "220506115227"
        },
        {
            "CODE": "UETQ",
            "GROUP": "T.SANTOS",
            "NAME": "BKN-725",
            "DATETIME": "220506061324"
        },
        {
            "CODE": "UETW",
            "GROUP": "RENTINCA",
            "NAME": "CATERP04",
            "DATETIME": "220401194527"
        },
        {
            "CODE": "UEVK",
            "GROUP": "MAPFRE",
            "NAME": "ATR-339",
            "DATETIME": "220204045618"
        },
        {
            "CODE": "UEWJ",
            "GROUP": "SOLGASTR",
            "NAME": "D1J-999",
            "DATETIME": "220506115900"
        },
        {
            "CODE": "UEWK",
            "GROUP": "ESPAR ",
            "NAME": "AWG-114",
            "DATETIME": "220506080015"
        },
        {
            "CODE": "UEWL",
            "GROUP": "NOR OIL",
            "NAME": "T6F-925",
            "DATETIME": "220506120154"
        },
        {
            "CODE": "UEWT",
            "GROUP": "FAMAI",
            "NAME": "V9B-735",
            "DATETIME": "220506115539"
        },
        {
            "CODE": "UEWU",
            "GROUP": "RIMAC",
            "NAME": "AVW-206",
            "DATETIME": "220506113806"
        },
        {
            "CODE": "UEXA",
            "GROUP": "RENTINCA",
            "NAME": "CATERP02",
            "DATETIME": "220506115836"
        },
        {
            "CODE": "UEXB",
            "GROUP": "RENTINCA",
            "NAME": "CATERP03",
            "DATETIME": "220506065857"
        },
        {
            "CODE": "UEXC",
            "GROUP": "RENTING",
            "NAME": "AWO-913",
            "DATETIME": "220506120527"
        },
        {
            "CODE": "UEXZ",
            "GROUP": "AUTONORT",
            "NAME": "M4G-391",
            "DATETIME": "220325150136"
        },
        {
            "CODE": "UEYY",
            "GROUP": "SAN MART",
            "NAME": "D4G-863",
            "DATETIME": "220304121524"
        },
        {
            "CODE": "UEZA",
            "GROUP": "MAPFRE",
            "NAME": "ATV-174",
            "DATETIME": "220506084818"
        },
        {
            "CODE": "UEZD",
            "GROUP": "ENERLETR",
            "NAME": "AWJ-880",
            "DATETIME": "220506120357"
        },
        {
            "CODE": "UEZG",
            "GROUP": "AUTONORT",
            "NAME": "H2Q-860",
            "DATETIME": "220505184100"
        },
        {
            "CODE": "UEZP",
            "GROUP": "PACIFICO",
            "NAME": "AUH-041",
            "DATETIME": "220506083051"
        },
        {
            "CODE": "UEZV",
            "GROUP": "T.EMNA",
            "NAME": "ARE-770",
            "DATETIME": "220505185909"
        },
        {
            "CODE": "W0JZ",
            "GROUP": "LISTOTAX",
            "NAME": "BRA-021",
            "DATETIME": "220506115121"
        },
        {
            "CODE": "W0K9",
            "GROUP": "RIMAC",
            "NAME": "AMI-809",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "W0KK",
            "GROUP": "RENTINLE",
            "NAME": "BLK-668",
            "DATETIME": "220506111233"
        },
        {
            "CODE": "W0KR",
            "GROUP": "ANDINAPL",
            "NAME": "BDM-894",
            "DATETIME": "220506115924"
        },
        {
            "CODE": "W0KV",
            "GROUP": "ESVICSAC",
            "NAME": "ANP-303",
            "DATETIME": "220506114309"
        },
        {
            "CODE": "W0L0",
            "GROUP": "ESVICSAC",
            "NAME": "ALT-935",
            "DATETIME": "220506120042"
        },
        {
            "CODE": "W0L2",
            "GROUP": "ESVICSAC",
            "NAME": "ANQ-184",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "W0L4",
            "GROUP": "ESVICSAC",
            "NAME": "ANQ-394",
            "DATETIME": "220506115818"
        },
        {
            "CODE": "W0L5",
            "GROUP": "SAN MART",
            "NAME": "D4N-839",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "W0L7",
            "GROUP": "FORTALEZ",
            "NAME": "AMB-727",
            "DATETIME": "220506114745"
        },
        {
            "CODE": "W0L8",
            "GROUP": "FORTALEZ",
            "NAME": "BJF-933",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "W0L9",
            "GROUP": "ESVICSAC",
            "NAME": "ANQ-300",
            "DATETIME": "220506115606"
        },
        {
            "CODE": "W0LA",
            "GROUP": "ESVICSAC",
            "NAME": "ALT-701",
            "DATETIME": "220506115415"
        },
        {
            "CODE": "W0LC",
            "GROUP": "FORTALEZ",
            "NAME": "AMA-928",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "W0LD",
            "GROUP": "SAGA",
            "NAME": "BHB-709",
            "DATETIME": "220506113357"
        },
        {
            "CODE": "W0LE",
            "GROUP": "FORTALEZ",
            "NAME": "AMB-783",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "W0LK",
            "GROUP": "ESVICSAC",
            "NAME": "B1B-780",
            "DATETIME": "220506120027"
        },
        {
            "CODE": "W0LM",
            "GROUP": "FORTALEZ",
            "NAME": "AMA-802",
            "DATETIME": "220506115109"
        },
        {
            "CODE": "W0LQ",
            "GROUP": "NOR OIL",
            "NAME": "T6F-938",
            "DATETIME": "220506115027"
        },
        {
            "CODE": "W0LS",
            "GROUP": "RENTANOR",
            "NAME": "T7V-822",
            "DATETIME": "220506093415"
        },
        {
            "CODE": "W0ME",
            "GROUP": "ESVICSAC",
            "NAME": "ANO-667",
            "DATETIME": "220502082633"
        },
        {
            "CODE": "W0MJ",
            "GROUP": "FORTALEZ",
            "NAME": "AMA-819",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "W0MK",
            "GROUP": "VILLENA",
            "NAME": "B7S-847",
            "DATETIME": "220506120133"
        },
        {
            "CODE": "W0MS",
            "GROUP": "FAMESA",
            "NAME": "AMY-932",
            "DATETIME": "220421150303"
        },
        {
            "CODE": "W0MW",
            "GROUP": "ASZTRANS",
            "NAME": "B6G-832",
            "DATETIME": "220506120321"
        },
        {
            "CODE": "W0N3",
            "GROUP": "MAPFRE",
            "NAME": "APQ-190",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "W0NM",
            "GROUP": "RIMAC",
            "NAME": "APJ-443",
            "DATETIME": "220506120000"
        },
        {
            "CODE": "W0NS",
            "GROUP": "LISTOTAX",
            "NAME": "BJA-276",
            "DATETIME": "220505183515"
        },
        {
            "CODE": "W0NX",
            "GROUP": "SERV JTC",
            "NAME": "ANW-380",
            "DATETIME": "220506102954"
        },
        {
            "CODE": "W0P9",
            "GROUP": "POMA",
            "NAME": "D3U-705",
            "DATETIME": "220506094939"
        },
        {
            "CODE": "W0PP",
            "GROUP": "LISTOTAX",
            "NAME": "BWU-387",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "W0PQ",
            "GROUP": "VILCA",
            "NAME": "AMI-754",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "W0PV",
            "GROUP": "PAREDES",
            "NAME": "T0W-834",
            "DATETIME": "220506090130"
        },
        {
            "CODE": "W0PX",
            "GROUP": "RIMAC",
            "NAME": "APS-234",
            "DATETIME": "220505155300"
        },
        {
            "CODE": "W0Q1",
            "GROUP": "ELIZABET",
            "NAME": "F8Q-836",
            "DATETIME": "220506065509"
        },
        {
            "CODE": "W0Q7",
            "GROUP": "T.SANTOS",
            "NAME": "AXF-924",
            "DATETIME": "220506040124"
        },
        {
            "CODE": "W0QA",
            "GROUP": "ESVICSAC",
            "NAME": "ANQ-667",
            "DATETIME": "220506113718"
        },
        {
            "CODE": "W0QF",
            "GROUP": "ESVICSAC",
            "NAME": "B1S-345",
            "DATETIME": "220506115827"
        },
        {
            "CODE": "W0QG",
            "GROUP": "ESVICSAC",
            "NAME": "B9D-933",
            "DATETIME": "220506113921"
        },
        {
            "CODE": "W0QP",
            "GROUP": "INGINOR",
            "NAME": "BCF-823",
            "DATETIME": "220506115703"
        },
        {
            "CODE": "W0QQ",
            "GROUP": "AUTONORT",
            "NAME": "M5T-780",
            "DATETIME": "220506113148"
        },
        {
            "CODE": "W0QR",
            "GROUP": "SANAM",
            "NAME": "UCAYALI1",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "W0QY",
            "GROUP": "T. VICKY",
            "NAME": "BFK-743",
            "DATETIME": "220506113812"
        },
        {
            "CODE": "W0R7",
            "GROUP": "P.CONTAI",
            "NAME": "APU-136",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "W0S1",
            "GROUP": "AGREVO",
            "NAME": "AMF-217",
            "DATETIME": "220506120139"
        },
        {
            "CODE": "W0S2",
            "GROUP": "JYSCORP",
            "NAME": "B5K-783",
            "DATETIME": "220506101657"
        },
        {
            "CODE": "W0S4",
            "GROUP": "LISTOTAX",
            "NAME": "BRA-580",
            "DATETIME": "220505092157"
        },
        {
            "CODE": "W0SC",
            "GROUP": "LISTOTAX",
            "NAME": "BAW-555",
            "DATETIME": "220505212109"
        },
        {
            "CODE": "W0SD",
            "GROUP": "LISTOTAX",
            "NAME": "BNG-012",
            "DATETIME": "220506114524"
        },
        {
            "CODE": "W0SK",
            "GROUP": "OLIVARES",
            "NAME": "AAH-911",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "W0SM",
            "GROUP": "PART BET",
            "NAME": "T3W-597",
            "DATETIME": "220506115721"
        },
        {
            "CODE": "W0T1",
            "GROUP": "CARGAMYM",
            "NAME": "C4P-847",
            "DATETIME": "220506120239"
        },
        {
            "CODE": "W0TK",
            "GROUP": "LISTOTAX",
            "NAME": "BXN-365",
            "DATETIME": "220506120351"
        },
        {
            "CODE": "W0TQ",
            "GROUP": "A&J",
            "NAME": "ANF-729",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "Z24Z",
            "GROUP": "CESEL",
            "NAME": "BJT-651",
            "DATETIME": "220428182333"
        },
        {
            "CODE": "Z252",
            "GROUP": "PROCARGO",
            "NAME": "B4C-863",
            "DATETIME": "220504183245"
        },
        {
            "CODE": "Z256",
            "GROUP": "SOLGASTR",
            "NAME": "B0D-999",
            "DATETIME": "220103162424"
        },
        {
            "CODE": "Z25C",
            "GROUP": "PROCARGO",
            "NAME": "C1K-927",
            "DATETIME": "220504204151"
        },
        {
            "CODE": "Z25U",
            "GROUP": "PROCARGO",
            "NAME": "D2Y-908",
            "DATETIME": "220501193648"
        },
        {
            "CODE": "Z25X",
            "GROUP": "PROCARGO",
            "NAME": "B4I-797",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "Z265",
            "GROUP": "NEGERIB",
            "NAME": "A7J-978",
            "DATETIME": "220506114715"
        },
        {
            "CODE": "Z26E",
            "GROUP": "TRANSJ&M",
            "NAME": "ACA-936",
            "DATETIME": "220506120130"
        },
        {
            "CODE": "Z26X",
            "GROUP": "J.C.A.",
            "NAME": "A5K-838",
            "DATETIME": "220506112133"
        },
        {
            "CODE": "Z271",
            "GROUP": "PART BET",
            "NAME": "B3W-054",
            "DATETIME": "220430130518"
        },
        {
            "CODE": "Z27D",
            "GROUP": "M.INFANT",
            "NAME": "B6Z-932",
            "DATETIME": "220422061551"
        },
        {
            "CODE": "Z27E",
            "GROUP": "G.GEMEVA",
            "NAME": "T7F-841",
            "DATETIME": "220506113715"
        },
        {
            "CODE": "Z27G",
            "GROUP": "INYEPLAS",
            "NAME": "AAF-624",
            "DATETIME": "220506071551"
        },
        {
            "CODE": "Z27P",
            "GROUP": "JM PANDU",
            "NAME": "B0R-976",
            "DATETIME": "220420070527"
        },
        {
            "CODE": "Z51A",
            "GROUP": "POSITIVA",
            "NAME": "BAY-577",
            "DATETIME": "220505151606"
        },
        {
            "CODE": "Z51L",
            "GROUP": "MAPFRE",
            "NAME": "ACT-600",
            "DATETIME": "220506075327"
        },
        {
            "CODE": "Z51W",
            "GROUP": "COMERCIA",
            "NAME": "BEL-073",
            "DATETIME": "220506075324"
        },
        {
            "CODE": "Z532",
            "GROUP": "ESPAR",
            "NAME": "ADV-514",
            "DATETIME": "220430170821"
        },
        {
            "CODE": "Z54G",
            "GROUP": "PNP",
            "NAME": "AZA-054",
            "DATETIME": "220505094409"
        },
        {
            "CODE": "Z57P",
            "GROUP": "POSITIVA",
            "NAME": "T7O-806",
            "DATETIME": "220506111330"
        },
        {
            "CODE": "ZCZ0",
            "GROUP": "STA-ROSA",
            "NAME": "TFT-997",
            "DATETIME": "220506115342"
        },
        {
            "CODE": "ZCZ1",
            "GROUP": "CONSTRUC",
            "NAME": "AXJ-900",
            "DATETIME": "220506120324"
        },
        {
            "CODE": "ZCZ5",
            "GROUP": "DIAG.UAL",
            "NAME": "ASG-230",
            "DATETIME": "220427165424"
        },
        {
            "CODE": "ZCZ7",
            "GROUP": "ENERGIGA",
            "NAME": "VBT-974",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "ZCZ8",
            "GROUP": "RENTING",
            "NAME": "AUU-940",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "ZCZD",
            "GROUP": "SSAT",
            "NAME": "C1-9604",
            "DATETIME": "220506035524"
        },
        {
            "CODE": "ZCZK",
            "GROUP": "OROGAS",
            "NAME": "B7G-983",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "ZCZL",
            "GROUP": "RENTING",
            "NAME": "BEG-597",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "ZCZM",
            "GROUP": "A&J",
            "NAME": "ANE-933",
            "DATETIME": "220506084900"
        },
        {
            "CODE": "ZCZT",
            "GROUP": "REPARTO",
            "NAME": "AYT-848",
            "DATETIME": "220506114742"
        },
        {
            "CODE": "ZCZU",
            "GROUP": "ARONI",
            "NAME": "A4G-846",
            "DATETIME": "220506115336"
        },
        {
            "CODE": "ZD0P",
            "GROUP": "ESPAR",
            "NAME": "AFA-471",
            "DATETIME": "220505180557"
        },
        {
            "CODE": "ZD17",
            "GROUP": "PALACIN",
            "NAME": "AHE-709",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "ZD1C",
            "GROUP": "RENTING",
            "NAME": "AWA-707",
            "DATETIME": "220506120439"
        },
        {
            "CODE": "ZD1E",
            "GROUP": "POSITIVA",
            "NAME": "P2A-931",
            "DATETIME": "220506115854"
        },
        {
            "CODE": "ZD1R",
            "GROUP": "POSITIVA",
            "NAME": "Y1R-198",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "ZD20",
            "GROUP": "MORALES",
            "NAME": "B5W-847",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "ZD25",
            "GROUP": "ACEROS C",
            "NAME": "V9U-785",
            "DATETIME": "220506113839"
        },
        {
            "CODE": "ZD28",
            "GROUP": "TRUCKTIR",
            "NAME": "A6C-580",
            "DATETIME": "220506073039"
        },
        {
            "CODE": "ZD2C",
            "GROUP": "NOR OIL",
            "NAME": "T4U-824",
            "DATETIME": "220506115833"
        },
        {
            "CODE": "ZD2J",
            "GROUP": "LISTOTAX",
            "NAME": "BJB-611",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "ZD3E",
            "GROUP": "FERMINA",
            "NAME": "ASJ-791",
            "DATETIME": "220506115345"
        },
        {
            "CODE": "ZD3N",
            "GROUP": "TRUCKTIR",
            "NAME": "AEI-890",
            "DATETIME": "220506113054"
        },
        {
            "CODE": "ZD3Q",
            "GROUP": "TMC",
            "NAME": "APH-890",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "ZD47",
            "GROUP": "PNP",
            "NAME": "EGP-669",
            "DATETIME": "220506084912"
        },
        {
            "CODE": "ZD4A",
            "GROUP": "SHILCAYO",
            "NAME": "BBT-754",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "ZD4M",
            "GROUP": "RENTANOR",
            "NAME": "F1M-966",
            "DATETIME": "220424104839"
        },
        {
            "CODE": "ZGA8",
            "GROUP": "ADUANDIN",
            "NAME": "BPE-718",
            "DATETIME": "220506083527"
        },
        {
            "CODE": "ZGAA",
            "GROUP": "COMASUR",
            "NAME": "D3R-874",
            "DATETIME": "220506072803"
        },
        {
            "CODE": "ZGAW",
            "GROUP": "ACEROS C",
            "NAME": "V9U-742",
            "DATETIME": "220506103009"
        },
        {
            "CODE": "ZGB9",
            "GROUP": "CORINSER",
            "NAME": "ALB-909",
            "DATETIME": "220506085536"
        },
        {
            "CODE": "ZGBC",
            "GROUP": "JESHUA",
            "NAME": "P3Y-825",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "ZGBG",
            "GROUP": "LISTOTAX",
            "NAME": "BHX-302",
            "DATETIME": "220506062851"
        },
        {
            "CODE": "ZGBU",
            "GROUP": "SHILCAYO",
            "NAME": "C6N-976",
            "DATETIME": "220506114257"
        },
        {
            "CODE": "ZGC0",
            "GROUP": "SLI",
            "NAME": "AVY-741",
            "DATETIME": "220506114730"
        },
        {
            "CODE": "ZGC2",
            "GROUP": "POSITIVA",
            "NAME": "AKD-277",
            "DATETIME": "220506120409"
        },
        {
            "CODE": "ZGC4",
            "GROUP": "INTERSEN",
            "NAME": "D9Q-914",
            "DATETIME": "220120162836"
        },
        {
            "CODE": "ZGCR",
            "GROUP": "MORALES",
            "NAME": "AHI-840",
            "DATETIME": "220506115821"
        },
        {
            "CODE": "ZGCV",
            "GROUP": "ENERLETR",
            "NAME": "AWJ-739",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "ZGD8",
            "GROUP": "STA-ROSA",
            "NAME": "D2B-789",
            "DATETIME": "220506114430"
        },
        {
            "CODE": "ZGDB",
            "GROUP": "A&J",
            "NAME": "ANF-777",
            "DATETIME": "220506114945"
        },
        {
            "CODE": "ZGDN",
            "GROUP": "BONALIS",
            "NAME": "RIL-970",
            "DATETIME": "220505115912"
        },
        {
            "CODE": "ZGDP",
            "GROUP": "PAREDES",
            "NAME": "T5V-847",
            "DATETIME": "220506115245"
        },
        {
            "CODE": "ZGDU",
            "GROUP": "CORPESA",
            "NAME": "ABO-553",
            "DATETIME": "220506115312"
        },
        {
            "CODE": "ZGDZ",
            "GROUP": "ACEROS C",
            "NAME": "V9U-791",
            "DATETIME": "220506120400"
        },
        {
            "CODE": "ZGE3",
            "GROUP": "ENERLETR",
            "NAME": "AWJ-881",
            "DATETIME": "220506101427"
        },
        {
            "CODE": "ZGE8",
            "GROUP": "DIAG.UAL",
            "NAME": "BHC-035",
            "DATETIME": "220506112918"
        },
        {
            "CODE": "ZGED",
            "GROUP": "GILDEMEI",
            "NAME": "BHN-318",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "ZGEE",
            "GROUP": "BIDDLE",
            "NAME": "C8L-713",
            "DATETIME": "220408104457"
        },
        {
            "CODE": "ZGEK",
            "GROUP": "QANTU",
            "NAME": "AEY-907",
            "DATETIME": "220118152254"
        },
        {
            "CODE": "ZGET",
            "GROUP": "VIA FOOD",
            "NAME": "BAY-743",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "ZGEW",
            "GROUP": "A&J",
            "NAME": "ANK-830",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "ZGEX",
            "GROUP": "INTERSEN",
            "NAME": "D9P-769",
            "DATETIME": "220506114927"
        },
        {
            "CODE": "ZGF7",
            "GROUP": "TAXI AH",
            "NAME": "D2K-353",
            "DATETIME": "220506115418"
        },
        {
            "CODE": "ZGFA",
            "GROUP": "TYS VALE",
            "NAME": "W5A-966",
            "DATETIME": "220506083854"
        },
        {
            "CODE": "ZGFD",
            "GROUP": "RENTINLE",
            "NAME": "BHB-115",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "ZGFJ",
            "GROUP": "V.CASTRO",
            "NAME": "AFY-640",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "ZGFK",
            "GROUP": "SOLGASTR",
            "NAME": "A7Z-978",
            "DATETIME": "220326132336"
        },
        {
            "CODE": "ZGFN",
            "GROUP": "ACOSTA",
            "NAME": "ANM-824",
            "DATETIME": "220506114212"
        },
        {
            "CODE": "ZGFT",
            "GROUP": "RENTINLE",
            "NAME": "BHB-116",
            "DATETIME": "220506120248"
        },
        {
            "CODE": "ZGFW",
            "GROUP": "ROQUE",
            "NAME": "C6C-726",
            "DATETIME": "220506114245"
        },
        {
            "CODE": "ZGG5",
            "GROUP": "V.CASTRO",
            "NAME": "AKM-131",
            "DATETIME": "220506120215"
        },
        {
            "CODE": "ZGGD",
            "GROUP": "PAREDES",
            "NAME": "T8M-894",
            "DATETIME": "220506113948"
        },
        {
            "CODE": "ZHBK",
            "GROUP": "PTRANQUI",
            "NAME": "F2X-651",
            "DATETIME": "220506120515"
        },
        {
            "CODE": "ZHBW",
            "GROUP": "LISTOTAX",
            "NAME": "BWV-670",
            "DATETIME": "220506120012"
        },
        {
            "CODE": "ZHBX",
            "GROUP": "RENTINCA",
            "NAME": "AVQ-819",
            "DATETIME": "220506115436"
        },
        {
            "CODE": "ZHC8",
            "GROUP": "RENTING",
            "NAME": "BHD-340",
            "DATETIME": "220506114424"
        },
        {
            "CODE": "ZHCP",
            "GROUP": "BIDDLE",
            "NAME": "D4K-835",
            "DATETIME": "220505143836"
        },
        {
            "CODE": "ZHCV",
            "GROUP": "BIDDLE",
            "NAME": "D6N-949",
            "DATETIME": "220428144733"
        },
        {
            "CODE": "ZHD2",
            "GROUP": "NOR OIL",
            "NAME": "T6D-871",
            "DATETIME": "220506120227"
        },
        {
            "CODE": "ZHD6",
            "GROUP": "CORPESA",
            "NAME": "D1A-784",
            "DATETIME": "220506101815"
        },
        {
            "CODE": "ZHDA",
            "GROUP": "VILCA HN",
            "NAME": "W5V-738",
            "DATETIME": "220506075724"
        },
        {
            "CODE": "ZHDD",
            "GROUP": "CORPESA",
            "NAME": "A0R-746",
            "DATETIME": "220322170403"
        },
        {
            "CODE": "ZHDK",
            "GROUP": "BIDDLE",
            "NAME": "D6O-800",
            "DATETIME": "220506114427"
        },
        {
            "CODE": "ZHDP",
            "GROUP": "MOVIL.GA",
            "NAME": "AHA-760",
            "DATETIME": "220506113733"
        },
        {
            "CODE": "ZHDQ",
            "GROUP": "BIDDLE",
            "NAME": "BPM-039",
            "DATETIME": "220506095424"
        },
        {
            "CODE": "ZHDT",
            "GROUP": "REPARTO",
            "NAME": "AYT-794",
            "DATETIME": "220506114512"
        },
        {
            "CODE": "ZHE0",
            "GROUP": "CORPESA",
            "NAME": "C0Z-753",
            "DATETIME": "220506111854"
        },
        {
            "CODE": "ZHED",
            "GROUP": "FIERRO",
            "NAME": "BDK-753",
            "DATETIME": "220506120206"
        },
        {
            "CODE": "ZHEN",
            "GROUP": "GUAPOLIN",
            "NAME": "A1N-928",
            "DATETIME": "220506120145"
        },
        {
            "CODE": "ZHF7",
            "GROUP": "RENTINCA",
            "NAME": "C1H-766",
            "DATETIME": "220506081103"
        },
        {
            "CODE": "ZHFH",
            "GROUP": "VIA FOOD",
            "NAME": "ATA-769",
            "DATETIME": "220506120421"
        },
        {
            "CODE": "ZHFS",
            "GROUP": "FAMESA",
            "NAME": "AZT-712",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "ZHFT",
            "GROUP": "FORTALEZ",
            "NAME": "ASH-713",
            "DATETIME": "220506114127"
        },
        {
            "CODE": "ZHG0",
            "GROUP": "LISTOTAX",
            "NAME": "BWS-226",
            "DATETIME": "220506075418"
        },
        {
            "CODE": "ZHG8",
            "GROUP": "SAN MART",
            "NAME": "C-93",
            "DATETIME": "220506110551"
        },
        {
            "CODE": "ZHGQ",
            "GROUP": "G.GIANPI",
            "NAME": "B9A-852",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "ZKCB",
            "GROUP": "FAMESA",
            "NAME": "D0G-906",
            "DATETIME": "220427095533"
        },
        {
            "CODE": "ZKCQ",
            "GROUP": "FAMESA",
            "NAME": "AJA-778",
            "DATETIME": "220331064700"
        },
        {
            "CODE": "ZKCV",
            "GROUP": "PTRANQUI",
            "NAME": "D4S-298",
            "DATETIME": "220506120451"
        },
        {
            "CODE": "ZKCW",
            "GROUP": "TELRED",
            "NAME": "IMVS10",
            "DATETIME": "220331084412"
        },
        {
            "CODE": "ZKCY",
            "GROUP": "ANDINAPL",
            "NAME": "BCA-774",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "ZKD6",
            "GROUP": "ACEROS C",
            "NAME": "V9U-741",
            "DATETIME": "220506111842"
        },
        {
            "CODE": "ZKER",
            "GROUP": "TYS VALE",
            "NAME": "W4S-961",
            "DATETIME": "220506081151"
        },
        {
            "CODE": "ZKEV",
            "GROUP": "CORPESA",
            "NAME": "AHR-929",
            "DATETIME": "220429120633"
        },
        {
            "CODE": "ZKEW",
            "GROUP": "ACEROS C",
            "NAME": "V9U-747",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "ZKF2",
            "GROUP": "ACOSTA",
            "NAME": "ANL-732",
            "DATETIME": "220506095448"
        },
        {
            "CODE": "ZKF3",
            "GROUP": "LISTOTAX",
            "NAME": "BWS-218",
            "DATETIME": "220505155527"
        },
        {
            "CODE": "ZKF5",
            "GROUP": "FERMINA",
            "NAME": "AYX-811",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "ZKFA",
            "GROUP": "CONDOR.T",
            "NAME": "F2L-963",
            "DATETIME": "220506074018"
        },
        {
            "CODE": "ZKFB",
            "GROUP": "KAMITAL",
            "NAME": "D1C-944",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "ZKFD",
            "GROUP": "NOR OIL",
            "NAME": "T4X-258",
            "DATETIME": "220506114403"
        },
        {
            "CODE": "ZKFP",
            "GROUP": "INTERSEN",
            "NAME": "D9Q-835",
            "DATETIME": "220430123524"
        },
        {
            "CODE": "ZKFT",
            "GROUP": "T. ALFA",
            "NAME": "F9M-977",
            "DATETIME": "220506113533"
        },
        {
            "CODE": "ZKG4",
            "GROUP": "PRONATUR",
            "NAME": "ABH-877",
            "DATETIME": "220330145745"
        },
        {
            "CODE": "ZKG5",
            "GROUP": "CORPESA",
            "NAME": "BAX-069",
            "DATETIME": "220501130451"
        },
        {
            "CODE": "ZKGF",
            "GROUP": "GUAPOLIN",
            "NAME": "ABD-714",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "ZKGG",
            "GROUP": "A&S OPER",
            "NAME": "D0Z-850",
            "DATETIME": "220506114021"
        },
        {
            "CODE": "ZKGL",
            "GROUP": "RENTINLE",
            "NAME": "BLL-309",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "ZKGM",
            "GROUP": "R Y J",
            "NAME": "BMO-358",
            "DATETIME": "220506120339"
        },
        {
            "CODE": "ZKGR",
            "GROUP": "DEMO",
            "NAME": "ANE-595",
            "DATETIME": "220506120239"
        },
        {
            "CODE": "ZKGW",
            "GROUP": "DANUSKA",
            "NAME": "D7C-930",
            "DATETIME": "220506115518"
        },
        {
            "CODE": "ZKH0",
            "GROUP": "T.EMB DI",
            "NAME": "BDJ-928",
            "DATETIME": "220506120236"
        },
        {
            "CODE": "ZKH4",
            "GROUP": "DIAG.UAL",
            "NAME": "ANQ-450",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "ZKH6",
            "GROUP": "TMC",
            "NAME": "ATN-851",
            "DATETIME": "220506075527"
        },
        {
            "CODE": "ZKH8",
            "GROUP": "TAXI AH",
            "NAME": "D9P-663",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "ZKHB",
            "GROUP": "KAMITAL",
            "NAME": "T4Y-848",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "ZKHD",
            "GROUP": "INTERSEN",
            "NAME": "AYO-891",
            "DATETIME": "220316124230"
        },
        {
            "CODE": "ZKHE",
            "GROUP": "ACEROS C",
            "NAME": "V9U-775",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "ZKHH",
            "GROUP": "BIDDLE",
            "NAME": "C0Z-754",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "ZKHK",
            "GROUP": "PROCARGO",
            "NAME": "AYZ-949",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "ZKHT",
            "GROUP": "INTERSEN",
            "NAME": "APB-928",
            "DATETIME": "220506115233"
        },
        {
            "CODE": "ZKHU",
            "GROUP": "REPARTO",
            "NAME": "AYU-929",
            "DATETIME": "220504082539"
        },
        {
            "CODE": "ZKHV",
            "GROUP": "ANDINAPL",
            "NAME": "D2O-752",
            "DATETIME": "220505155839"
        },
        {
            "CODE": "ZKHX",
            "GROUP": "CASAS",
            "NAME": "B9L-872",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "ZKJ0",
            "GROUP": "RIMAC",
            "NAME": "ASV-076",
            "DATETIME": "220506072724"
        },
        {
            "CODE": "ZLNS",
            "GROUP": "INYEPLAS",
            "NAME": "F5F-753",
            "DATETIME": "220506115557"
        },
        {
            "CODE": "ZLNX",
            "GROUP": "INYEPLAS",
            "NAME": "D8M-921",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "ZLP7",
            "GROUP": "INYEPLAS",
            "NAME": "D5Z-425",
            "DATETIME": "220506113903"
        },
        {
            "CODE": "ZLXP",
            "GROUP": "INYEPLAS",
            "NAME": "C1C-599",
            "DATETIME": "220506113715"
        },
        {
            "CODE": "ZLXS",
            "GROUP": "PAREDES",
            "NAME": "T8M-893",
            "DATETIME": "220215124218"
        },
        {
            "CODE": "ZLXU",
            "GROUP": "ALCIDESF",
            "NAME": "F1I-487",
            "DATETIME": "220506115221"
        },
        {
            "CODE": "ZQB6",
            "GROUP": "CONDOR.T",
            "NAME": "F1E-959",
            "DATETIME": "220506072412"
        },
        {
            "CODE": "ZQBB",
            "GROUP": "LISTOTAX",
            "NAME": "BHC-452",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "ZQBE",
            "GROUP": "DOMINGO",
            "NAME": "AHZ-867",
            "DATETIME": "220506115154"
        },
        {
            "CODE": "ZQBV",
            "GROUP": "RENTING",
            "NAME": "ATG-847",
            "DATETIME": "220506120339"
        },
        {
            "CODE": "ZQC3",
            "GROUP": "ANDINAEX",
            "NAME": "C8P-740",
            "DATETIME": "220326112724"
        },
        {
            "CODE": "ZQCD",
            "GROUP": "TMC",
            "NAME": "ATN-925",
            "DATETIME": "220506120233"
        },
        {
            "CODE": "ZQCN",
            "GROUP": "ROQUE",
            "NAME": "F2N-803",
            "DATETIME": "220506114845"
        },
        {
            "CODE": "ZQCU",
            "GROUP": "PART BET",
            "NAME": "C0I-961",
            "DATETIME": "220419173348"
        },
        {
            "CODE": "ZQCX",
            "GROUP": "TRUCKTEA",
            "NAME": "V9S-906",
            "DATETIME": "220506120209"
        },
        {
            "CODE": "ZQD9",
            "GROUP": "PART BET",
            "NAME": "APY-646",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "ZQDM",
            "GROUP": "PROCARGO",
            "NAME": "ACT-743",
            "DATETIME": "220503112900"
        },
        {
            "CODE": "ZQDP",
            "GROUP": "RIMAC",
            "NAME": "ACQ-634",
            "DATETIME": "220505173103"
        },
        {
            "CODE": "ZQDY",
            "GROUP": "MINERA T",
            "NAME": "ABM-937",
            "DATETIME": "220506064745"
        },
        {
            "CODE": "ZQE0",
            "GROUP": "ACEROS C",
            "NAME": "V9U-749",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "ZQE7",
            "GROUP": "RENTANOR",
            "NAME": "T3L-838",
            "DATETIME": "220504110809"
        },
        {
            "CODE": "ZQE8",
            "GROUP": "SMIGUELG",
            "NAME": "V7V-730",
            "DATETIME": "220506114224"
        },
        {
            "CODE": "ZQE9",
            "GROUP": "POSITIVA",
            "NAME": "AJL-058",
            "DATETIME": "220505162400"
        },
        {
            "CODE": "ZQEG",
            "GROUP": "BIDDLE",
            "NAME": "C8K-798",
            "DATETIME": "220506102424"
        },
        {
            "CODE": "ZQEJ",
            "GROUP": "LISTOTAX",
            "NAME": "BXO-183",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "ZQEK",
            "GROUP": "RIMAC",
            "NAME": "ANG-421",
            "DATETIME": "220505160318"
        },
        {
            "CODE": "ZQEX",
            "GROUP": "ONSIHUAY",
            "NAME": "C7U-771",
            "DATETIME": "220424024400"
        },
        {
            "CODE": "ZQEY",
            "GROUP": "INYEPLAS",
            "NAME": "A4P-948",
            "DATETIME": "220506110736"
        },
        {
            "CODE": "ZQF3",
            "GROUP": "SPACE",
            "NAME": "AEW-781",
            "DATETIME": "220505175224"
        },
        {
            "CODE": "ZQF5",
            "GROUP": "PALMA",
            "NAME": "B2G-801",
            "DATETIME": "220428150530"
        },
        {
            "CODE": "ZQF8",
            "GROUP": "P.CONTAI",
            "NAME": "AFH-477",
            "DATETIME": "220506094806"
        },
        {
            "CODE": "ZQFH",
            "GROUP": "TAXI",
            "NAME": "ANU-507",
            "DATETIME": "220506115215"
        },
        {
            "CODE": "ZQFM",
            "GROUP": "ACEROS C",
            "NAME": "V9U-786",
            "DATETIME": "220506120415"
        },
        {
            "CODE": "ZQFT",
            "GROUP": "SANTA RO",
            "NAME": "ADX-768",
            "DATETIME": "220506115209"
        },
        {
            "CODE": "ZQFU",
            "GROUP": "LISTOTAX",
            "NAME": "BAR-355",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "ZQFV",
            "GROUP": "HUASCAR",
            "NAME": "AVU-947",
            "DATETIME": "220506114609"
        },
        {
            "CODE": "ZQFZ",
            "GROUP": "T.ROCHA",
            "NAME": "AAL-885",
            "DATETIME": "220506114951"
        },
        {
            "CODE": "ZQGN",
            "GROUP": "FUENTES",
            "NAME": "AJZ-278",
            "DATETIME": "220506075648"
        },
        {
            "CODE": "ZQGR",
            "GROUP": "MYI GLO",
            "NAME": "D1C-816",
            "DATETIME": "220506113951"
        },
        {
            "CODE": "ZQGT",
            "GROUP": "POLMAR",
            "NAME": "B5Q-941",
            "DATETIME": "220311103700"
        },
        {
            "CODE": "ZSS7",
            "GROUP": "LISTOTAX",
            "NAME": "BRA-341",
            "DATETIME": "220506114703"
        },
        {
            "CODE": "ZSSJ",
            "GROUP": "CIELITO",
            "NAME": "AHJ-948",
            "DATETIME": "220506120251"
        },
        {
            "CODE": "ZSSV",
            "GROUP": "O.L.MINE",
            "NAME": "AAH-881",
            "DATETIME": "220506114412"
        },
        {
            "CODE": "ZSU8",
            "GROUP": "STA ROSA",
            "NAME": "BDU-814",
            "DATETIME": "220506115403"
        },
        {
            "CODE": "ZSUK",
            "GROUP": "LISTOTAX",
            "NAME": "BWQ-093",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "ZSUQ",
            "GROUP": "INCHE",
            "NAME": "F6B-992",
            "DATETIME": "220506115518"
        },
        {
            "CODE": "ZSV2",
            "GROUP": "LISTOTAX",
            "NAME": "BWU-569",
            "DATETIME": "220506101018"
        },
        {
            "CODE": "ZSV8",
            "GROUP": "ESPAR",
            "NAME": "ALL-668",
            "DATETIME": "220506114015"
        },
        {
            "CODE": "ZSVB",
            "GROUP": "KAMITAL",
            "NAME": "T6T-818",
            "DATETIME": "220506115848"
        },
        {
            "CODE": "ZSVN",
            "GROUP": "INCHE",
            "NAME": "F6O-804",
            "DATETIME": "220506115818"
        },
        {
            "CODE": "ZSWA",
            "GROUP": "SAN MART",
            "NAME": "EUE-995",
            "DATETIME": "220506102924"
        },
        {
            "CODE": "ZSWC",
            "GROUP": "MAPFRE",
            "NAME": "AKJ-346",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "ZSWJ",
            "GROUP": "LLANOSL",
            "NAME": "AJX-752",
            "DATETIME": "220505204006"
        },
        {
            "CODE": "ZSWL",
            "GROUP": "ACEROS C",
            "NAME": "V9U-776",
            "DATETIME": "220505135239"
        },
        {
            "CODE": "ZSWP",
            "GROUP": "DURAND",
            "NAME": "D5S-414",
            "DATETIME": "220506120430"
        },
        {
            "CODE": "ZSWW",
            "GROUP": "L & M",
            "NAME": "T5Q-883",
            "DATETIME": "220505091354"
        },
        {
            "CODE": "ZSX0",
            "GROUP": "RENTINLE",
            "NAME": "BHM-117",
            "DATETIME": "220506112106"
        },
        {
            "CODE": "ZSX4",
            "GROUP": "DONPOLLO",
            "NAME": "AAB-854",
            "DATETIME": "220506115018"
        },
        {
            "CODE": "ZSXG",
            "GROUP": "RENTING",
            "NAME": "AWU-940",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "ZSXK",
            "GROUP": "LISTOTAX",
            "NAME": "BXM-620",
            "DATETIME": "220506113757"
        },
        {
            "CODE": "ZSXL",
            "GROUP": "ADUANDIN",
            "NAME": "APK-756",
            "DATETIME": "220506120506"
        },
        {
            "CODE": "ZSXV",
            "GROUP": "T.VICKY",
            "NAME": "BJM-909",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "ZT55",
            "GROUP": "LISTOTAX",
            "NAME": "BNG-315",
            "DATETIME": "220506120500"
        },
        {
            "CODE": "ZT5A",
            "GROUP": "ACOSTA",
            "NAME": "ANN-838",
            "DATETIME": "220506120157"
        },
        {
            "CODE": "ZT8E",
            "GROUP": "TICLAVIL",
            "NAME": "ATE-834",
            "DATETIME": "220506120139"
        },
        {
            "CODE": "ZT8V",
            "GROUP": "LISTOTAX",
            "NAME": "BLC-549",
            "DATETIME": "220506000924"
        },
        {
            "CODE": "ZT94",
            "GROUP": "SOLTRAK",
            "NAME": "ATO-799",
            "DATETIME": "220207132924"
        },
        {
            "CODE": "ZTL1",
            "GROUP": "P & M",
            "NAME": "B7X-756",
            "DATETIME": "220506115933"
        },
        {
            "CODE": "ZTLC",
            "GROUP": "INVMARIA",
            "NAME": "ANF-878",
            "DATETIME": "220506120203"
        },
        {
            "CODE": "ZTLD",
            "GROUP": "SOLTRAK",
            "NAME": "ATP-945",
            "DATETIME": "220506120424"
        },
        {
            "CODE": "ZTNY",
            "GROUP": "POSITIVA",
            "NAME": "ACQ-170",
            "DATETIME": "220506073830"
        },
        {
            "CODE": "ZTP4",
            "GROUP": "PART BET",
            "NAME": "ARY-707",
            "DATETIME": "220506120318"
        },
        {
            "CODE": "ZTPN",
            "GROUP": "LISTOTAX",
            "NAME": "BNE-471",
            "DATETIME": "220506112921"
        },
        {
            "CODE": "ZTTL",
            "GROUP": "ROSSIFER",
            "NAME": "D3G-747",
            "DATETIME": "220429141024"
        },
        {
            "CODE": "ZTTY",
            "GROUP": "RIMAC",
            "NAME": "ALK-549",
            "DATETIME": "220505124103"
        },
        {
            "CODE": "ZTWY",
            "GROUP": "T.VICKYV",
            "NAME": "B4B-875",
            "DATETIME": "220506115451"
        },
        {
            "CODE": "ZTWZ",
            "GROUP": "LISTOTAX",
            "NAME": "BAT-007",
            "DATETIME": "220506120230"
        },
        {
            "CODE": "ZTXD",
            "GROUP": "RIMAC",
            "NAME": "AMQ-459",
            "DATETIME": "220505165027"
        },
        {
            "CODE": "ZTXM",
            "GROUP": "T.VICKYV",
            "NAME": "C6E-864",
            "DATETIME": "220506113300"
        },
        {
            "CODE": "ZTXT",
            "GROUP": "T.VICKYV",
            "NAME": "B4Y-884",
            "DATETIME": "220506113824"
        },
        {
            "CODE": "ZTXY",
            "GROUP": "T.VICKYV",
            "NAME": "D3W-789",
            "DATETIME": "220506115212"
        },
        {
            "CODE": "ZTXZ",
            "GROUP": "T.VICKYV",
            "NAME": "B9E-744",
            "DATETIME": "220506120009"
        },
        {
            "CODE": "ZTY0",
            "GROUP": "ALCIDESF",
            "NAME": "C6F-417",
            "DATETIME": "220506120503"
        },
        {
            "CODE": "ZTY1",
            "GROUP": "ALCIDESF",
            "NAME": "B8M-145",
            "DATETIME": "220506115115"
        },
        {
            "CODE": "ZTY9",
            "GROUP": "T.BALDEO",
            "NAME": "D1D-962",
            "DATETIME": "220506120524"
        },
        {
            "CODE": "ZU0P",
            "GROUP": "TAFUR",
            "NAME": "BHZ-576",
            "DATETIME": "220506120448"
        },
        {
            "CODE": "ZUGP",
            "GROUP": "PACIFICO",
            "NAME": "C4Q-744",
            "DATETIME": "220506115118"
        },
        {
            "CODE": "ZUH7",
            "GROUP": "RIMAC",
            "NAME": "ADK-621",
            "DATETIME": "220506113551"
        },
        {
            "CODE": "ZUHR",
            "GROUP": "AUTONORT",
            "NAME": "T7Z-870",
            "DATETIME": "220506120433"
        },
        {
            "CODE": "ZUJD",
            "GROUP": "ESPAR",
            "NAME": "AMQ-024",
            "DATETIME": "220506113851"
        },
        {
            "CODE": "ZVFH",
            "GROUP": "ESPAR",
            "NAME": "ANO-048",
            "DATETIME": "220506112415"
        },
        {
            "CODE": "ZVGY",
            "GROUP": "RIMAC",
            "NAME": "ANP-016",
            "DATETIME": "220506094339"
        },
        {
            "CODE": "ZWVQ",
            "GROUP": "ORELLANA",
            "NAME": "W1O-980",
            "DATETIME": "220506111536"
        },
        {
            "CODE": "ZWW8",
            "GROUP": "T.FLORES",
            "NAME": "A8E-913",
            "DATETIME": "220502094939"
        },
        {
            "CODE": "ZWW9",
            "GROUP": "T.FLORES",
            "NAME": "Z3Y-846",
            "DATETIME": "220223124021"
        },
        {
            "CODE": "ZWWA",
            "GROUP": "T.FLORES",
            "NAME": "D1J-743",
            "DATETIME": "220506113636"
        },
        {
            "CODE": "ZWWB",
            "GROUP": "T.FLORES",
            "NAME": "ABG-895",
            "DATETIME": "220414173418"
        },
        {
            "CODE": "ZWWD",
            "GROUP": "T.FLORES",
            "NAME": "C8V-949",
            "DATETIME": "220506090530"
        },
        {
            "CODE": "ZWWE",
            "GROUP": "EMTRACOM",
            "NAME": "ALM-989",
            "DATETIME": "220205111224"
        },
        {
            "CODE": "ZWWP",
            "GROUP": "T.FLORES",
            "NAME": "Z1A-911",
            "DATETIME": "220506114736"
        },
        {
            "CODE": "ZWWZ",
            "GROUP": "T.FLORES",
            "NAME": "A2Q-837",
            "DATETIME": "220506115806"
        },
        {
            "CODE": "ZWXY",
            "GROUP": "MUNDO",
            "NAME": "ALB-949",
            "DATETIME": "220506115618"
        },
        {
            "CODE": "ZWYD",
            "GROUP": "CORMEI",
            "NAME": "B7R-781",
            "DATETIME": "220506114848"
        },
        {
            "CODE": "ZWYG",
            "GROUP": "OLIVARES",
            "NAME": "AAG-883",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "ZWYZ",
            "GROUP": "GILDEMEI",
            "NAME": "AYA-898",
            "DATETIME": "220506112142"
        },
        {
            "CODE": "ZWZB",
            "GROUP": "PART BET",
            "NAME": "BEP-555",
            "DATETIME": "220506113618"
        },
        {
            "CODE": "ZWZL",
            "GROUP": "SINCONVE",
            "NAME": "BJM-601",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "ZXTF",
            "GROUP": "SHILCAYO",
            "NAME": "BEW-914",
            "DATETIME": "220506114045"
        },
        {
            "CODE": "ZXTW",
            "GROUP": "REPARTO",
            "NAME": "BHX-793",
            "DATETIME": "220506120412"
        },
        {
            "CODE": "ZXU5",
            "GROUP": "FAMESA",
            "NAME": "F1G-741",
            "DATETIME": "220427110045"
        },
        {
            "CODE": "ZXU6",
            "GROUP": "CESEL",
            "NAME": "ANG-349",
            "DATETIME": "220506114012"
        },
        {
            "CODE": "ZXUA",
            "GROUP": "INCHE",
            "NAME": "D4C-989",
            "DATETIME": "220506120342"
        },
        {
            "CODE": "ZXUC",
            "GROUP": "INCHE",
            "NAME": "F6C-973",
            "DATETIME": "220506111609"
        },
        {
            "CODE": "ZXUK",
            "GROUP": "SAN MART",
            "NAME": "C5P-774",
            "DATETIME": "220506120445"
        },
        {
            "CODE": "ZXUP",
            "GROUP": "DIAG.UAL",
            "NAME": "C0N-078",
            "DATETIME": "220506112321"
        },
        {
            "CODE": "ZXUR",
            "GROUP": "LISTOTAX",
            "NAME": "BHZ-431",
            "DATETIME": "220506120512"
        },
        {
            "CODE": "ZXUT",
            "GROUP": "INCHE",
            "NAME": "F4B-999",
            "DATETIME": "220506092124"
        },
        {
            "CODE": "ZXUU",
            "GROUP": "SAN DIEG",
            "NAME": "AJN-807",
            "DATETIME": "220506114712"
        },
        {
            "CODE": "ZXUW",
            "GROUP": "DIAG.UAL",
            "NAME": "AWF-254",
            "DATETIME": "220506120354"
        },
        {
            "CODE": "ZXV0",
            "GROUP": "V.CASTRO",
            "NAME": "ANL-492",
            "DATETIME": "220506120521"
        },
        {
            "CODE": "ZXV2",
            "GROUP": "MACROSIG",
            "NAME": "AVT-754",
            "DATETIME": "220506115430"
        },
        {
            "CODE": "ZXV6",
            "GROUP": "INCHE",
            "NAME": "D4B-982",
            "DATETIME": "220506064327"
        },
        {
            "CODE": "ZXV7",
            "GROUP": "BIDDLE",
            "NAME": "C0L-192",
            "DATETIME": "220503114151"
        },
        {
            "CODE": "ZXVA",
            "GROUP": "POSITIVA",
            "NAME": "Y1R-172",
            "DATETIME": "220506120306"
        },
        {
            "CODE": "ZXVC",
            "GROUP": "DIAG.UAL",
            "NAME": "BHC-379",
            "DATETIME": "220506114751"
        },
        {
            "CODE": "ZXVD",
            "GROUP": "FAMESA",
            "NAME": "A6N-932",
            "DATETIME": "220426092433"
        },
        {
            "CODE": "ZXVE",
            "GROUP": "FAMESA",
            "NAME": "C8C-356",
            "DATETIME": "220505204303"
        },
        {
            "CODE": "ZXVG",
            "GROUP": "FAMESA",
            "NAME": "EUD-956",
            "DATETIME": "220422104118"
        },
        {
            "CODE": "ZXVH",
            "GROUP": "FAMESA",
            "NAME": "B8K-783",
            "DATETIME": "220427091703"
        },
        {
            "CODE": "ZXVK",
            "GROUP": "FAMESA",
            "NAME": "D0I-740",
            "DATETIME": "220422152524"
        },
        {
            "CODE": "ZXVM",
            "GROUP": "FAMESA",
            "NAME": "ASK-776",
            "DATETIME": "220506114248"
        },
        {
            "CODE": "ZXVN",
            "GROUP": "FAMESA",
            "NAME": "C8V-230",
            "DATETIME": "220426121839"
        },
        {
            "CODE": "ZXVP",
            "GROUP": "FAMESA",
            "NAME": "D2B-938",
            "DATETIME": "220427150345"
        },
        {
            "CODE": "ZXVQ",
            "GROUP": "FAMESA",
            "NAME": "B8K-707",
            "DATETIME": "220420120306"
        },
        {
            "CODE": "ZXVS",
            "GROUP": "FAMESA",
            "NAME": "D6U-705",
            "DATETIME": "220422104145"
        },
        {
            "CODE": "ZXVT",
            "GROUP": "FAMESA",
            "NAME": "C5K-732",
            "DATETIME": "220422093012"
        },
        {
            "CODE": "ZXVW",
            "GROUP": "FAMESA",
            "NAME": "F6L-850",
            "DATETIME": "220420113221"
        },
        {
            "CODE": "ZXW0",
            "GROUP": "FAMESA",
            "NAME": "A6M-815",
            "DATETIME": "220422152742"
        },
        {
            "CODE": "ZXW1",
            "GROUP": "FAMESA",
            "NAME": "B7H-948",
            "DATETIME": "220506115951"
        },
        {
            "CODE": "ZXW3",
            "GROUP": "FAMESA",
            "NAME": "ASJ-937",
            "DATETIME": "220420143945"
        },
        {
            "CODE": "ZXW8",
            "GROUP": "SHILCAYO",
            "NAME": "BEW-912",
            "DATETIME": "220505190215"
        },
        {
            "CODE": "ZXW9",
            "GROUP": "RIMAC",
            "NAME": "AMN-386",
            "DATETIME": "220506110221"
        },
        {
            "CODE": "ZXWF",
            "GROUP": "FAMESA",
            "NAME": "C5L-719",
            "DATETIME": "220422114427"
        },
        {
            "CODE": "ZXWN",
            "GROUP": "FAMESA",
            "NAME": "A6N-934",
            "DATETIME": "220421144345"
        },
        {
            "CODE": "ZXWQ",
            "GROUP": "VILLENA",
            "NAME": "ALG-845",
            "DATETIME": "220506120509"
        },
        {
            "CODE": "ZXWR",
            "GROUP": "SERVINSA",
            "NAME": "AKV-926",
            "DATETIME": "220506120139"
        },
        {
            "CODE": "ZXWU",
            "GROUP": "FAMESA",
            "NAME": "EUD-428",
            "DATETIME": "220419151239"
        },
        {
            "CODE": "ZXX2",
            "GROUP": "BIDDLE",
            "NAME": "B3N-838",
            "DATETIME": "220505171021"
        },
        {
            "CODE": "ZXX6",
            "GROUP": "FAMESA",
            "NAME": "C4T-751",
            "DATETIME": "220506091818"
        },
        {
            "CODE": "ZXX7",
            "GROUP": "BIDDLE",
            "NAME": "B3N-812",
            "DATETIME": "220506120042"
        },
        {
            "CODE": "ZXX9",
            "GROUP": "T.SANTA",
            "NAME": "W3G-971",
            "DATETIME": "220506120527"
        },
        {
            "CODE": "ZXXF",
            "GROUP": "AYBAR",
            "NAME": "ARM-866",
            "DATETIME": "220505172327"
        },
        {
            "CODE": "ZXXG",
            "GROUP": "POLMAR",
            "NAME": "D9T-351",
            "DATETIME": "220506110633"
        },
        {
            "CODE": "ZXXJ",
            "GROUP": "VIA FOOD",
            "NAME": "AVT-859",
            "DATETIME": "220505123927"
        },
        {
            "CODE": "ZXXP",
            "GROUP": "CORPESA",
            "NAME": "B4I-904",
            "DATETIME": "220506115833"
        },
        {
            "CODE": "ZXXT",
            "GROUP": "T.CALDER",
            "NAME": "B1M-919",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "ZXXV",
            "GROUP": "CASTROCO",
            "NAME": "AAY-815",
            "DATETIME": "220506120518"
        },
        {
            "CODE": "ZXXW",
            "GROUP": "GUAPOLIN",
            "NAME": "ALZ-703",
            "DATETIME": "220506120457"
        },
        {
            "CODE": "ZXXY",
            "GROUP": "FAMESA",
            "NAME": "D0I-866",
            "DATETIME": "220426094609"
        },
        {
            "CODE": "ZXXZ",
            "GROUP": "CALDERON",
            "NAME": "V8J-939",
            "DATETIME": "220505125821"
        },
        {
            "CODE": "ZXY4",
            "GROUP": "T.VICKYV",
            "NAME": "AJR-925",
            "DATETIME": "220506120454"
        },
        {
            "CODE": "ZXY8",
            "GROUP": "MACROSIG",
            "NAME": "BCW-817",
            "DATETIME": "220506120027"
        },
        {
            "CODE": "ZXYA",
            "GROUP": "T.VICKYV",
            "NAME": "B4B-878",
            "DATETIME": "220506115142"
        },
        {
            "CODE": "ZXYC",
            "GROUP": "T.VICKYV",
            "NAME": "D3X-748",
            "DATETIME": "220506114942"
        },
        {
            "CODE": "ZXYD",
            "GROUP": "T.VICKYV",
            "NAME": "B8D-716",
            "DATETIME": "220506120157"
        },
        {
            "CODE": "ZXYM",
            "GROUP": "INCHE",
            "NAME": "A1X-923",
            "DATETIME": "220506112806"
        },
        {
            "CODE": "ZXYS",
            "GROUP": "SEGURSAT",
            "NAME": "BDB-588",
            "DATETIME": "220506114236"
        },
        {
            "CODE": "ZXYT",
            "GROUP": "T.VICKYV",
            "NAME": "D3X-741",
            "DATETIME": "220505092303"
        },
        {
            "CODE": "ZXYV",
            "GROUP": "T.VICKYV",
            "NAME": "C2M-883",
            "DATETIME": "220506120157"
        },
        {
            "CODE": "ZXYY",
            "GROUP": "O.L.MINE",
            "NAME": "AJF-795",
            "DATETIME": "220506120227"
        },
        {
            "CODE": "ZXYZ",
            "GROUP": "B VISTA",
            "NAME": "V5V-734",
            "DATETIME": "220506120442"
        },
        {
            "CODE": "ZXZ0",
            "GROUP": "T.VICKYV",
            "NAME": "A0A-912",
            "DATETIME": "220506120051"
        },
        {
            "CODE": "ZXZ4",
            "GROUP": "FAMESA",
            "NAME": "EUE-010",
            "DATETIME": "220505144654"
        },
        {
            "CODE": "ZXZD",
            "GROUP": "DIAG.UAL",
            "NAME": "B2F-063",
            "DATETIME": "220505172439"
        },
        {
            "CODE": "ZXZE",
            "GROUP": "FAMESA",
            "NAME": "B8J-712",
            "DATETIME": "220506114818"
        },
        {
            "CODE": "ZXZF",
            "GROUP": "FAMESA",
            "NAME": "F7L-933",
            "DATETIME": "220421172415"
        },
        {
            "CODE": "ZXZJ",
            "GROUP": "INTERSEN",
            "NAME": "C9Y-808",
            "DATETIME": "220506120427"
        },
        {
            "CODE": "ZXZK",
            "GROUP": "FAMESA",
            "NAME": "B7I-901",
            "DATETIME": "220422122342"
        },
        {
            "CODE": "ZXZM",
            "GROUP": "RENTING",
            "NAME": "AYH-496",
            "DATETIME": "220506114403"
        },
        {
            "CODE": "ZXZS",
            "GROUP": "FAMESA",
            "NAME": "B0Q-906",
            "DATETIME": "220420140657"
        },
        {
            "CODE": "ZXZY",
            "GROUP": "FAMESA",
            "NAME": "A6N-937",
            "DATETIME": "220422123015"
        }
    ]
}

account = Account.objects.get(name='kft')

for unit in data['SHEET1']:
    try:
        device = Device.objects.create(
            uniqueid = unit['CODE'],
            imei = unit['CODE'],
            name = unit['NAME'],
            description = f"{unit['GROUP']} - {unit['NAME']}",
            account = account,
        )
    except Exception as e:
        print(e)