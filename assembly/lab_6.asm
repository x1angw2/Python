; 将 datasg 段中每个单词的前 4 个字母改为大写字母
assume cs:codesg, ss:stacksg, ds:datasg

stacksg segment
	dw 0, 0, 0, 0, 0, 0, 0, 0
stacksg ends

datasg segment
	db '1. display      '
	db '2. brows        '
	db '3. replace      '
	db '4. modify       '
datasg ends

codesg segment

	start:	mov ax,stacksg
			mov ss,ax				; 定义栈段地址
			mov sp,10h

			mov ax,datasg
			mov ds,ax				; 定义数据段地址
	
			mov bx,0
			mov si,0
			mov cx,4
		s:	push cx
			mov cx,4
		s0:	mov al,[bx + si + 3]
			and al,11011111b
			mov [bx + si + 3],al
			inc si
			loop s0
			
			mov si,0

			add bx,10h
			pop cx
			loop s

			mov ax, 4c00h
			int 21h

codesg ends

end start
