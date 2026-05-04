# Tổng hợp công thức hình học: phẳng, không gian, tọa độ, vector

## 1. Kí hiệu nhanh

- Điểm: $A(x_A,y_A)$, $A(x_A,y_A,z_A)$.
- Vector: $\vec{AB}=B-A$.
- Độ dài vector:
  $$
  |\vec u|=\sqrt{u_x^2+u_y^2},\qquad
  |\vec u|=\sqrt{u_x^2+u_y^2+u_z^2}.
  $$
- Tích vô hướng:
  $$
  \vec u\cdot \vec v=|\vec u||\vec v|\cos\theta.
  $$
- Hai vector vuông góc:
  $$
  \vec u\cdot \vec v=0.
  $$
- Hai vector cùng phương:
  $$
  \vec u=k\vec v.
  $$

## 2. Hình học phẳng cơ bản

### 2.1. Tam giác

Với tam giác $ABC$:

- Cạnh:
  $$
  a=BC,\qquad b=CA,\qquad c=AB.
  $$
- Nửa chu vi:
  $$
  p=\frac{a+b+c}{2}.
  $$
- Diện tích:
  $$
  S=\frac12 ah_a=\frac12 bc\sin A.
  $$
- Công thức Heron:
  $$
  S=\sqrt{p(p-a)(p-b)(p-c)}.
  $$
- Định lí cos:
  $$
  a^2=b^2+c^2-2bc\cos A.
  $$
- Định lí sin:
  $$
  \frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}=2R.
  $$
- Bán kính đường tròn ngoại tiếp:
  $$
  R=\frac{abc}{4S}.
  $$
- Bán kính đường tròn nội tiếp:
  $$
  r=\frac{S}{p}.
  $$
- Trung tuyến từ $A$:
  $$
  m_a^2=\frac{2b^2+2c^2-a^2}{4}.
  $$
- Phân giác trong từ $A$:
  $$
  l_a^2=bc\left(1-\frac{a^2}{(b+c)^2}\right).
  $$
- Đường cao:
  $$
  h_a=\frac{2S}{a}.
  $$

### 2.2. Tam giác đặc biệt

- Tam giác vuông:
  $$
  a^2+b^2=c^2.
  $$
- Diện tích tam giác vuông:
  $$
  S=\frac12 ab.
  $$
- Đường cao từ đỉnh vuông xuống cạnh huyền:
  $$
  h^2=mn,\qquad a^2=cm,\qquad b^2=cn,
  $$
  trong đó $c$ là cạnh huyền, $m,n$ là hai đoạn trên cạnh huyền.
- Tam giác đều cạnh $a$:
  $$
  h=\frac{a\sqrt3}{2},\qquad S=\frac{a^2\sqrt3}{4},\qquad R=\frac{a\sqrt3}{3},\qquad r=\frac{a\sqrt3}{6}.
  $$

### 2.3. Tứ giác và đa giác

- Hình bình hành:
  $$
  S=ah=ab\sin\theta.
  $$
- Hình chữ nhật:
  $$
  S=ab,\qquad d=\sqrt{a^2+b^2}.
  $$
- Hình vuông:
  $$
  S=a^2,\qquad d=a\sqrt2.
  $$
- Hình thoi:
  $$
  S=ah=\frac12 d_1d_2.
  $$
- Hình thang:
  $$
  S=\frac{(a+b)h}{2}.
  $$
- Tứ giác nội tiếp:
  $$
  A+C=180^\circ,\qquad B+D=180^\circ.
  $$
- Định lí Ptolemy cho tứ giác nội tiếp $ABCD$:
  $$
  AC\cdot BD=AB\cdot CD+BC\cdot AD.
  $$
- Đa giác đều $n$ cạnh, cạnh $a$:
  $$
  P=na,\qquad S=\frac12 Pr=\frac{na^2}{4\tan(\pi/n)}.
  $$

### 2.4. Đường tròn

- Chu vi, diện tích:
  $$
  C=2\pi R,\qquad S=\pi R^2.
  $$
- Độ dài cung góc ở tâm $\alpha$ rad:
  $$
  l=R\alpha.
  $$
- Diện tích quạt tròn:
  $$
  S_q=\frac12 R^2\alpha.
  $$
- Dây cung chắn góc ở tâm $\alpha$:
  $$
  d=2R\sin\frac{\alpha}{2}.
  $$
- Góc nội tiếp bằng nửa góc ở tâm cùng chắn một cung:
  $$
  \widehat{AMB}=\frac12\widehat{AOB}.
  $$
- Lực của điểm $M$ đối với đường tròn tâm $O$, bán kính $R$:
  $$
  \operatorname{Pow}(M)=MO^2-R^2.
  $$
- Nếu hai cát tuyến từ $M$:
  $$
  MA\cdot MB=MC\cdot MD.
  $$
- Nếu tiếp tuyến $MT$ và cát tuyến $MAB$:
  $$
  MT^2=MA\cdot MB.
  $$

## 3. Tọa độ trong mặt phẳng $Oxy$

### 3.1. Điểm và vector

- Khoảng cách:
  $$
  AB=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}.
  $$
- Trung điểm:
  $$
  M\left(\frac{x_A+x_B}{2},\frac{y_A+y_B}{2}\right).
  $$
- Điểm chia đoạn $AB$ theo tỉ số $AM:MB=m:n$:
  $$
  M\left(\frac{nx_A+mx_B}{m+n},\frac{ny_A+my_B}{m+n}\right).
  $$
- Trọng tâm tam giác:
  $$
  G\left(\frac{x_A+x_B+x_C}{3},\frac{y_A+y_B+y_C}{3}\right).
  $$
- Tích vô hướng:
  $$
  \vec u\cdot\vec v=u_xv_x+u_yv_y.
  $$
- Góc giữa hai vector:
  $$
  \cos\theta=\frac{\vec u\cdot\vec v}{|\vec u||\vec v|}.
  $$

### 3.2. Đường thẳng

- Dạng tổng quát:
  $$
  ax+by+c=0,\qquad \vec n=(a,b).
  $$
- Vector chỉ phương của đường thẳng:
  $$
  \vec u=(b,-a)\quad \text{hoặc}\quad \vec u=(-b,a).
  $$
- Qua điểm $M_0(x_0,y_0)$, có vector chỉ phương $\vec u=(u_1,u_2)$:
  $$
  \frac{x-x_0}{u_1}=\frac{y-y_0}{u_2}.
  $$
- Dạng tham số:
  $$
  \begin{cases}
  x=x_0+u_1t,\\
  y=y_0+u_2t.
  \end{cases}
  $$
- Dạng hệ số góc:
  $$
  y=kx+m.
  $$
- Khoảng cách từ điểm $M(x_0,y_0)$ đến đường thẳng $ax+by+c=0$:
  $$
  d(M,\Delta)=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}.
  $$
- Góc giữa hai đường thẳng có vector pháp tuyến $\vec n_1,\vec n_2$:
  $$
  \cos\varphi=\frac{|\vec n_1\cdot\vec n_2|}{|\vec n_1||\vec n_2|}.
  $$
- Hai đường thẳng song song:
  $$
  a_1b_2-a_2b_1=0.
  $$
- Hai đường thẳng vuông góc:
  $$
  a_1a_2+b_1b_2=0.
  $$

### 3.3. Diện tích bằng tọa độ

- Diện tích tam giác:
  $$
  S_{ABC}=\frac12\left|
  \begin{vmatrix}
  x_A&y_A&1\\
  x_B&y_B&1\\
  x_C&y_C&1
  \end{vmatrix}
  \right|.
  $$
- Dạng khai triển:
  $$
  S_{ABC}=\frac12 |(x_B-x_A)(y_C-y_A)-(y_B-y_A)(x_C-x_A)|.
  $$
- Diện tích đa giác $A_1A_2...A_n$:
  $$
  S=\frac12\left|\sum_{i=1}^{n}(x_iy_{i+1}-y_ix_{i+1})\right|,
  $$
  với $A_{n+1}=A_1$.

### 3.4. Đường tròn

- Dạng chuẩn:
  $$
  (x-a)^2+(y-b)^2=R^2.
  $$
- Dạng tổng quát:
  $$
  x^2+y^2+Dx+Ey+F=0.
  $$
- Tâm và bán kính:
  $$
  I\left(-\frac D2,-\frac E2\right),\qquad
  R=\sqrt{\frac{D^2+E^2}{4}-F}.
  $$
- Tiếp tuyến tại $M(x_0,y_0)$ của đường tròn tâm $I(a,b)$:
  $$
  (x_0-a)(x-x_0)+(y_0-b)(y-y_0)=0.
  $$

### 3.5. Conic thường gặp

- Elip:
  $$
  \frac{x^2}{a^2}+\frac{y^2}{b^2}=1,\qquad c^2=a^2-b^2,\qquad e=\frac ca.
  $$
- Hyperbol:
  $$
  \frac{x^2}{a^2}-\frac{y^2}{b^2}=1,\qquad c^2=a^2+b^2,\qquad e=\frac ca.
  $$
- Parabol:
  $$
  y^2=2px.
  $$

## 4. Vector trong mặt phẳng và không gian

### 4.1. Các phép toán vector

- Cộng, trừ:
  $$
  \vec u+\vec v=(u_1+v_1,u_2+v_2,u_3+v_3).
  $$
- Nhân với số:
  $$
  k\vec u=(ku_1,ku_2,ku_3).
  $$
- Tích vô hướng trong không gian:
  $$
  \vec u\cdot\vec v=u_1v_1+u_2v_2+u_3v_3.
  $$
- Góc giữa hai vector:
  $$
  \cos\theta=\frac{\vec u\cdot\vec v}{|\vec u||\vec v|}.
  $$
- Hình chiếu của $\vec u$ lên $\vec v$:
  $$
  \operatorname{proj}_{\vec v}\vec u=\frac{\vec u\cdot\vec v}{|\vec v|^2}\vec v.
  $$
- Thành phần vuông góc với $\vec v$:
  $$
  \vec u_\perp=\vec u-\operatorname{proj}_{\vec v}\vec u.
  $$

### 4.2. Tích có hướng trong không gian

Với $\vec u=(u_1,u_2,u_3)$, $\vec v=(v_1,v_2,v_3)$:

$$
\vec u\times\vec v=
\begin{vmatrix}
\vec i&\vec j&\vec k\\
u_1&u_2&u_3\\
v_1&v_2&v_3
\end{vmatrix}.
$$

- Độ lớn:
  $$
  |\vec u\times\vec v|=|\vec u||\vec v|\sin\theta.
  $$
- Diện tích hình bình hành:
  $$
  S=|\vec u\times\vec v|.
  $$
- Diện tích tam giác:
  $$
  S=\frac12|\vec u\times\vec v|.
  $$
- Hai vector cùng phương:
  $$
  \vec u\times\vec v=\vec 0.
  $$

### 4.3. Tích hỗn tạp

$$
[\vec u,\vec v,\vec w]=\vec u\cdot(\vec v\times\vec w).
$$

- Thể tích hình hộp:
  $$
  V=|[\vec u,\vec v,\vec w]|.
  $$
- Thể tích tứ diện:
  $$
  V=\frac16|[\vec u,\vec v,\vec w]|.
  $$
- Ba vector đồng phẳng:
  $$
  [\vec u,\vec v,\vec w]=0.
  $$

## 5. Hình học không gian

### 5.1. Công thức thể tích và diện tích

- Lăng trụ:
  $$
  V=S_{\text{đáy}}h.
  $$
- Hình hộp chữ nhật:
  $$
  V=abc,\qquad d=\sqrt{a^2+b^2+c^2}.
  $$
- Hình lập phương:
  $$
  V=a^3,\qquad S_{\text{tp}}=6a^2,\qquad d=a\sqrt3.
  $$
- Chóp:
  $$
  V=\frac13S_{\text{đáy}}h.
  $$
- Chóp cụt:
  $$
  V=\frac h3\left(S_1+S_2+\sqrt{S_1S_2}\right).
  $$
- Trụ:
  $$
  V=\pi R^2h,\qquad S_{\text{xq}}=2\pi Rh,\qquad S_{\text{tp}}=2\pi R(h+R).
  $$
- Nón:
  $$
  V=\frac13\pi R^2h,\qquad S_{\text{xq}}=\pi Rl,\qquad S_{\text{tp}}=\pi R(l+R).
  $$
- Cầu:
  $$
  V=\frac43\pi R^3,\qquad S=4\pi R^2.
  $$

### 5.2. Quan hệ vuông góc, song song

- Đường thẳng $d$ vuông góc mặt phẳng $(P)$ nếu $d$ vuông góc với hai đường thẳng cắt nhau nằm trong $(P)$.
- Hai mặt phẳng vuông góc nếu một mặt phẳng chứa một đường thẳng vuông góc với mặt phẳng kia.
- Đường thẳng song song mặt phẳng nếu song song với một đường thẳng nằm trong mặt phẳng đó.
- Hai mặt phẳng song song nếu chúng có hai cặp đường thẳng cắt nhau tương ứng song song.

### 5.3. Góc và khoảng cách trong không gian

- Góc giữa hai đường thẳng là góc giữa hai vector chỉ phương.
- Góc giữa đường thẳng và mặt phẳng:
  $$
  \sin\varphi=\frac{|\vec u\cdot\vec n|}{|\vec u||\vec n|},
  $$
  trong đó $\vec u$ là vector chỉ phương đường thẳng, $\vec n$ là vector pháp tuyến mặt phẳng.
- Góc giữa hai mặt phẳng:
  $$
  \cos\varphi=\frac{|\vec n_1\cdot\vec n_2|}{|\vec n_1||\vec n_2|}.
  $$
- Khoảng cách từ điểm đến mặt phẳng:
  $$
  d(M,(P))=\frac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}.
  $$
- Khoảng cách giữa hai mặt phẳng song song:
  $$
  d=\frac{|d_1-d_2|}{\sqrt{a^2+b^2+c^2}},
  $$
  nếu chúng có dạng $ax+by+cz+d_1=0$, $ax+by+cz+d_2=0$.

## 6. Tọa độ không gian $Oxyz$

### 6.1. Điểm, vector, mặt cầu

- Khoảng cách:
  $$
  AB=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}.
  $$
- Trung điểm:
  $$
  M\left(\frac{x_A+x_B}{2},\frac{y_A+y_B}{2},\frac{z_A+z_B}{2}\right).
  $$
- Trọng tâm tam giác:
  $$
  G\left(\frac{x_A+x_B+x_C}{3},\frac{y_A+y_B+y_C}{3},\frac{z_A+z_B+z_C}{3}\right).
  $$
- Trọng tâm tứ diện:
  $$
  G\left(\frac{x_A+x_B+x_C+x_D}{4},\frac{y_A+y_B+y_C+y_D}{4},\frac{z_A+z_B+z_C+z_D}{4}\right).
  $$
- Mặt cầu tâm $I(a,b,c)$, bán kính $R$:
  $$
  (x-a)^2+(y-b)^2+(z-c)^2=R^2.
  $$

### 6.2. Đường thẳng trong không gian

Qua $M_0(x_0,y_0,z_0)$, có vector chỉ phương $\vec u=(a,b,c)$:

- Dạng tham số:
  $$
  \begin{cases}
  x=x_0+at,\\
  y=y_0+bt,\\
  z=z_0+ct.
  \end{cases}
  $$
- Dạng chính tắc:
  $$
  \frac{x-x_0}{a}=\frac{y-y_0}{b}=\frac{z-z_0}{c}.
  $$
- Khoảng cách từ điểm $M$ đến đường thẳng $d$ qua $A$, chỉ phương $\vec u$:
  $$
  d(M,d)=\frac{|\,\vec{AM}\times\vec u\,|}{|\vec u|}.
  $$
- Khoảng cách giữa hai đường thẳng chéo nhau $d_1,d_2$, qua $A,B$, chỉ phương $\vec u,\vec v$:
  $$
  d(d_1,d_2)=\frac{|\,\vec{AB}\cdot(\vec u\times\vec v)\,|}{|\vec u\times\vec v|}.
  $$

### 6.3. Mặt phẳng

- Dạng tổng quát:
  $$
  ax+by+cz+d=0,\qquad \vec n=(a,b,c).
  $$
- Qua điểm $M_0(x_0,y_0,z_0)$, có pháp tuyến $\vec n=(a,b,c)$:
  $$
  a(x-x_0)+b(y-y_0)+c(z-z_0)=0.
  $$
- Qua ba điểm $A,B,C$:
  $$
  \vec n=\vec{AB}\times\vec{AC}.
  $$
- Dạng tham số qua điểm $M_0$, có hai vector chỉ phương không cùng phương $\vec u,\vec v$:
  $$
  \begin{cases}
  x=x_0+u_1s+v_1t,\\
  y=y_0+u_2s+v_2t,\\
  z=z_0+u_3s+v_3t.
  \end{cases}
  $$
- Khoảng cách từ điểm $M(x_0,y_0,z_0)$ đến mặt phẳng:
  $$
  d(M,(P))=\frac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}.
  $$

## 7. Kĩ thuật tham số hóa

### 7.1. Tham số hóa đoạn thẳng

Với $A,B$:

$$
M=A+t(B-A),\qquad 0\le t\le1.
$$

- Nếu $t=0$, $M=A$.
- Nếu $t=1$, $M=B$.
- Nếu $t=\frac12$, $M$ là trung điểm.
- Nếu không giới hạn $t$, ta được cả đường thẳng $AB$.

### 7.2. Tham số hóa đường thẳng

Qua $A$, chỉ phương $\vec u$:

$$
M=A+t\vec u,\qquad t\in\mathbb R.
$$

Dùng khi điểm $M$ chạy trên một đường thẳng và cần biến điều kiện hình học thành phương trình theo $t$.

### 7.3. Tham số hóa đường tròn

Đường tròn tâm $I(a,b)$, bán kính $R$:

$$
\begin{cases}
x=a+R\cos t,\\
y=b+R\sin t.
\end{cases}
$$

Với nửa đường tròn hoặc cung tròn, giới hạn miền của $t$.

### 7.4. Tham số hóa mặt phẳng

Mặt phẳng qua $A$, có hai vector chỉ phương $\vec u,\vec v$:

$$
M=A+s\vec u+t\vec v,\qquad s,t\in\mathbb R.
$$

Nếu $M$ nằm trong tam giác $ABC$:

$$
M=A+s(B-A)+t(C-A),\qquad s\ge0,\quad t\ge0,\quad s+t\le1.
$$

### 7.5. Tham số hóa bằng tỉ số

Nếu $M\in AB$ và:

$$
\frac{AM}{MB}=\frac mn,
$$

thì:

$$
M=\frac{nA+mB}{m+n}.
$$

Nếu dùng tham số:

$$
M=A+\frac{m}{m+n}(B-A).
$$

### 7.6. Tham số hóa điều kiện cực trị

Các dạng hay gặp:

- $M$ trên đường thẳng: đặt $M=A+t\vec u$, đưa biểu thức cần tối ưu về hàm một biến $f(t)$.
- $M$ trên đoạn: đặt $t\in[0,1]$, xét thêm hai đầu mút.
- $M$ trên đường tròn: đặt $M=I+R(\cos t,\sin t)$, dùng lượng giác hoặc tích vô hướng.
- $M$ trên mặt phẳng: đặt $M=A+s\vec u+t\vec v$, giải hệ theo $s,t$.

## 8. Kĩ thuật tọa độ hóa

### 8.1. Nguyên tắc chọn hệ tọa độ

- Đặt gốc tọa độ tại điểm đặc biệt: đỉnh vuông, tâm, trọng tâm, trung điểm.
- Đặt trục theo cạnh, đường cao, đường trung tuyến, đường đối xứng.
- Ưu tiên biến ít nhất: cạnh đã biết đặt trùng trục để nhiều tọa độ bằng $0$.
- Với hình vuông, chữ nhật, hộp chữ nhật: đặt các cạnh song song trục.
- Với tam giác vuông: đặt đỉnh vuông tại $O$, hai cạnh góc vuông theo $Ox,Oy$.
- Với hình chóp có đáy phẳng: đặt đáy trong mặt phẳng $Oxy$, chiều cao theo $Oz$.

### 8.2. Mẫu tọa độ hóa thường dùng

- Tam giác vuông tại $A$:
  $$
  A(0,0),\qquad B(b,0),\qquad C(0,c).
  $$
- Tam giác cân tại $A$, đáy $BC$:
  $$
  B(-a,0),\qquad C(a,0),\qquad A(0,h).
  $$
- Tam giác đều cạnh $a$:
  $$
  A(0,0),\qquad B(a,0),\qquad C\left(\frac a2,\frac{a\sqrt3}{2}\right).
  $$
- Hình chữ nhật:
  $$
  A(0,0),\quad B(a,0),\quad C(a,b),\quad D(0,b).
  $$
- Hình hộp chữ nhật:
  $$
  A(0,0,0),\quad B(a,0,0),\quad D(0,b,0),\quad A'(0,0,c).
  $$
- Chóp có đáy $ABC$ nằm trên $Oxy$, chân đường cao tại $H(x_H,y_H,0)$:
  $$
  S(x_H,y_H,h).
  $$

### 8.3. Quy trình tọa độ hóa

1. Chọn hệ trục làm nhiều tọa độ bằng $0$.
2. Gán tọa độ các điểm cố định.
3. Biểu diễn điểm động bằng tham số.
4. Chuyển điều kiện hình học thành phương trình tọa độ hoặc vector.
5. Giải phương trình, rồi kiểm tra miền tham số.

## 9. Kĩ thuật tách vector

### 9.1. Tách theo hai vector cơ sở

Nếu $\vec u,\vec v$ không cùng phương, mọi vector trong mặt phẳng của chúng có thể viết:

$$
\vec x=\alpha\vec u+\beta\vec v.
$$

Dùng khi muốn biến quan hệ hình học thành hệ phương trình theo $\alpha,\beta$.

### 9.2. Tách theo ba vector cơ sở trong không gian

Nếu $\vec u,\vec v,\vec w$ không đồng phẳng:

$$
\vec x=\alpha\vec u+\beta\vec v+\gamma\vec w.
$$

Các hệ số $\alpha,\beta,\gamma$ thường tìm bằng cách so sánh tọa độ hoặc giải hệ tuyến tính.

### 9.3. Tách vector theo phương song song và vuông góc

Với vector $\vec a$ và phương $\vec u$:

$$
\vec a=\vec a_{\parallel}+\vec a_{\perp}.
$$

Trong đó:

$$
\vec a_{\parallel}=\frac{\vec a\cdot\vec u}{|\vec u|^2}\vec u,\qquad
\vec a_{\perp}=\vec a-\vec a_{\parallel}.
$$

Dùng nhiều trong bài toán khoảng cách, hình chiếu, cực trị.

### 9.4. Tách vector trong tam giác

Với tam giác $ABC$, chọn gốc tại $A$:

$$
\vec{AM}=x\vec{AB}+y\vec{AC}.
$$

- $M$ nằm trên đường thẳng $BC$:
  $$
  x+y=1.
  $$
- $M$ nằm trong tam giác $ABC$:
  $$
  x\ge0,\qquad y\ge0,\qquad x+y\le1.
  $$
- $M$ là trung điểm $BC$:
  $$
  \vec{AM}=\frac12\vec{AB}+\frac12\vec{AC}.
  $$
- $G$ là trọng tâm:
  $$
  \vec{AG}=\frac13\vec{AB}+\frac13\vec{AC}.
  $$

### 9.5. Tách bằng trọng số affine

Điểm $M$ được biểu diễn bởi các điểm $A_1,A_2,\dots,A_n$:

$$
M=\lambda_1A_1+\lambda_2A_2+\cdots+\lambda_nA_n,
$$

với:

$$
\lambda_1+\lambda_2+\cdots+\lambda_n=1.
$$

Nếu mọi $\lambda_i\ge0$, điểm $M$ nằm trong bao lồi của các điểm $A_i$.

## 10. Công thức hình chiếu, đối xứng, khoảng cách

### 10.1. Hình chiếu điểm lên đường thẳng trong mặt phẳng

Đường thẳng $\Delta: ax+by+c=0$, điểm $M(x_0,y_0)$. Hình chiếu $H$:

$$
H\left(
x_0-\frac{a(ax_0+by_0+c)}{a^2+b^2},
y_0-\frac{b(ax_0+by_0+c)}{a^2+b^2}
\right).
$$

### 10.2. Điểm đối xứng qua đường thẳng

Nếu $H$ là hình chiếu của $M$ lên $\Delta$, điểm $M'$ đối xứng với $M$ qua $\Delta$:

$$
M'=2H-M.
$$

### 10.3. Hình chiếu điểm lên mặt phẳng

Mặt phẳng $(P): ax+by+cz+d=0$, điểm $M(x_0,y_0,z_0)$. Hình chiếu $H$:

$$
H=M-\frac{ax_0+by_0+cz_0+d}{a^2+b^2+c^2}(a,b,c).
$$

### 10.4. Điểm đối xứng qua mặt phẳng

Nếu $H$ là hình chiếu của $M$ lên $(P)$, điểm đối xứng $M'$:

$$
M'=2H-M.
$$

## 11. Kĩ thuật giải nhanh theo dạng bài

### 11.1. Chứng minh vuông góc

Các hướng thường dùng:

- Chứng minh tích vô hướng bằng $0$.
- Chứng minh đường thẳng vuông góc với hai đường cắt nhau trong mặt phẳng.
- Dùng định lí Pythagore đảo.
- Dùng vector pháp tuyến hoặc vector chỉ phương.

### 11.2. Chứng minh song song

Các hướng thường dùng:

- Chứng minh hai vector cùng phương.
- Chứng minh hai đường có cùng vector pháp tuyến hoặc chỉ phương.
- Dùng định lí Thales, đường trung bình.
- Trong không gian, chứng minh đường thẳng song song với một đường nằm trong mặt phẳng.

### 11.3. Tính góc

Các hướng thường dùng:

- Đưa về góc giữa hai vector:
  $$
  \cos\theta=\frac{\vec u\cdot\vec v}{|\vec u||\vec v|}.
  $$
- Đường thẳng và mặt phẳng:
  $$
  \sin\varphi=\frac{|\vec u\cdot\vec n|}{|\vec u||\vec n|}.
  $$
- Hai mặt phẳng:
  $$
  \cos\varphi=\frac{|\vec n_1\cdot\vec n_2|}{|\vec n_1||\vec n_2|}.
  $$

### 11.4. Tính khoảng cách

Các hướng thường dùng:

- Điểm đến đường thẳng trong $Oxy$:
  $$
  d=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}.
  $$
- Điểm đến mặt phẳng trong $Oxyz$:
  $$
  d=\frac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}.
  $$
- Điểm đến đường thẳng trong không gian:
  $$
  d=\frac{|\,\vec{AM}\times\vec u\,|}{|\vec u|}.
  $$
- Hai đường chéo nhau:
  $$
  d=\frac{|\,\vec{AB}\cdot(\vec u\times\vec v)\,|}{|\vec u\times\vec v|}.
  $$

### 11.5. Tính diện tích và thể tích bằng vector

- Tam giác:
  $$
  S=\frac12|\vec{AB}\times\vec{AC}|.
  $$
- Hình bình hành:
  $$
  S=|\vec{AB}\times\vec{AD}|.
  $$
- Tứ diện:
  $$
  V=\frac16|\vec{AB}\cdot(\vec{AC}\times\vec{AD})|.
  $$
- Hình hộp:
  $$
  V=|\vec{AB}\cdot(\vec{AD}\times\vec{AA'})|.
  $$

## 12. Bảng chọn công cụ

| Dạng bài | Công cụ nên nghĩ tới |
|---|---|
| Tính độ dài | Khoảng cách tọa độ, định lí cos, Pythagore |
| Tính góc | Tích vô hướng, vector chỉ phương, pháp tuyến |
| Vuông góc | Tích vô hướng bằng $0$, đường vuông góc mặt phẳng |
| Song song | Vector cùng phương, tích có hướng bằng $\vec0$ |
| Diện tích | Heron, $\frac12 ah$, định thức, tích có hướng |
| Thể tích | $S_{\text{đáy}}h$, tích hỗn tạp |
| Điểm chạy trên đường | Tham số hóa $M=A+t\vec u$ |
| Điểm chạy trên đoạn | $M=A+t(B-A)$, $0\le t\le1$ |
| Điểm trong tam giác | $M=A+s(B-A)+t(C-A)$, $s,t\ge0,s+t\le1$ |
| Cực trị khoảng cách | Hình chiếu, tách vector song song/vuông góc |
| Bài hình không gian khó dựng | Tọa độ hóa đáy trên $Oxy$, chiều cao theo $Oz$ |
