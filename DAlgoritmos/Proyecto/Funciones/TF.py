import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import scipy.signal as spsignal

# Función para la Transformada Rápida de Fourier (FFT) recursiva
def fft_recursive(x):
    N = len(x)
    if N <= 1:  # Caso base: si solo hay un elemento, retornamos x
        return x
    elif np.log2(N) % 1 > 0:  # La longitud debe ser una potencia de 2
        raise ValueError("La longitud del array debe ser una potencia de 2.")
    
    # Separamos los elementos pares e impares
    even = fft_recursive(x[::2])
    odd = fft_recursive(x[1::2])
    
    # Calculamos los términos exponenciales
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Función para la Transformada Inversa de Fourier
def ifft_recursive(X):
    N = len(X)
    if N <= 1:
        return X
    # Hacemos la transformada directa pero ajustando el signo del exponente
    X_conj = np.conj(X)  # Conjugado complejo
    result = fft_recursive(X_conj)
    return np.conj(result) / N  # Escalamos por N y volvemos a tomar el conjugado

# Función para aplicar un filtro pasabajas
def low_pass_filter(data, cutoff_freq, sample_rate):
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = spsignal.butter(4, normal_cutoff, btype='low', analog=False)
    return spsignal.filtfilt(b, a, data)

# Leer archivo de audio
def read_audio(file_path):
    sample_rate, data = wavfile.read(file_path)
    return sample_rate, data

# Guardar archivo de audio
def write_audio(file_path, sample_rate, data):
    wavfile.write(file_path, sample_rate, data)

# Graficar las frecuencias
def plot_frequencies(frequencies, title="Espectro de Frecuencias"):
    plt.figure(figsize=(10, 6))
    plt.plot(np.abs(frequencies))
    plt.title(title)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")
    plt.show()

# Main
if __name__ == "__main__":
    # Parámetros
    input_audio = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto\\Archivos\\Proyecto7\\Audios\\entrada.wav"  # Archivo de entrada
    output_audio = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto\\Archivos\\Proyecto7\\Audios\\salida_filtrada.wav"  # Archivo de salida
    cutoff_frequency = 1000  # Frecuencia de corte en Hz
    
    # 1. Leer el archivo de audio
    sample_rate, data = read_audio(input_audio)
    print("Frecuencia de muestreo:", sample_rate, "Hz")
    
    # Asegurar que sea mono (1 canal)
    if len(data.shape) > 1:
        data = data[:, 0]
    
    # Asegurar longitud como potencia de 2 para la FFT
    N = len(data)
    N_pow2 = 1 << (N - 1).bit_length()
    padded_data = np.zeros(N_pow2)
    padded_data[:N] = data
    
    # 2. Aplicar la FFT
    print("Calculando la FFT...")
    fft_result = fft_recursive(padded_data)
    
    # 3. Graficar el espectro de frecuencias
    plot_frequencies(fft_result, "Espectro Original de Frecuencias")
    
    # 4. Aplicar el filtro pasabajas
    print("Aplicando filtro pasabajas...")
    filtered_signal = low_pass_filter(padded_data, cutoff_frequency, sample_rate)
    
    # Graficar las frecuencias filtradas
    fft_filtered = fft_recursive(filtered_signal)
    plot_frequencies(fft_filtered, "Espectro Filtrado de Frecuencias")
    
    # 5. Aplicar la IFFT
    print("Aplicando IFFT...")
    ifft_result = ifft_recursive(fft_filtered)
    
    # 6. Guardar el resultado en un archivo de audio
    print("Guardando el archivo de salida...")
    output_signal = np.int16(np.real(ifft_result[:N]))  # Tomamos la parte real y luego convertimos
    write_audio(output_audio, sample_rate, output_signal)
    print("Proceso completado. Archivo guardado como:", output_audio)
