import jetFunctions as jet
import numpy as np
import time

try:
    jet.initStepMotorGpio()
    measures = []
    x = []
    i = 1
    jet.initSpiAdc()
    #данная часть скрипта для получения показаний при выключенном вентиляторе
    a = 0
    for i in range(500):
        adc = jet.getAdc()
        measures.append(adc) #затем этот массив отдельно выводим в файл "00Pa.txt"
        a += adc    

    motorSteps = 0
    samplesInMeasure = 50
    count = 500

    with open("/home/gr106/Desktop/Scripts/00Pa.txt", "w") as outfile:
        outfile.write('- Jet Lab\n\n')
        outfile.write('- Experiment date = {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        outfile.write('- Number of samples in measure = {}\n'.format(samplesInMeasure))
        outfile.write('- Number of motor steps between measures = {}\n'.format(motorSteps))
        outfile.write('- Measures count = {}\n\n'.format(count))
            
        outfile.write('- adc12bit\n')
        np.savetxt(outfile, np.array(measures).T, fmt='%d')

time.sleep(30)


#данная часть скрипта для получения показаний при включенном вентиляторе
    a = 0
    measures = []
    for i in range(500):
        adc = jet.getAdc()
        measures.append(adc) #затем этот массив отдельно выводим в файл "00Pa.txt"
        a += adc    

    motorSteps = 0
    samplesInMeasure = 50
    count = 500

    with open("/home/gr106/Desktop/Scripts/00Pa.txt", "w") as outfile:
        outfile.write('- Jet Lab\n\n')
        outfile.write('- Experiment date = {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        outfile.write('- Number of samples in measure = {}\n'.format(samplesInMeasure))
        outfile.write('- Number of motor steps between measures = {}\n'.format(motorSteps))
        outfile.write('- Measures count = {}\n\n'.format(count))

        outfile.write('- adc12bit\n')
        np.savetxt(outfile, np.array(measures).T, fmt='%d')

finally:
    jet.deinitStepMotorGpio()