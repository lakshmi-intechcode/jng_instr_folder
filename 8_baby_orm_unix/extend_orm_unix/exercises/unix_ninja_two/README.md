Unix Ninja 2
============

ARE YOU READY FOR SOME MORE UNIX FUN?!!?!?!!?!!!!!!!!!!!!!??????

type these command into terminal

```bash
$ a=yo
$ b="armen and greg are the greatest, one"
$ echo $a
$ echo $b
```

Isn't that neat? We can store variables in our shell. That seems like it would be useful for if we wanted to write shell scripts...  
Anyways. write the variable b that you just saved to a .txt file. If you don't know how to do that, I recommend referring to yesterday's work. After you finish writing it to a txt file, take the contents of the text file you created, and tweet it.

We're going to have some fun with the text file attached.  
Python is a scripting language. So we can write scripts in it to do a lot of work for us. Write a script that creates 5 files and writes each consecutive line to it's respective file.

Make a sixth file. Have it write all of the lines with the word 'sculpture', and how many times the word appears. You can just make the files .txt, feel free to name them whatever you want.  
You should not be naming these manually. Your script should do all of it.

If I gave you a 100 line text file, it would make 100 folders with .txt files in them, and one file with all of the lines that contain the word 'sculpture', and the word count as the last night.

You will find the [subprocess](https://docs.python.org/3/library/subprocess.html) module helpful for this assignment. What does the shell parameter do?

Unix Ninja 3
============

Today we're going to take a look at a few more commands.  

#### uniq

Type `$ man uniq` into your terminal and read the man page.

Type `$ uniq text.txt`. What do you get?

Can you get only one of each word?

How about the counts for each word?

Can you combine the two?

#### ps and top

Open a new tab in your terminal and type `$ ps`.

What is that? Let's man it.

While we're at it, let's type `$ man kill`.

Take the PID from one of your terminal processes and type `kill -9 [PID]`. Don't type PID, insert your PID where I typed it.

What does PID stand for?

What happened when you did that?

Remember this command. Sometimes when you're running a local server, it won't close it connection to a port. You can kill the process to open the port again.

Now try `$ top`. What's the difference between ps and top?

#### diff

Type `$ man diff` and read the man page.

Get the diff of text.txt and yo.txt. See how the syntax works. Change the files around, and see how it changes the diff. This may look similar to when you've had a merge conflict, or if you've ever used `git diff`.

#### chmod

Here is some reading on [chmod](http://www.perlfect.com/articles/chmod.shtml).

Read the man on chmod and [chown](http://www.computerhope.com/unix/uchown.htm), as well.

There won't be any exercises on these functions, but you should know them. How do file permissions work in Unix?

#### stdio

Read about [stdio](http://en.wikipedia.org/wiki/Standard_streams). This plays a big role in backend processes. It's a little hard to grasp, so I just want to introduce you to the concept.

#### du

	$ man du
	$ du
	$ du text.txt
	$ du ../

This doesn't matter as much, anymore, since your computer has so much space. Back in the day you had to be much more frugal with disk space. Still, now you know how to know how much space a file or folder is taking.

#### cksum

Read about what a checksum is [here](http://en.wikipedia.org/wiki/Checksum)

The command cksum generates a checksum for any data or file.

Get the checksum of text.txt and compare it to the checksum of yo.txt.

Now duplicate text.txt using cat and compare the checksums again.