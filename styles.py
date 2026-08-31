GLOBAL_CSS = """
<style>
:root {
    --bg: #05060a;
    --bg-elevated: #0b0d18;
    --card-bg: rgba(18, 20, 36, 0.6);
    --border: rgba(139, 92, 246, 0.18);
    --border-strong: rgba(139, 92, 246, 0.4);
    --primary: #8b5cf6;
    --primary-light: #a78bfa;
    --accent: #38bdf8;
    --text: #f1f2f8;
    --text-muted: #9aa0c0;
    --success: #34d399;
    --warning: #fbbf24;
    --danger: #f87171;
    --radius: 12px;
}

.stApp {
    background:
        radial-gradient(ellipse 900px 600px at 15% 10%, rgba(139,92,246,0.16), transparent 60%),
        radial-gradient(ellipse 800px 500px at 85% 25%, rgba(56,189,248,0.12), transparent 60%),
        radial-gradient(ellipse at top left, #10132a 0%, var(--bg) 55%);
    font-family: 'Inter', 'Segoe UI', sans-serif;
}
html, body, [class*="css"] { font-family: 'Inter', 'Segoe UI', sans-serif; }

section[data-testid="stSidebar"] {
    background: var(--bg-elevated);
    border-right: 1px solid var(--border);
}
section[data-testid="stSidebar"] * { color: var(--text) !important; }

[data-testid="stSidebarNav"] a, [data-testid="stSidebarNavLink"] {
    border-radius: 8px !important;
    margin: 2px 8px !important;
    transition: background 0.2s ease, transform 0.15s ease;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(139, 92, 246, 0.12) !important;
    transform: translateX(2px);
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(139,92,246,0.25), rgba(56,189,248,0.12)) !important;
    border-left: 3px solid var(--primary);
}

.sidebar-profile {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px;
    margin: 6px 8px 14px 8px;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
}
.sidebar-avatar {
    width: 34px; height: 34px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; color: white; font-size: 0.9rem;
}
.sidebar-username { font-weight: 600; font-size: 0.88rem; }
.sidebar-role { font-size: 0.72rem; color: var(--text-muted); }

.groq-key-row {
    margin: 4px 8px 6px 8px;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text);
}
.groq-key-status {
    margin: 4px 8px 14px 8px;
    font-size: 0.74rem;
}
.groq-key-status.ok { color: var(--success); }
.groq-key-status.warn { color: var(--text-muted); }

/* squeeze the eye-toggle button next to the key field into a small square */
section[data-testid="stSidebar"] div.stButton:has(button[kind="secondary"]) {
    margin-top: 0;
}
section[data-testid="stSidebar"] .stTextInput,
section[data-testid="stSidebar"] .stButton {
    margin: 0 8px !important;
}

.sidebar-status-card {
    margin: 14px 8px;
    padding: 12px;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
}
.status-dot {
    display: inline-block; width: 8px; height: 8px; border-radius: 50%;
    background: var(--success); margin-right: 6px;
    box-shadow: 0 0 6px var(--success);
    animation: pulseDot 2s ease-in-out infinite;
}
@keyframes pulseDot { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }

.cb-topbar {
    position: sticky; top: 0; z-index: 100;
    display: flex; justify-content: space-between; align-items: center;
    padding: 14px 4px;
    margin-bottom: 1rem;
    background: rgba(5, 6, 10, 0.75);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
}
.cb-brand { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 1.2rem; }
.cb-brand-badge {
    background: linear-gradient(135deg, var(--primary), var(--accent));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}

.cb-card {
    background: var(--card-bg);
    backdrop-filter: blur(14px);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.4rem;
    margin-bottom: 1rem;
    transition: border 0.2s ease, transform 0.15s ease;
}
.cb-card:hover { border-color: var(--border-strong); }

.cb-h1 { font-size: 1.9rem; font-weight: 800; color: var(--text); margin-bottom: 0.1rem; }
.cb-sub { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.2rem; }

.stat-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.1rem;
    transition: transform 0.15s ease, border 0.2s ease;
}
.stat-card:hover { transform: translateY(-2px); border-color: var(--border-strong); }
.stat-icon { font-size: 1.4rem; margin-bottom: 6px; }
.stat-value { font-size: 1.6rem; font-weight: 800; color: var(--text); }
.stat-label { font-size: 0.8rem; color: var(--text-muted); }

div.stButton > button {
    background: linear-gradient(90deg, var(--primary), #7c3aed);
    color: white; border: none; border-radius: 999px;
    padding: 0.55rem 1.3rem; font-weight: 600;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
div.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(139, 92, 246, 0.4);
}

/* ===== Wix-style black navbar ===== */
.wix-navbar {
    position: sticky; top: 0; z-index: 200;
    display: flex; justify-content: space-between; align-items: center;
    background: #000000;
    padding: 16px 28px;
    border-radius: 14px;
    margin-bottom: 1.5rem;
}
.wix-logo { display: flex; align-items: center; gap: 10px; color: white; font-weight: 700; font-size: 1.1rem; }
.wix-logo-badge {
    width: 26px; height: 26px; border-radius: 6px;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    display: flex; align-items: center; justify-content: center; font-size: 0.85rem;
}
.wix-nav-links { display: flex; gap: 28px; align-items: center; }
.wix-nav-links a { color: #d8d8e4; text-decoration: none; font-size: 0.92rem; font-weight: 500; }
.wix-pill-btn {
    background: white; color: #000; border-radius: 999px;
    padding: 8px 20px; font-weight: 600; font-size: 0.85rem;
    letter-spacing: 0.5px; text-transform: uppercase;
}

/* ===== Hero header ===== */
.hero-eyebrow {
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-size: 0.78rem;
    color: var(--text-muted);
    font-weight: 600;
    margin-bottom: 0.6rem;
}
.hero-title {
    font-size: clamp(2.2rem, 5vw, 3.6rem);
    font-weight: 500;
    line-height: 1.05;
    letter-spacing: -1px;
    color: var(--text);
    margin-bottom: 0.8rem;
}
.hero-title .accent {
    background: linear-gradient(90deg, var(--primary-light), var(--accent));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    font-size: 0.95rem;
    color: var(--text-muted);
    max-width: 560px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    line-height: 1.6;
}

.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 600;
    margin-right: 6px;
    background: rgba(56, 189, 248, 0.12);
    color: var(--accent);
    border: 1px solid rgba(56, 189, 248, 0.3);
}

.timeline-step { display: flex; gap: 12px; padding: 8px 0; align-items: flex-start; }
.timeline-icon {
    width: 22px; height: 22px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.75rem; flex-shrink: 0; margin-top: 2px;
}
.ts-done { background: var(--success); color: #05060a; }
.ts-active {
    background: linear-gradient(135deg, var(--primary), var(--accent));
    color: white; box-shadow: 0 0 10px rgba(139,92,246,0.6);
    animation: pulseDot 1.5s ease-in-out infinite;
}
.ts-pending { background: rgba(255,255,255,0.08); color: var(--text-muted); }
.ts-failed { background: var(--danger); color: white; }
.timeline-title { font-weight: 600; font-size: 0.92rem; }
.timeline-desc { font-size: 0.78rem; color: var(--text-muted); }

.tpl-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.1rem;
    height: 100%;
    transition: transform 0.15s ease, border 0.2s ease;
}
.tpl-card:hover { transform: translateY(-3px); border-color: var(--border-strong); }
.tpl-icon { font-size: 1.6rem; margin-bottom: 8px; }
.tpl-name { font-weight: 700; margin-bottom: 2px; }
.tpl-desc { font-size: 0.8rem; color: var(--text-muted); margin-bottom: 8px; }

.chat-bubble-user, .chat-bubble-ai {
    padding: 10px 14px; border-radius: 12px; margin-bottom: 8px; max-width: 85%;
}
.chat-bubble-user {
    background: linear-gradient(90deg, var(--primary), #7c3aed);
    color: white; margin-left: auto;
}
.chat-bubble-ai {
    background: var(--card-bg); border: 1px solid var(--border); color: var(--text);
}

.success-card {
    background: linear-gradient(135deg, rgba(52,211,153,0.1), rgba(56,189,248,0.06));
    border: 1px solid rgba(52,211,153,0.35);
    border-radius: var(--radius);
    padding: 1.5rem;
    text-align: center;
}

.stTextArea textarea, .stTextInput input, div[data-baseweb="select"] {
    background: rgba(255,255,255,0.03) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 9px !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.15) !important;
}

.stCodeBlock, pre { border-radius: 10px !important; border: 1px solid var(--border) !important; }

.stTabs [data-baseweb="tab"] { color: var(--text-muted); font-weight: 600; }
.stTabs [aria-selected="true"] { color: var(--primary) !important; }
</style>
"""

STARFIELD_CSS = """
<style>
#starfield-layer {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: transparent;
    z-index: 0;
    overflow: hidden;
    pointer-events: none;
}
.stars, .stars2, .stars3 {
    position: absolute;
    top: 0; left: 0;
    width: 1px; height: 1px;
    background: transparent;
}
.stars {
    box-shadow: 1309px 228px #FFF, 51px 1518px #FFF, 563px 501px #FFF, 457px 285px #FFF, 1508px 209px #FFF, 1385px 1516px #FFF, 1827px 1116px #FFF, 178px 1209px #FFF, 864px 65px #FFF, 61px 191px #FFF, 447px 476px #FFF, 1034px 1232px #FFF, 54px 1149px #FFF, 407px 1466px #FFF, 1330px 1436px #FFF, 1116px 859px #FFF, 451px 919px #FFF, 1206px 569px #FFF, 1657px 1780px #FFF, 13px 1554px #FFF, 1650px 326px #FFF, 1429px 865px #FFF, 696px 569px #FFF, 318px 440px #FFF, 1960px 1563px #FFF, 689px 209px #FFF, 189px 778px #FFF, 198px 735px #FFF, 1735px 704px #FFF, 1236px 541px #FFF, 1652px 88px #FFF, 1494px 940px #FFF, 1098px 255px #FFF, 1992px 1888px #FFF, 775px 161px #FFF, 1130px 600px #FFF, 1698px 1287px #FFF, 1266px 1813px #FFF, 1764px 740px #FFF, 1182px 393px #FFF, 1442px 142px #FFF, 93px 1354px #FFF, 466px 1583px #FFF, 592px 163px #FFF, 1751px 476px #FFF, 1774px 206px #FFF, 778px 569px #FFF, 928px 1301px #FFF, 1708px 747px #FFF, 333px 758px #FFF, 727px 429px #FFF, 1372px 546px #FFF, 1437px 1918px #FFF, 1399px 1327px #FFF, 146px 1247px #FFF, 1300px 350px #FFF, 1093px 1493px #FFF, 501px 334px #FFF, 946px 777px #FFF, 552px 1895px #FFF, 1310px 1409px #FFF, 1140px 449px #FFF, 1402px 664px #FFF, 1726px 1573px #FFF, 1589px 114px #FFF, 469px 1683px #FFF, 65px 1648px #FFF, 646px 821px #FFF, 548px 135px #FFF, 432px 1870px #FFF, 1931px 1161px #FFF, 1794px 1470px #FFF, 644px 435px #FFF, 1342px 1022px #FFF, 810px 1811px #FFF, 1872px 1316px #FFF, 939px 292px #FFF, 542px 285px #FFF, 505px 1525px #FFF, 1149px 1103px #FFF, 538px 1529px #FFF, 1197px 877px #FFF, 1838px 1195px #FFF, 817px 741px #FFF, 449px 283px #FFF, 1043px 1010px #FFF, 186px 1547px #FFF, 96px 1763px #FFF, 224px 313px #FFF, 1285px 327px #FFF, 1622px 1393px #FFF, 864px 1221px #FFF, 130px 788px #FFF, 781px 1220px #FFF, 958px 1083px #FFF, 514px 1988px #FFF, 1133px 1762px #FFF, 1930px 23px #FFF, 1393px 1476px #FFF, 234px 1396px #FFF, 1812px 1099px #FFF, 1537px 546px #FFF, 1574px 1312px #FFF, 696px 228px #FFF, 601px 890px #FFF, 323px 929px #FFF, 6px 1953px #FFF, 1478px 1793px #FFF, 1473px 539px #FFF, 1990px 1025px #FFF, 1560px 365px #FFF, 1039px 1869px #FFF, 217px 1782px #FFF, 1280px 611px #FFF, 1723px 1308px #FFF, 1039px 1247px #FFF, 407px 313px #FFF, 765px 1561px #FFF, 330px 1104px #FFF, 1952px 1594px #FFF, 1889px 1086px #FFF, 1881px 1px #FFF, 1226px 663px #FFF, 1000px 39px #FFF, 229px 1902px #FFF, 743px 1799px #FFF, 1703px 1652px #FFF, 629px 490px #FFF, 118px 493px #FFF, 1798px 1161px #FFF, 1939px 161px #FFF, 175px 1498px #FFF, 995px 1671px #FFF, 141px 1557px #FFF, 1090px 1568px #FFF, 257px 262px #FFF, 1351px 973px #FFF, 1939px 1125px #FFF, 338px 542px #FFF, 1080px 1786px #FFF, 1242px 866px #FFF, 1975px 433px #FFF, 1902px 1104px #FFF, 1546px 1494px #FFF, 1412px 411px #FFF, 1460px 638px #FFF, 817px 1375px #FFF, 1330px 764px #FFF, 897px 1842px #FFF, 1059px 924px #FFF, 247px 507px #FFF, 460px 131px #FFF, 692px 43px #FFF, 1204px 1134px #FFF, 471px 1205px #FFF, 451px 14px #FFF, 145px 1449px #FFF, 1292px 120px #FFF, 468px 138px #FFF, 1854px 64px #FFF, 1760px 676px #FFF, 145px 1052px #FFF, 487px 570px #FFF, 1370px 994px #FFF, 438px 1104px #FFF, 270px 1481px #FFF, 1915px 1807px #FFF, 1169px 1180px #FFF, 968px 497px #FFF, 1606px 968px #FFF, 1653px 833px #FFF, 389px 193px #FFF, 198px 1349px #FFF, 882px 725px #FFF, 867px 841px #FFF, 956px 1769px #FFF, 1493px 110px #FFF, 1379px 1338px #FFF, 1323px 201px #FFF, 124px 824px #FFF, 1491px 694px #FFF, 1639px 1764px #FFF, 223px 509px #FFF, 392px 389px #FFF, 1098px 918px #FFF, 287px 864px #FFF, 375px 570px #FFF, 947px 511px #FFF, 1790px 1890px #FFF, 154px 907px #FFF, 1654px 1764px #FFF, 1753px 1127px #FFF, 200px 103px #FFF, 1335px 1107px #FFF, 1712px 30px #FFF, 1984px 191px #FFF, 1897px 1543px #FFF, 1738px 484px #FFF, 340px 832px #FFF, 994px 985px #FFF;
    animation: animStar 90s linear infinite;
}
.stars::after {
    content: " ";
    position: absolute;
    top: 2000px;
    width: 1px; height: 1px;
    box-shadow: 1309px 228px #FFF, 51px 1518px #FFF, 563px 501px #FFF, 457px 285px #FFF, 1508px 209px #FFF, 1385px 1516px #FFF, 1827px 1116px #FFF, 178px 1209px #FFF, 864px 65px #FFF, 61px 191px #FFF, 447px 476px #FFF, 1034px 1232px #FFF, 54px 1149px #FFF, 407px 1466px #FFF, 1330px 1436px #FFF, 1116px 859px #FFF, 451px 919px #FFF, 1206px 569px #FFF, 1657px 1780px #FFF, 13px 1554px #FFF, 1650px 326px #FFF, 1429px 865px #FFF, 696px 569px #FFF, 318px 440px #FFF, 1960px 1563px #FFF, 689px 209px #FFF, 189px 778px #FFF, 198px 735px #FFF, 1735px 704px #FFF, 1236px 541px #FFF, 1652px 88px #FFF, 1494px 940px #FFF, 1098px 255px #FFF, 1992px 1888px #FFF, 775px 161px #FFF, 1130px 600px #FFF, 1698px 1287px #FFF, 1266px 1813px #FFF, 1764px 740px #FFF, 1182px 393px #FFF, 1442px 142px #FFF, 93px 1354px #FFF, 466px 1583px #FFF, 592px 163px #FFF, 1751px 476px #FFF, 1774px 206px #FFF, 778px 569px #FFF, 928px 1301px #FFF, 1708px 747px #FFF, 333px 758px #FFF, 727px 429px #FFF, 1372px 546px #FFF, 1437px 1918px #FFF, 1399px 1327px #FFF, 146px 1247px #FFF, 1300px 350px #FFF, 1093px 1493px #FFF, 501px 334px #FFF, 946px 777px #FFF, 552px 1895px #FFF, 1310px 1409px #FFF, 1140px 449px #FFF, 1402px 664px #FFF, 1726px 1573px #FFF, 1589px 114px #FFF, 469px 1683px #FFF, 65px 1648px #FFF, 646px 821px #FFF, 548px 135px #FFF, 432px 1870px #FFF, 1931px 1161px #FFF, 1794px 1470px #FFF, 644px 435px #FFF, 1342px 1022px #FFF, 810px 1811px #FFF, 1872px 1316px #FFF, 939px 292px #FFF, 542px 285px #FFF, 505px 1525px #FFF, 1149px 1103px #FFF, 538px 1529px #FFF, 1197px 877px #FFF, 1838px 1195px #FFF, 817px 741px #FFF, 449px 283px #FFF, 1043px 1010px #FFF, 186px 1547px #FFF, 96px 1763px #FFF, 224px 313px #FFF, 1285px 327px #FFF, 1622px 1393px #FFF, 864px 1221px #FFF, 130px 788px #FFF, 781px 1220px #FFF, 958px 1083px #FFF, 514px 1988px #FFF, 1133px 1762px #FFF, 1930px 23px #FFF, 1393px 1476px #FFF, 234px 1396px #FFF, 1812px 1099px #FFF, 1537px 546px #FFF, 1574px 1312px #FFF, 696px 228px #FFF, 601px 890px #FFF, 323px 929px #FFF, 6px 1953px #FFF, 1478px 1793px #FFF, 1473px 539px #FFF, 1990px 1025px #FFF, 1560px 365px #FFF, 1039px 1869px #FFF, 217px 1782px #FFF, 1280px 611px #FFF, 1723px 1308px #FFF, 1039px 1247px #FFF, 407px 313px #FFF, 765px 1561px #FFF, 330px 1104px #FFF, 1952px 1594px #FFF, 1889px 1086px #FFF, 1881px 1px #FFF, 1226px 663px #FFF, 1000px 39px #FFF, 229px 1902px #FFF, 743px 1799px #FFF, 1703px 1652px #FFF, 629px 490px #FFF, 118px 493px #FFF, 1798px 1161px #FFF, 1939px 161px #FFF, 175px 1498px #FFF, 995px 1671px #FFF, 141px 1557px #FFF, 1090px 1568px #FFF, 257px 262px #FFF, 1351px 973px #FFF, 1939px 1125px #FFF, 338px 542px #FFF, 1080px 1786px #FFF, 1242px 866px #FFF, 1975px 433px #FFF, 1902px 1104px #FFF, 1546px 1494px #FFF, 1412px 411px #FFF, 1460px 638px #FFF, 817px 1375px #FFF, 1330px 764px #FFF, 897px 1842px #FFF, 1059px 924px #FFF, 247px 507px #FFF, 460px 131px #FFF, 692px 43px #FFF, 1204px 1134px #FFF, 471px 1205px #FFF, 451px 14px #FFF, 145px 1449px #FFF, 1292px 120px #FFF, 468px 138px #FFF, 1854px 64px #FFF, 1760px 676px #FFF, 145px 1052px #FFF, 487px 570px #FFF, 1370px 994px #FFF, 438px 1104px #FFF, 270px 1481px #FFF, 1915px 1807px #FFF, 1169px 1180px #FFF, 968px 497px #FFF, 1606px 968px #FFF, 1653px 833px #FFF, 389px 193px #FFF, 198px 1349px #FFF, 882px 725px #FFF, 867px 841px #FFF, 956px 1769px #FFF, 1493px 110px #FFF, 1379px 1338px #FFF, 1323px 201px #FFF, 124px 824px #FFF, 1491px 694px #FFF, 1639px 1764px #FFF, 223px 509px #FFF, 392px 389px #FFF, 1098px 918px #FFF, 287px 864px #FFF, 375px 570px #FFF, 947px 511px #FFF, 1790px 1890px #FFF, 154px 907px #FFF, 1654px 1764px #FFF, 1753px 1127px #FFF, 200px 103px #FFF, 1335px 1107px #FFF, 1712px 30px #FFF, 1984px 191px #FFF, 1897px 1543px #FFF, 1738px 484px #FFF, 340px 832px #FFF, 994px 985px #FFF;
}
.stars2 {
    box-shadow: 437px 1770px #FFF, 821px 1848px #FFF, 120px 337px #FFF, 776px 4px #FFF, 799px 543px #FFF, 1897px 1605px #FFF, 1607px 931px #FFF, 584px 866px #FFF, 1426px 1960px #FFF, 1496px 1604px #FFF, 1138px 1355px #FFF, 1471px 996px #FFF, 317px 388px #FFF, 607px 445px #FFF, 1983px 119px #FFF, 1186px 1506px #FFF, 1110px 124px #FFF, 1531px 642px #FFF, 117px 102px #FFF, 1196px 976px #FFF, 1029px 1882px #FFF, 1746px 1087px #FFF, 322px 116px #FFF, 1967px 1040px #FFF, 164px 1743px #FFF, 380px 140px #FFF, 1218px 139px #FFF, 1382px 1765px #FFF, 481px 826px #FFF, 245px 1928px #FFF, 1823px 1166px #FFF, 504px 1185px #FFF, 1217px 81px #FFF, 1268px 167px #FFF, 858px 1346px #FFF, 1195px 1157px #FFF, 1070px 647px #FFF, 1914px 534px #FFF, 418px 1371px #FFF, 1466px 643px #FFF, 488px 543px #FFF, 810px 268px #FFF, 1375px 1321px #FFF, 614px 936px #FFF, 647px 1902px #FFF, 1539px 1916px #FFF, 148px 19px #FFF, 938px 1272px #FFF, 1153px 204px #FFF, 150px 1101px #FFF, 436px 1036px #FFF, 543px 271px #FFF, 1911px 714px #FFF, 1804px 140px #FFF, 1800px 500px #FFF, 756px 583px #FFF, 323px 897px #FFF, 1707px 1112px #FFF, 1440px 619px #FFF, 1252px 1652px #FFF, 1339px 1083px #FFF, 16px 1367px #FFF, 1673px 1135px #FFF, 613px 1908px #FFF, 1358px 212px #FFF, 1922px 1798px #FFF, 275px 541px #FFF, 236px 1822px #FFF, 219px 1520px #FFF, 1133px 318px #FFF, 557px 577px #FFF, 1238px 431px #FFF, 1469px 702px #FFF, 416px 1407px #FFF, 1298px 1746px #FFF, 540px 1035px #FFF, 1000px 514px #FFF, 1854px 1859px #FFF, 1732px 104px #FFF, 189px 1299px #FFF;
    animation: animStar 140s linear infinite;
}
.stars2::after {
    content: " ";
    position: absolute;
    top: 2000px;
    width: 2px; height: 2px;
    box-shadow: 437px 1770px #FFF, 821px 1848px #FFF, 120px 337px #FFF, 776px 4px #FFF, 799px 543px #FFF, 1897px 1605px #FFF, 1607px 931px #FFF, 584px 866px #FFF, 1426px 1960px #FFF, 1496px 1604px #FFF, 1138px 1355px #FFF, 1471px 996px #FFF, 317px 388px #FFF, 607px 445px #FFF, 1983px 119px #FFF, 1186px 1506px #FFF, 1110px 124px #FFF, 1531px 642px #FFF, 117px 102px #FFF, 1196px 976px #FFF, 1029px 1882px #FFF, 1746px 1087px #FFF, 322px 116px #FFF, 1967px 1040px #FFF, 164px 1743px #FFF, 380px 140px #FFF, 1218px 139px #FFF, 1382px 1765px #FFF, 481px 826px #FFF, 245px 1928px #FFF, 1823px 1166px #FFF, 504px 1185px #FFF, 1217px 81px #FFF, 1268px 167px #FFF, 858px 1346px #FFF, 1195px 1157px #FFF, 1070px 647px #FFF, 1914px 534px #FFF, 418px 1371px #FFF, 1466px 643px #FFF, 488px 543px #FFF, 810px 268px #FFF, 1375px 1321px #FFF, 614px 936px #FFF, 647px 1902px #FFF, 1539px 1916px #FFF, 148px 19px #FFF, 938px 1272px #FFF, 1153px 204px #FFF, 150px 1101px #FFF, 436px 1036px #FFF, 543px 271px #FFF, 1911px 714px #FFF, 1804px 140px #FFF, 1800px 500px #FFF, 756px 583px #FFF, 323px 897px #FFF, 1707px 1112px #FFF, 1440px 619px #FFF, 1252px 1652px #FFF, 1339px 1083px #FFF, 16px 1367px #FFF, 1673px 1135px #FFF, 613px 1908px #FFF, 1358px 212px #FFF, 1922px 1798px #FFF, 275px 541px #FFF, 236px 1822px #FFF, 219px 1520px #FFF, 1133px 318px #FFF, 557px 577px #FFF, 1238px 431px #FFF, 1469px 702px #FFF, 416px 1407px #FFF, 1298px 1746px #FFF, 540px 1035px #FFF, 1000px 514px #FFF, 1854px 1859px #FFF, 1732px 104px #FFF, 189px 1299px #FFF;
}
.stars3 {
    box-shadow: 867px 1698px #FFF, 566px 90px #FFF, 7px 683px #FFF, 1579px 267px #FFF, 1304px 536px #FFF, 330px 1518px #FFF, 904px 1129px #FFF, 1445px 875px #FFF, 1148px 19px #FFF, 229px 154px #FFF, 1935px 1808px #FFF, 1415px 1851px #FFF, 305px 1117px #FFF, 73px 1709px #FFF, 756px 1192px #FFF, 1131px 303px #FFF, 880px 261px #FFF, 85px 631px #FFF, 746px 1841px #FFF, 1910px 1630px #FFF, 1991px 1762px #FFF, 81px 1840px #FFF, 732px 430px #FFF, 1396px 511px #FFF, 1365px 210px #FFF, 724px 1597px #FFF, 1146px 1810px #FFF, 1791px 832px #FFF, 1994px 1271px #FFF, 1534px 316px #FFF, 1895px 1904px #FFF, 484px 1770px #FFF, 332px 1999px #FFF, 1638px 1660px #FFF, 362px 1805px #FFF, 844px 50px #FFF, 367px 1508px #FFF, 1893px 680px #FFF, 1602px 1906px #FFF, 843px 1642px #FFF;
    animation: animStar 220s linear infinite, twinkle 4s ease-in-out infinite alternate;
}
.stars3::after {
    content: " ";
    position: absolute;
    top: 2000px;
    width: 3px; height: 3px;
    box-shadow: 867px 1698px #FFF, 566px 90px #FFF, 7px 683px #FFF, 1579px 267px #FFF, 1304px 536px #FFF, 330px 1518px #FFF, 904px 1129px #FFF, 1445px 875px #FFF, 1148px 19px #FFF, 229px 154px #FFF, 1935px 1808px #FFF, 1415px 1851px #FFF, 305px 1117px #FFF, 73px 1709px #FFF, 756px 1192px #FFF, 1131px 303px #FFF, 880px 261px #FFF, 85px 631px #FFF, 746px 1841px #FFF, 1910px 1630px #FFF, 1991px 1762px #FFF, 81px 1840px #FFF, 732px 430px #FFF, 1396px 511px #FFF, 1365px 210px #FFF, 724px 1597px #FFF, 1146px 1810px #FFF, 1791px 832px #FFF, 1994px 1271px #FFF, 1534px 316px #FFF, 1895px 1904px #FFF, 484px 1770px #FFF, 332px 1999px #FFF, 1638px 1660px #FFF, 362px 1805px #FFF, 844px 50px #FFF, 367px 1508px #FFF, 1893px 680px #FFF, 1602px 1906px #FFF, 843px 1642px #FFF;
}
@keyframes animStar {
    from { transform: translateY(0px); }
    to { transform: translateY(-2000px); }
}
@keyframes twinkle {
    from { opacity: 0.4; }
    to { opacity: 1; }
}

/* make sure real app content sits above the starfield */
.stApp > header, section[data-testid="stSidebar"], .main .block-container {
    position: relative;
    z-index: 1;
}
</style>
"""

STARFIELD_HTML = """
<div id="starfield-layer">
    <div class="stars"></div>
    <div class="stars2"></div>
    <div class="stars3"></div>
</div>
"""
