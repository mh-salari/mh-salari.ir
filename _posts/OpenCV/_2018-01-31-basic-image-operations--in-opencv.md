---
layout: fa-post
custom_css: fa-post

title: "اعمال مقدماتی بر روی عکس در OpenCV"
date: 2018-01-31T13:53:59+03:30
tags: [ Python, OpenCV]
image: /assets/post-images/opencv/basic-image-operations-in-opencv/basic_image_operations_in_opencv.jpg
headerImage: true
description: " در این نوشته یاد می‌گیرم که چطور یک عکس رو در OpenCV بخوانیم، روی اون اعمال مقدماتی‌ای همچون تغییر اندازه، برش، چرخش، تبدیل رنگ عکس به خاکستری و ... رو انجام دهیم، عکس رو نمایش بدهیم و در نهایت نتیجه رو دخیره کنیم."
category: OpenCV
author: Hue Salari
externalLink: false
---


در این نوشته یاد می‌گیرم که چطور یک عکس رو در OpenCV بخوانیم، روی اون اعمال مقدماتی‌ای همچون تغییر اندازه، برش، چرخش، تبدیل رنگ عکس به خاکستری و ... رو انجام دهیم، عکس رو نمایش بدهیم و در نهایت نتیجه رو با فرمت دلخواه دخیره کنیم.


## خواندن، نمایش، تغییر رنگ و ذخیره‌ی عکس در OpenCV:

در OpenCV جهت خواندن عکس از دستور _imread_ جهت دخیره ی تصویر در حافظه از _imwrite_ و جهت نمایش آن از دستور _imshow_ استفاده می‌کنیم:

دستورهای بالا رو در عمل ببینیم تا بیشتر توضیح بدم:

{% highlight python linenos %}

#فرا خواندن کتابخانه‌ی Opencv
import cv2

#بارگذاری یک عکس از آدرسی در حافظه
image = cv2.imread("mrFox.jpg")

#بررسی می‌کنیم که آیا عکس به شکل صحیح بارگذاری شده است یا نه
if image is None:
        print ("Coud not open or find the image")

#با این دستور عکس رنگی را به سیاه و سفید تبدیل می‌کنیم
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#ذخیره نتیجه تبدیل عکس رنگی به سیاه و سفید
cv2.imwrite("grayImage.jpg",grayImage)

#ایجاد پنجره برای نمایش عکس‌ها
cv2.namedWindow("Image",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Gray Image",cv2.WINDOW_NORMAL)

#نمایش عکس‌ها
cv2.imshow("Image",image)
cv2.imshow("Gray Image",grayImage)

#صبر می‌کنیم تا یک کلید فشرده شود
cv2.waitKey(0)

{% endhighlight %}

 <img src="/assets/post-images/opencv/basic-image-operations-in-opencv/opencv_read_images_display.jpg" alt="Open and display images in Opencv" style="width:600px;height:auto;display: block;margin: 0 auto;"> 
 <img src="/assets/post-images/opencv/basic-image-operations-in-opencv/opencv_read_images_folder.png" alt="Open and display images in Opencv (folder)" style="width:600px;height:auto;display: block;margin: 0 auto;"> 




دستور _imread_ دو ورودی می‌گیره، ورودی اول اسم و آدرس عکس ذخیره شده در حافظه و ورودی دوم اون یک فلک است که color type عکس رو مشخص می‌کنه.

<p dir="ltr" style="text-align: left;">
  <span style="color: #034239;"><strong><tt class="descclassname">cv2.</tt><tt class="descname"><span class="highlighted">imread</span></tt><big>(</big>filename<span class="optional">[</span>, flags<span class="optional">]</span><big>)</big></strong></span>
</p>

<p dir="ltr" style="text-align: left;">
  <span style="color: #034239;"><strong>Parameters:</strong></span>
</p>

<ul class="first last simple" dir="ltr">
  <li style="text-align: left;">
    <span style="color: #034239;"><strong>filename</strong> – Name of file to be loaded.</span>
  </li>
  <li>
    <span style="color: #034239;"><strong>flags</strong> –</span> <p style="text-align: left;">
      <span style="color: #034239;">Flags specifying the color type of a loaded image:</span>
    </p>
    
    <ul>
      <li style="text-align: left;">
        <span style="color: #034239;">CV_LOAD_IMAGE_ANYDEPTH &#8211; If set, return 16-bit/32-bit image when the input has the corresponding depth, otherwise convert it to 8-bit.</span>
      </li>
      <li style="text-align: left;">
        <span style="color: #034239;">CV_LOAD_IMAGE_COLOR &#8211; If set, always convert image to the color one</span>
      </li>
      <li style="text-align: left;">
        <span style="color: #034239;">CV_LOAD_IMAGE_GRAYSCALE &#8211; If set, always convert image to the grayscale one</span>
      </li>
      <li style="text-align: left;">
        <dl class="first docutils">
          <dt>
            <span style="color: #034239;"><strong>>0</strong> Return a 3-channel color image.</span>
          </dt>
          
          <dd>
            <div class="first last admonition note">
              <p class="first admonition-title">
                <span style="color: #034239;">Note</span>
              </p>
              
              <p class="last">
                <span style="color: #034239;">In the current implementation the alpha channel, if any, is stripped from the output image. Use negative value if you need the alpha channel.</span>
              </p>
            </div>
          </dd>
        </dl>
      </li>
      
      <li style="text-align: left;">
        <span style="color: #034239;"><strong>=0</strong> Return a grayscale image.</span>
      </li>
      <li style="text-align: left;">
        <span style="color: #034239;"><strong><0</strong> Return the loaded image as is (with alpha channel).</span>
      </li>
    </ul>
  </li>
</ul>

ما می‌توینم بجای سه Falg بالا از 1، 0 و -1 استفاده کنیم. همچنین مقدار پیش‌فرض ورودی دوم CV\_LOAD\_IMAGE_COLOR است.

دقت کنید  اگر عکسی که آدرس اون رو به دستور _imread_ می‌دهیم وجود نداشته باشه ما خطایی نمی‌گیریم (در عمل یک عکس خالی [None] ایجاد میشه)، برای همین بهتره چک کنیم که آیا عکس به درستی بارگذاری شده یا نه [خط ۸ و ۹.]

در خط ۱۲ با استفاده از دستور _cvtColor_ می‌توانیم رنگ عکس رو تغییر بدهیم، توضیح کامل این دستور در [این لینک][3].

در خط ۱۵ ما عکس خاکستری تولید شده از روی عکس اصلی رو با دستور _imwrite_ ذخیره کرده‌ایم.
به خط ۱۸ توجه کنید، برای نمایش تصاویر ابتدا به وسیله‌ی دستور_cv2.namedWindow_ یک پنجره ایجاد می‌کتیم، این دستور جدا از اسم پنجره سه پارامتر دیگه هم می‌گیره:

<p dir="ltr" style="text-align: left;">
  <span style="color: #034239;"><strong><tt class="descclassname">cv2.</tt><tt class="descname"><span class="highlighted">namedWindow</span></tt><big>(</big>winname<span class="optional">[</span>, flags<span class="optional">]</span><big>)</big></strong></span>
</p>

<p dir="ltr">
  <span style="color: #034239;"><strong>Parameters:</strong>.</span>
</p>

<ul class="first last simple" dir="ltr">
  <li>
    <span style="color: #034239;"><strong>name</strong> – Name of the window in the window caption that may be used as a window identifier.</span>
  </li>
  <li>
    <span style="color: #034239;"><strong>flags</strong> –Flags of the window. The supported flags are:</span> <ul>
      <li>
        <span style="color: #034239;"><strong>WINDOW_NORMAL</strong> If this is set, the user can resize the window (no constraint).</span>
      </li>
      <li>
        <span style="color: #034239;"><strong>WINDOW_AUTOSIZE</strong> If this is set, the window size is automatically adjusted to fit the displayed image, and you cannot change the window size manually.</span>
      </li>
      <li>
        <span style="color: #034239;"><strong>WINDOW_OPENGL</strong> If this is set, the window will be created with OpenGL support</span>
      </li>
    </ul>
  </li>
</ul>

این سه پارامتر نوع و اندازه‌ی پنجره رو مشخص می‌کنه. [<span style="color: #ff0000;">من در اوبونتو یک باگ دارم و اون اینکه سایز پنجره هنگام استفاده از دستور WINDOW_AUTOSIZE به تناسب صفحه‌ی نمایشم تغییر نمی‌کنه.</span>]

سپس در خط ۲۲ تصویرمون رو نمایش می‌دهیم به این شکل که ابتدا اسم پنجره‌ای که می‌خواهیم تصویر در اون نمایش داده بشه رو می‌گیم (همون اسمی که در خط ۱۸ و ۱۹ ایجاد کردیم) و سپس اسم متغیر عکسی که می‌خواهیم نمایش داده بشه رو وارد می‌کنیم.

در مورد دستور خط آخر [_cv2.waitKey(0)_]، این دستور پنجره‌ها تا زمانی که یک کلید فشرده بشه باز نگه می‌داره، اگر این دستور رو وارد نکنیم عملا نتیجه‌ی کار رو نمی‌بینم (چون پنجره‌ها بلافاصله بسته می‌شوند.)

### **برش و تغییر اندازه‌ی عکس در OpenCV:**

با استفاده از دستور _resize_  می‌توانیم عکس‌ها رو بزرگ و یا کوچیک کنیم،. معمولا برای افزایش سرعت، محاسبات رو بر روی عکس‌هایی که سایر اون‌ها رو کم کره‌ایم انجام می‌دهیم و بعد از اتمام محاسبات میایم و عکس رو به اندازه‌ی اصلی خودش بر می‌گردونیم. همچنین برش زدن عکس بهمون کمک می‌کنه تا فقط روی اون قسمت‌هایی از تصویر که اهمیت دارن پردازش انجام بدهیم. شیوه‌ی کوچک و بزرگ کردن تصویر در OpenCV و همچنین برش تصویر رو در ادامه می‌بینیم:

{% highlight python linenos %}

 کتابخانه‌ی OpenCV رو فرا می‌خونیم
import cv2

# مانند قبل تصویر رو بارگذاری کرده و بررسی می‌کینم آیابه درستی خوانده شده یا نه
originalImage = cv2.imread("mrFox.jpg")
if originalImage is None:
 print("Oh! we have problem in reading image!")

# تصویر رو با نسبت‌های داده شده .۲ و.۱ کوچک می‌کنیم
scaleDown = cv2.resize(originalImage, None, fx=0.1, fy=0.2, interpolation=cv2.INTER_LINEAR)

# تصویر را به نسبت ۲ و ۲ بزرگ می‌کنیم
scaleUp = cv2.resize(originalImage, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# از ۲۵۰ تا ۳۰۰ محورایکس و ۱۰۰ تا ۲۰۰ محور ایگرگ را از تصویر اصلی جدا کرده و در متغیر جدید ذخیره می‌کنیم
crop = originalImage[250:300, 100:200]

# مثل قبل تصاویررا نمایش می‌دهیم
cv2.imshow("Original", originalImage)
cv2.imshow("Scaled Down", scaleDown)
cv2.imshow("Scaled Up", scaleUp)
cv2.imshow("Cropped Image", crop)

cv2.waitKey(0)
{% endhighlight %}

<img loading="lazy" class="wp-image-326 aligncenter" src="https://hue-salari.ir/wp-content/uploads/2-300x169.jpg" alt="" width="533" height="300" srcset="https://hue-salari.ir/wp-content/uploads/2-300x169.jpg 300w, https://hue-salari.ir/wp-content/uploads/2-768x431.jpg 768w, https://hue-salari.ir/wp-content/uploads/2-1024x575.jpg 1024w, https://hue-salari.ir/wp-content/uploads/2.jpg 1280w" sizes="(max-width: 533px) 100vw, 533px" /> 

ما در برنامه‌ی بالا اومدیم و نسبت طول و عرض عکس رو با استفاده از ضرایب fx و fy تغییر دادم، اما اگر بخواهیم تصویر رو به سایز دقیقی مثل ۶۴۰*۴۸۰ تغییر اندازه بدهیم باید به شکل زیر عمل کنیم:

<pre class="EnlighterJSRAW" data-enlighter-language="null">resized = cv2.resize(originalImage,(640,480))
</pre>

این که اومدیم و سایز عکس رو به شکل فله‌ای با دستور بالا تغییر دادیم خیلی جالب نیست، نه؟ بهتره به شکل زیر کار کنیم تا ابعاد تصویر بهم نریزه:

<pre class="EnlighterJSRAW" data-enlighter-language="python"># کتابخانه‌ی OpenCV رو فرا می‌خونیم
import cv2

# مانند قبل تصویر رو بارگذاری کرده و بررسی می‌کینم آیابه درستی خوانده شده یا نه
image = cv2.imread("mrFox.jpg")
if image is None:
    print("Oh! we have problem in reading image!")

# برای این که نسبت‌های عکس بهم نریزه باید مقادیر طول و عرض عکس رو ذخیره کنیم و
# و به نسبت اون‌ها عکس رو تغییر ابعاد بدهیم
xRatio = 480.0
r = xRatio / image.shape[1]
dim = (int(xRatio), int(image.shape[0] * r))

# تغییر ابعاد عکس
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Original Image", image)
cv2.imshow("resized Image", resized)
# چاپ ابعاد اصلی و ابعاد تغییر یافته
print("Original image size: ", image.shape)
print("Resized image size: ", dim)
cv2.waitKey(0)</pre>

<img loading="lazy" class="wp-image-328 aligncenter" src="https://hue-salari.ir/wp-content/uploads/3-300x169.jpg" alt="" width="533" height="300" srcset="https://hue-salari.ir/wp-content/uploads/3-300x169.jpg 300w, https://hue-salari.ir/wp-content/uploads/3-768x431.jpg 768w, https://hue-salari.ir/wp-content/uploads/3-1024x575.jpg 1024w, https://hue-salari.ir/wp-content/uploads/3.jpg 1280w" sizes="(max-width: 533px) 100vw, 533px" /> 

به کاربرد <code class="EnlighterJSRAW">.shape _دقت کنید. قبلا در [این پست][2] در موردش توضیح دادم.

اطلاعات کامل دستور resize  رو هم اینجا میارم:

<p dir="ltr">
  <code class="descclassname">&lt;span style="color: #034239;">cv2.&lt;/span>_<span style="color: #034239;"><code class="descname">Resize_<span class="sig-paren">(</span>src, dst, interpolation=CV_INTER_LINEAR<span class="sig-paren">)</span></span>
</p>

<p dir="ltr" style="text-align: left;">
  <span style="color: #034239;"><strong>Parameters:</strong></span>
</p>

<ul class="first last simple" dir="ltr">
  <li style="text-align: left;">
    <span style="color: #034239;"><strong>src</strong> – input image.</span>
  </li>
  <li style="text-align: left;">
    <span style="color: #034239;"><strong>dst</strong> – output image; it has the size <code class="docutils literal">&lt;span class="pre">dsize&lt;/span>_ (when it is non-zero) or the size computed from <code class="docutils literal">&lt;span class="pre">src.size()&lt;/span>_, <code class="docutils literal">&lt;span class="pre">fx&lt;/span>_, and <code class="docutils literal">&lt;span class="pre">fy&lt;/span>_; the type of <code class="docutils literal">&lt;span class="pre">dst&lt;/span>_ is the same as of <code class="docutils literal">&lt;span class="pre">src&lt;/span>_.</span>
  </li>
  <li style="text-align: left;">
    <span style="color: #034239;"><strong>dsize</strong> –output image size; if it equals zero, it is computed as:</span> <div class="math">
      <p>
        <span style="color: #034239;"><img src="https://docs.opencv.org/2.4/_images/math/35ed0468ed221de8a5f35516bceafda9788cd015.png" alt="\texttt{dsize = Size(round(fx*src.cols), round(fy*src.rows))}" /></span>
      </p>
    </div>
    
    <p>
      <span style="color: #034239;">Either <code class="docutils literal">&lt;span class="pre">dsize&lt;/span>_ or both <code class="docutils literal">&lt;span class="pre">fx&lt;/span>_ and <code class="docutils literal">&lt;span class="pre">fy&lt;/span>_ must be non-zero.</span></li> 
      
      <li style="text-align: left;">
        <span style="color: #034239;"><strong>fx</strong> –scale factor along the horizontal axis; when it equals 0, it is computed as</span> <div class="math">
          <p>
            <span style="color: #034239;"><img src="https://docs.opencv.org/2.4/_images/math/68bc15bc90b1ec313d34f5d72485fa04c51f5c3e.png" alt="\texttt{(double)dsize.width/src.cols}" /></span>
          </p>
        </div>
      </li>
      
      <li style="text-align: left;">
        <span style="color: #034239;"><strong>fy</strong> –scale factor along the vertical axis; when it equals 0, it is computed as</span> <div class="math">
          <p>
            <span style="color: #034239;"><img src="https://docs.opencv.org/2.4/_images/math/af495c626474d56d29d356d581a18f143109e972.png" alt="\texttt{(double)dsize.height/src.rows}" /></span>
          </p>
        </div>
      </li>
      
      <li>
        <span style="color: #034239;"><strong>interpolation</strong> –</span> <p style="text-align: left;">
          <span style="color: #034239;">interpolation method:</span>
        </p>
        
        <ul>
          <li style="text-align: left;">
            <span style="color: #034239;"><strong>INTER_NEAREST</strong> &#8211; a nearest-neighbor interpolation</span>
          </li>
          <li style="text-align: left;">
            <span style="color: #034239;"><strong>INTER_LINEAR</strong> &#8211; a bilinear interpolation (used by default)</span>
          </li>
          <li style="text-align: left;">
            <span style="color: #034239;"><strong>INTER_AREA</strong> &#8211; resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the <code class="docutils literal">&lt;span class="pre">INTER_NEAREST&lt;/span>_ method.</span>
          </li>
          <li style="text-align: left;">
            <span style="color: #034239;"><strong>INTER_CUBIC</strong> &#8211; a bicubic interpolation over 4&#215;4 pixel neighborhood</span>
          </li>
          <li style="text-align: left;">
            <span style="color: #034239;"><strong>INTER_LANCZOS4</strong> &#8211; a Lanczos interpolation over 8&#215;8 pixel neighborhood</span>
          </li>
        </ul>
      </li></ul> 
      
      <p>
        اگر دقت کنید در برنامه‌ی بالا ما تصاویر رو مستقیم نمایش دادیم و مثل قبل نبود که ابتدا یک پنجره رو ایجاد کنیم و سپس تصویر رو نمایش بدیم، خوب این هم یک جورشه:-) [وقت‌هایی از این روش نمایش تصویر استفاده می‌کنیم که نمی‌خوایم روی سایز پنجره تغییری ایجاد کنیم، منظورم همون سه‌تا پارامتر دستور  _cv2.namedWindow_ است.]
      </p>
      
      <p>
        &nbsp;
      </p>
      
      <h3>
        <strong>چرخش عکس در OpenCV:</strong>
      </h3>
      
      <p>
        با OpenCV می‌توان عکس رو از هر نقطه‌ای (هر مرکزی) و با هر زاویه‌‌ی چرخش دلخواهی بچرخونیم.
      </p>
      
      <p>
        در OpenCV چرخش‌ها به شکل یک ماتریس 2&#215;3 بیان می‌شن به این علت که چرخش عضوی از کلاسی از تبدیلات به اسم Affine Transform است (بعدا بیشتر در موردش صحبت می‌کنیم) بیاید اول شکل ریاضی کار رو ببینیم:
      </p>
      
      <p dir="ltr" style="text-align: left;">
        <span style="color: #034239;"><strong>rotMat = getRotationMatrix2D(center, angle, scale)</strong></span>
      </p>
      
      <p id="math--what-is-inside-the-rotation-matrix" dir="ltr" style="text-align: left;">
        <span style="color: #034239;"><strong>getRotationMatrix2D </strong>returns the following matrix<strong> :</strong></span>
      </p>
      
      <p>
        <center dir="ltr">
          <span style="color: #034239;"><strong><img src="https://www.learnopencv.com/wp-content/uploads/2017/11/ocfb-d1-m4-rotation-matrix.png" /></strong></span>
        </center>
      </p>
      
      <p dir="ltr" style="text-align: left;">
        <span style="color: #034239;">Where,</span><br /> <span style="color: #034239;"> <strong> <span class="mathjax"><span id="MathJax-Element-1-Frame" class="MathJax" tabindex="0" role="presentation" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&#x03B1;</mi></math>"><span id="MathJax-Span-1" class="math"><span id="MathJax-Span-2" class="mrow"><span id="MathJax-Span-3" class="mi">α</span></span></span></span></span> </strong>is given by<strong> scale * cos (angle), <span class="mathjax"><span id="MathJax-Element-2-Frame" class="MathJax" tabindex="0" role="presentation" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&#x03B2;</mi></math>"><span id="MathJax-Span-4" class="math"><span id="MathJax-Span-5" class="mrow"><span id="MathJax-Span-6" class="mi">β</span></span></span></span></span></strong> is given by<strong> scale * sin (angle)</strong></span>
      </p>
      
      <p style="text-align: right;">
        پس ما برای استفاده از دستور بالا به مرکز و همچین زاویه‌ی چرخش احتیاج داریم، ماتریس <strong>rotMat</strong> می‌تونه با تابع <strong>warpAffine</strong> استفاده شه تا تصویر دوران یافته رو ایجاد کنیم، بریم و کدهای برنامه رو ببینم:
      </p>
      
      <pre class="EnlighterJSRAW" data-enlighter-language="python"># کتابخانه‌ی OpenCV رو فرا می‌خونیم
import cv2

# مانند قبل تصویر رو بارگذاری کرده و بررسی می‌کینم آیابه درستی خوانده شده یا نه
image = cv2.imread("hmrFox.jpg")
if image is None:
    print("Oh! we have problem in reading image!")

# طول و عرض تصویر رو استخراج کرده و با استفاده از اون مرکز عکس رو پیدا می‌کنیم
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
rotationAngle = 180
scaleFactor = 1.0
# عکس رو 180 درجه می‌چرخونیم
rotationMatrix = cv2.getRotationMatrix2D(center, rotationAngle, scaleFactor)
rotated = cv2.warpAffine(image, rotationMatrix, (w, h))
cv2.imshow("rotated 180 deg", rotated)

# عکس رو +45 درجه می‌چرخونیم
rotationMatrix = cv2.getRotationMatrix2D(center, 45, scaleFactor)
rotated = cv2.warpAffine(image, rotationMatrix, (w, h))
cv2.imshow("rotated +45 deg", rotated)

# عکس رو -45 درجه می‌چرخونیم
rotationMatrix = cv2.getRotationMatrix2D(center, -45, scaleFactor)
rotated = cv2.warpAffine(image, rotationMatrix, (w, h))
cv2.imshow("rotated -45 deg", rotated)

# نمابش عکس اصلی
cv2.imshow("Original Image", image)

# ماتریس rotationMatrix رو نمایش می‌دهیم
print(rotationMatrix)

# صبر می‌کنیم تا کاربر کلیدی را فشار دهد
cv2.waitKey(0)</pre>
      
      <h3>
        <img loading="lazy" class="wp-image-329 aligncenter" src="https://hue-salari.ir/wp-content/uploads/4-300x169.jpg" alt="" width="532" height="300" srcset="https://hue-salari.ir/wp-content/uploads/4-300x169.jpg 300w, https://hue-salari.ir/wp-content/uploads/4-768x431.jpg 768w, https://hue-salari.ir/wp-content/uploads/4-1024x575.jpg 1024w, https://hue-salari.ir/wp-content/uploads/4.jpg 1280w" sizes="(max-width: 532px) 100vw, 532px" />
      </h3>
      
      <h3>
        ذخیره‌ی عکس با کیفیت دلخواه:
      </h3>
      
      <p>
        اول بیایم و تابع ذخیره عکس رو با جزئیات ببینیم:
      </p>
      
      <p dir="ltr">
        <strong>cv2.imwrite(filename, img[, params])</strong>
      </p>
      
      <p dir="ltr">
        <strong>Parameters: </strong>
      </p>
      
      <ul dir="ltr">
        <li>
          <strong>filename</strong> – Name of the file.
        </li>
        <li>
          <strong>image</strong> – Image to be saved.
        </li>
        <li>
          <strong>params</strong> –Format-specific save parameters encoded as pairs <code class="docutils literal">&lt;span class="pre">paramId_1,&lt;/span> &lt;span class="pre">paramValue_1,&lt;/span> &lt;span class="pre">paramId_2,&lt;/span> &lt;span class="pre">paramValue_2,&lt;/span> &lt;span class="pre">...&lt;/span>_ . The following parameters are currently supported: <ul>
            <li>
              For JPEG, it can be a quality ( <code class="docutils literal">&lt;span class="pre">CV_IMWRITE_JPEG_QUALITY&lt;/span>_ ) from 0 to 100 (the higher is the better). Default value is 95.
            </li>
            <li>
              For PNG, it can be the compression level ( <code class="docutils literal">&lt;span class="pre">CV_IMWRITE_PNG_COMPRESSION&lt;/span>_ ) from 0 to 9. A higher value means a smaller size and longer compression time. Default value is 3.
            </li>
            <li>
              For PPM, PGM, or PBM, it can be a binary format flag ( <code class="docutils literal">&lt;span class="pre">CV_IMWRITE_PXM_BINARY&lt;/span>_ ), 0 or 1. Default value is 1.
            </li>
          </ul>
        </li>
      </ul>
      
      <p>
        پس ما می‌تونیم کیفیت دلخواه ذخیره‌ی عکسمون بسته به فرمت فشرده‌سازی اون داشته باشیم. یک مثال با هم ببینیم:
      </p>
      
      <pre class="EnlighterJSRAW" data-enlighter-language="python"># فراخوانی کتابخانه‌های مورد نیاز
import cv2

# بازگگذاری عکس
image = cv2.imread('hmrFox.jpg')

# بررسی معتبر بودن عکس ورودی
if image is None:
    print("Error in readig image")
    exit()

# تبدیل عکس رنگی به خاکستری
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# ایجاد پنجره جهت ذخیره‌ی نمایش عکس‌ها
cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Gray Image', cv2.WINDOW_AUTOSIZE)

key = 0
# حلقه‌ی بینهایت تا زمانی که کلید q فشرده شود
while key != ord('q'):

# نمایش عکس‌ها
    cv2.imshow('Image',image)
    cv2.imshow('Gray Image', gray)
    key = cv2.waitKey(0) & 0xFF

# ذخیره‌ی عکس خاکستری با کیفیت ۵
cv2.imwrite('Gray.jpg',gray, [cv2.IMWRITE_JPEG_QUALITY,10])

# بستن تمام پنجره‌های باز
cv2.destroyAllWindows()</pre>
      
      <p>
        <img loading="lazy" class="size-medium wp-image-408 aligncenter" src="https://hue-salari.ir/wp-content/uploads/quality-300x261.png" alt="" width="300" height="261" srcset="https://hue-salari.ir/wp-content/uploads/quality-300x261.png 300w, https://hue-salari.ir/wp-content/uploads/quality.png 438w" sizes="(max-width: 300px) 100vw, 300px" />
      </p>
      
      <p>
        فکر نکنم نیاز به توضیح خاصی داشته باشیم.
      </p>
      
      <p>
        &nbsp;
      </p>
      
      <hr />
      
      <p>
        جهت دانلودفایل‌های این آموزش می تونید به گیت‌هاب من (<a href="https://github.com/mh-salari/My-Blog-OpenCV-Tutorials/tree/master/02-basic%20image%20operation">به این آدرس</a>) مراجعه کنید.
      </p>
      
      <p>
        نویسنده: <a href="https://hue-salari.ir/">محمد حسین سالاری</a>
      </p>

 [1]: https://hue-salari.ir/install-opencv3-on-ubuntu-17-10/
 [2]: https://hue-salari.ir/introduction-to-numpy/
 [3]: https://docs.opencv.org/3.0-beta/modules/imgproc/doc/miscellaneous_transformations.html#void%20cvtColor(InputArray%20src,%20OutputArray%20dst,%20int%20code,%20int%20dstCn)
