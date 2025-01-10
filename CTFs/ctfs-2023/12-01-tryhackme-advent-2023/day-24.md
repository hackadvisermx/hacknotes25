
# Task 30  [Day 24] Mobile analysis You Are on the Naughty List, McGreedy

## Learning Objectives

After completing this task, you will learn about:

- Procedures for collecting digital evidence
- The challenges with modern smartphones
- Using Autopsy Digital Forensics with an actual Android image

## Digital Forensics

Forensics is a method of using science to solve crimes. As a forensic scientist, you would expect to collect evidence from crime scenes, such as fingerprints, DNA, and footprints. You would use and analyse this evidence to determine what happened at the crime scene and who did it.

With the spread of digital equipment, such as computers, phones, smartphones, tablets, and digital video recorders, a different set of tools and training are required. When it comes to digital evidence, the ideal approach is to acquire a raw image. A raw image is a bit-for-bit copy of the device’s storage.

Forensics is an essential part of the criminal justice system. It helps to solve crimes and bring criminals to justice. However, for evidence to be permissible in court, we must ensure that it’s not tampered with or lost and that it’s authentic when presented to the court. This is why we need to maintain a chain of custody. Chain of custody is a legal concept used to track the possession and handling of evidence from the time it’s collected at a crime scene to the moment it’s presented in court. The chain of custody is documented through a series of written records that track the evidence’s movement and who handled it at each step.

## Acquiring a Digital Forensic Image

Acquiring an image for digital forensics can be challenging, depending on the target device. Computers are more accessible than other devices, so we’ll start our discussion by focusing on them.

There are four main types of forensic image acquisition:

- Static acquisition: A **bit-by-bit image** of the disk is created while the device is turned off.
- Live acquisition: A **bit-by-bit image** of the disk is created while the device is turned on.
- Logical acquisition: A **select list of files** is copied from the seized device.
- Sparse acquisition: Select **fragments of unallocated data** are copied. The unallocated areas of the disk might contain deleted data; however, this approach is limited compared to static and live acquisition because it doesn’t cover the whole disk.

Let’s consider the following two scenarios:

- The seized computer is switched off.
- As part of a crime scene, the investigators stumble on a live computer that’s switched on.

### A Computer That’s Switched Off

Imagine the evidence is a Windows 10 laptop that’s switched off. We know that by default, the disk is not encrypted. We should not turn it on as this will make some changes to the disk and tamper with the evidence as a result. Removing the hard disk drive or SSD from the laptop and cloning it is a relatively simple task:

- We use a write blocker, a hardware device that makes it possible to clone a disk without any risk of modifying the original data.
- We rely on our forensic imaging software to get the raw image or equivalent. This would create a bit-by-bit copy of the disk.
- Finally, we need a suitable storage device to save the image.

### A Computer That’s Switched On

Another example would be dealing with a laptop that is switched on. In this case, we shouldn’t switch it off. Instead, we should aim for a live image. The laptop might be encrypted, and shutting it down will make reading its data impossible without a password. Furthermore, data in the volatile memory (RAM) might be important for our investigation.

When they’re able to analyse a device that’s switched on, investigators can gain access to the accounts and services the suspect is logged into. This can be indispensable in some instances to prove guilt and solve a crime.

Various tools can be used. They usually require us to run a program on the target system, giving us access to all the data in the volatile memory and on the non-volatile memory (disk).

## Acquiring a Smartphone Image

The smartphone is a ubiquitous digital device that we can expect to encounter. Modern smartphones are now encrypted by default, which can be a challenge for digital forensics. Without the decryption key, encrypted storage looks literally like random data. Finding the decryption key is crucial to be able to analyse the image.

Let us briefly overview smartphone encryption before discussing acquiring a forensic image of an Android device.

### Encryption in Smart Phones

Android 4.4 introduced **full-disk encryption**. When full-disk encryption is activated, the user-created data is automatically encrypted before being written to the device storage and decrypted before being read from the storage. Furthermore, the phone cannot be booted before providing the password. It is important to note that this type of encryption applies to built-in storage and doesn’t include removable memory, such as micro SD cards.

Android 7.0 introduced _Direct Boot_, a **file-based encryption** mode. File-based encryption lets us use different keys for different files. From the user’s perspective, the phone can be booted, and some basic functionality can be used, such as receiving phone calls. Beyond this basic functionality, the encryption password needs to be provided. Depending on the settings and Android version, the SD card might also be encrypted; Android 9.0 and higher can encrypt an SD card as it would encrypt internal storage.

Since Android 6.0, encryption has been mandatory. Unless we are dealing with an older Android version, we can expect the seized phone to be encrypted. Apple iPhone devices are encrypted by default, too. _Data Protection_, a **file-based encryption** methodology, is part of iOS, the iPhone’s operating system.

In this section, we provided an overview of smartphone encryption. Ultimately, encryption can be a significant obstacle that digital forensic investigators need to overcome. Obtaining or discovering the encryption key is necessary for a complete digital forensic investigation.

