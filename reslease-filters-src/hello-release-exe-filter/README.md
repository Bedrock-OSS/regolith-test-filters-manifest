# What is this filter?
This filter creates a `BP/hello_release_exe_filter.txt` file and writes the following content to it:

```txt
Hello from hello-release-exe-filter!
```

# How to build it?

Run the `build-script.py`. It creates 2 zip files:
- `windows.zip` - Contains the Windows executable and `filter.json`.
- `linux.zip` - Contains the Linux executable and `filter.json`.

After that make a release on GitHub and upload the zip files (this part is not automated).
