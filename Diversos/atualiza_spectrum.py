from xml.dom import minidom
import logging
import requests

logFile= ("C:\\Users\\celestip\\Desktop\\Alterar IP\\Offline.log")
csv = ("C:\\Users\\celestip\\Desktop\\Alterar IP\\report.csv")
xml = minidom.parse("C:\\Users\\celestip\\Desktop\\Alterar IP\\devices.xml")
#response = requests.get("http://10.3.5.11:8080/spectrum/restful/devices?throttlesize=5000&attr=0x12d7f")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger_handler = logging.FileHandler(logFile, mode='w')
logger_handler.setLevel(logging.INFO)
logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)

x = 0
y = 0
z = 0
t = 0

def busca(ip_sp):
    global x, y, z, t
    arquivo = open( csv, 'r', encoding="utf8")
    for linha in arquivo:
        linha = linha.split(',')
        ip_cc = linha[16]
        x += 1
        
        if ip_sp[-9:] == ip_cc[-9:]:
            y += 1
            if ip_sp == ip_cc:
                z += 1                
            else:
                logger.info( "IP no CC: %s - IP no Spectrum: %s - Atualizar MH: %s" % (ip_cc,ip_sp,mh))
                try:
                    logger.info("PUT URL : http://10.3.5.11:8080/spectrum/restful/model/"+ mh +"?attr=0x12d7f&val="+ ip_cc)
#                   response = requests.put("http://10.3.5.11:8080/spectrum/restful/model/"+ mh +"?attr=0x12d7f&val="+ temp)
                    logger.info('SPECTRUM UPDATE OK')
                except:
                    logger.error('FALHA AO ATUALIZAR')
                t += 1            
            break
    arquivo.close()

models = xml.getElementsByTagName("model")
logger.info("INICIANDO LEITURA DO XML DO SPECTRUM")
for model in models:
    mh = model.getAttribute("mh")
    ip_sp = model.getElementsByTagName("attribute")[0]
    ip_sp = ip_sp.firstChild.data
    logger.info("MH = %s | IP = %s" % (mh,ip_sp))
    busca(ip_sp)        

print(x)
print(y)
print(z)
print(t)