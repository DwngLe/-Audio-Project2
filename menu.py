import numpy as np
from filter import Filter
from window import Window
from signal_class import Signal
from show import Show
from write import Write
from play import Play

class Menu:
    def Menu3( x, y, fs):
        while(True):
            print("---------------------Menu-----------------")
            print("0. Thoát")
            print("1. In đồ thị")
            print("2. In phổ")
            print("3. Lưu đoạn âm thanh")
            print("4. Nghe đoạn âm thanh gốc")
            print("5. Nghe đoạn âm thanh đã qua chỉnh sửa")
            print("-------------------------------------------")
            print("Nhap lua chon:")

            lua_chon = int(input())

            print("-------------------------------------------")    
            if lua_chon == 0:
                break
            if lua_chon == 1:
                Show.show_do_thi(x, y)
            if lua_chon == 2:
                Show.show_pho(x, y)
            if lua_chon == 3:
                Write.ghi_am_thanh(y, fs)
                break
            if lua_chon == 4:
                Play.phat(x, fs)
            if lua_chon == 5:
                Play.phat(y, fs)

    def Menu2(N):
        while(True):
            print("---------------------Menu cửa sổ-----------------")
            print("0. Thoát")
            print("1. Cửa sổ hcn")
            print("2. Cửa sổ tam giác")
            print("3. Cửa sổ hanning")
            print("4. Cửa sổ hamming")
            print("5. Cửa sổ blackman")
            print("-------------------------------------------")
            print("Nhap lua chon:")

            lua_chon = int(input())

            print("-------------------------------------------")

            if lua_chon == 0:
                break
            if lua_chon == 1:
                w  = Window.rectangular(N)
                return w
            if lua_chon == 2:
                w = Window.triangular(N)
                return w
            if lua_chon == 3:
                w = Window.hanning(N)
                return w
            if lua_chon == 4:
                w = Window.hamming(N)
                return w
            if lua_chon == 5:
                w = Window.blackman(N)
                return w

    def Menu1(x, fs):
        while(True):
            print("---------------------Menu bộ lọc-----------------")
            print("0. Thoát")
            print("1. Bộ lọc LBF")
            print("2. Bộ lọc HBF")
            print("3. Bộ lọc BPF")
            print("4. Bộ lọc BSF")
            print("-------------------------------------------")
            print("Nhap lua chon:")

            lua_chon = int(input())
            print("Nhập N:")
            N = int(input())
            print("-------------------------------------------")
            
            if lua_chon ==0:
                break

            if lua_chon == 1:
                print("Nhập tần số cắt:")
                fc = int(input())
                w = Menu.Menu2(N)
                hd = Filter.lpf(fc, fs, N, w)
                y = np.convolve(x, hd)
                print(y)
                Menu.Menu3(x, y, fs)
                break

            if lua_chon == 2:
                print("Nhập tần số cắt:")
                fc = int(input())
                w = Menu.Menu2(N)
                hd = Filter.hpf(fc, fs, N, w)
                y = np.convolve(x, hd)
                print(y)
                Menu.Menu3(x, y, fs)
                break

            if lua_chon == 3:
                print("Nhập tần số cắt 1:")
                fc1 = int(input())
                print("Nhập tần số cắt 2:")
                fc2 = int(input())
                w = Menu.Menu2(N)
                hd= Filter.bpf(fc1, fc2, fs, N, w)
                y = np.convolve(x, hd)
                print(y)
                Menu.Menu3(x, y, fs)
                break
            
            if lua_chon == 4:
                print("Nhập tần số cắt 1:")
                fc1 = int(input())
                print("Nhập tần số cắt 2:")
                fc2 = int(input())
                w = Menu.Menu2(N)
                hd= Filter.bsf(fc1, fc2, fs, N, w)
                y = np.convolve(x, hd)
                print(y)
                Menu.Menu3(x, y, fs)
                break


    