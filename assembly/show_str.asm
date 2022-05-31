; 功能  在指定的位置，用指定的颜色，显示一个用 0 结束的字符串
; 参数  (dh) = 行号 (取值范围 0 ~ 24)
;		(dl) = 列号 (取值范围 0 ~ 79)
;		(cl) = 颜色  ds:si 指向字符串的首地址
; 返回  无
assume cs:codesg
data segment
	db 'welcome to masm!',0
	db 'XIANG WEI ZHANG', 0
data ends
codesg segment

	start:	mov ax, data
			mov ds, ax

			mov si, 0									
			mov dh, 12
			mov dl, 12
			mov cl, 9ch							; 调用子程序前 相关设置

			call show_str						

			mov si,11h
			mov dh,13
			mov dl,12
			mov cl,0cfh							; 调用子程序前 相关设置

			call show_str

			mov ax, 4c00h
			int 21h



show_str:	push cx
			push es
			push ax
			push dx
			push ds
			push si
			push di							; 备份需要用到的寄存器

			mov ax,0b800h
			mov es,ax						; 设置显存基地址
			

			mov ax,0
			mov al,dh
			mov dh,160
			mul dh							; 每行 160 个字节 

			push ax
			mov ax,0
			mov al,dl
			mov dh,2
			mul dh							; 每列 2 个字节
			pop dx
			add ax, dx						; 组合起来的偏移地址
			mov di,ax						

			mov ah,cl						; 偶字节 显示颜色 奇字节显示字符    高 为 奇
			mov cl,0						; 设置 cl 方便 和 ch 组合跳出循环
											
											; 开始循环
go:			mov al, ds:[si]					; 取字符，放低位
			mov ch, ds:[si]					; 取字符，放高位   判断是否循环
			jcxz ok
			inc si
			mov es:[di], ax					; 写数据到显存
			add di, 2
			jmp short go

ok:			pop di							; 还原寄存器信息
			pop si
			pop ds
			pop dx
			pop ax
			pop es
			pop cx
			ret


codesg ends

end start
