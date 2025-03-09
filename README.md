# spy
### ** (Steganography + Shell)**

কোডটি (ছবির ভিতরে ডাটা লুকানো) ফিচার একত্রিত করা হয়েছে।

### **Step-by-Step Guide: Termux Setup & Execution**

1. **Termux ইনস্টল করুন (Android ডিভাইসে)**:
   - **Termux** ইনস্টল করার জন্য Google Play Store থেকে **Termux** অ্যাপটি ডাউনলোড এবং ইনস্টল করুন।

2. **Termux-এ প্রয়োজনীয় প্যাকেজ ইনস্টল করুন**:
   - **Python** এবং **Tkinter** ইন্সটল করতে হবে।

   ```bash
   pkg update && pkg upgrade -y
   pkg install python -y
   pkg install python-pip -y
   pip install stegano
   pip install tk
   pkg instoll git
   git clone https://github.com/RH0099/spy.git
   ```

3. **কোড ফাইল তৈরি করুন**:
   - কোডটি একটি `.py` ফাইলে সেভ করতে হবে। আপনি Termux এর মধ্যে যে কোনো টেক্সট এডিটর ব্যবহার করে ফাইলটি তৈরি করতে পারেন, যেমন:
   
   ```bash
   cd spy
   ```

5. **স্টেগানোগ্রাফি এবং ব্যাকডোর চালু করুন**:
   - কোড ফাইলটি চালাতে হলে **Python** দিয়ে রান করতে হবে:
   ```bash
   python Spy.py
   ```

   এতে একটি GUI প্রদর্শিত হবে যেখানে আপনি ছবি নির্বাচন করে গোপন বার্তা লুকাতে পারবেন। 
---

### **Information Capture Workflow**:
এখানে আপনার **Information Capture** প্রক্রিয়া কীভাবে কাজ করবে তা বিস্তারিত:

1. **স্টেগানোগ্রাফি**:
   - **ব্যবহারকারী একটি ছবি নির্বাচন করবে**।
   - **সেক্রেট মেসেজ** (যেমন ফাইল বা টেক্সট) সেই ছবির মধ্যে লুকানো হবে।
   - ব্যবহারকারী সেই ছবি **output.png** হিসাবে সেভ করবে। এই ছবিটি এখন বাহ্যিকভাবে কোনো কিছু ধারণ করছে না, কিন্তু এটি আসলে গোপন তথ্য ধারণ করছে।

