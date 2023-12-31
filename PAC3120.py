from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

class Medidor():
    direccion_ip = ""
    puerto = ""
    id = 0
    def __init__(self, direccion_ip, puerto, id):
        self.direccion_ip = direccion_ip
        self.puerto = puerto
        self.id = id
    def get_active_power(self):
        client = ModbusTcpClient(host=self.direccion_ip, port=self.puerto)
        if client.connect() == True:
            try:
                L1_active = client.read_holding_registers(25,2,self.id)
                L2_active = client.read_holding_registers(27,2,self.id)
                L3_active = client.read_holding_registers(29,2,self.id)
                real_decoder_L1 = BinaryPayloadDecoder.fromRegisters(L1_active.registers, byteorder=Endian.Big, wordorder=Endian.Little)
                real_decoder_L2 = BinaryPayloadDecoder.fromRegisters(L2_active.registers, byteorder=Endian.Big, wordorder=Endian.Little)
                real_decoder_L3 = BinaryPayloadDecoder.fromRegisters(L3_active.registers, byteorder=Endian.Big, wordorder=Endian.Little)
                L1_active = real_decoder_L1.decode_32bit_float()
                L2_active = real_decoder_L2.decode_32bit_float()
                L3_active = real_decoder_L3.decode_32bit_float()
                return [L1_active,L2_active,L3_active]
            except Exception as e:
                print("No se puedo conectar con el dispositivo")
                print("Error al obtener las potencias activas")
                print("Revisar si el Id del dispositivo es correcto")
                print(e)
                return "Bad"
        else:
            return "Bad"
    def get_reactive_power(self):
        client = ModbusTcpClient(host=self.direccion_ip, port=self.puerto)
        if client.connect() == True:
            try:
                L1_reactive = client.read_holding_registers(31,2,self.id)
                L2_reactive = client.read_holding_registers(33,2,self.id)
                L3_reactive = client.read_holding_registers(35,2,self.id)
                real_decoder_L1 = BinaryPayloadDecoder.fromRegisters(L1_reactive.registers, byteorder=Endian.Big, wordorder=Endian.Little)
                real_decoder_L2 = BinaryPayloadDecoder.fromRegisters(L2_reactive.registers, byteorder=Endian.Big, wordorder=Endian.Little)
                real_decoder_L3 = BinaryPayloadDecoder.fromRegisters(L3_reactive.registers, byteorder=Endian.Big, wordorder=Endian.Little)
                L1_reactive = real_decoder_L1.decode_32bit_float()
                L2_reactive = real_decoder_L2.decode_32bit_float()
                L3_reactive = real_decoder_L3.decode_32bit_float()
                return [L1_reactive,L2_reactive,L3_reactive]
            except Exception as e:
                print("No se puedo conectar con el dispositivo")
                print("Error al obtener las potencias reactivas")
                print("Revisar si el Id del dispositivo es correcto")
                print(e)
                return "Bad"                
        else:
            return "Bad"
    def get_power_factor(self):
        client = ModbusTcpClient(host=self.direccion_ip, port=self.puerto)
        if client.connect() == True:
            try:
                L1_factor = client.read_holding_registers(37,2,self.id)
                L2_factor = client.read_holding_registers(39,2,self.id)
                L3_factor = client.read_holding_registers(41,2,self.id)
                real_decoder_L1 = BinaryPayloadDecoder.fromRegisters(L1_factor.registers, byteorder=Endian.Big, wordorder=Endian.Little)
                real_decoder_L2 = BinaryPayloadDecoder.fromRegisters(L2_factor.registers, byteorder=Endian.Big, wordorder=Endian.Little)
                real_decoder_L3 = BinaryPayloadDecoder.fromRegisters(L3_factor.registers, byteorder=Endian.Big, wordorder=Endian.Little)
                L1_factor = real_decoder_L1.decode_32bit_float()
                L2_factor = real_decoder_L2.decode_32bit_float()
                L3_factor = real_decoder_L3.decode_32bit_float()
                return [round(L1_factor,2),round(L2_factor,2),round(L3_factor,2)]
            except Exception as e:
                print("No se puedo conectar con el dispositivo")
                print("Error al obtener los factores de potencia")
                print("Revisar si el Id del dispositivo es correcto")
                print(e)
                return "Bad"                
        else:
            return "Bad"





