# Cross Browser Testing with LambdaTest using Pylenium + pytest

This repo accompanies the LambdaTest YouTube video series and includes all of the code examples seen in each video.

> This series is all about using Pylenium + pytest to perform Cross Browser Testing with LambdaTest!

## How to use this repo

If you want to follow along with the exact setup that I'm using, then I recommend watching my YouTube video called:

[Setup VS Code for Python with pyenv & poetry](https://youtu.be/547Jr26duHQ)

> I highly recommend watching the above video! It will guide you through setting up your machine and your IDE for Python Development!

Then clone this project and you're ready to follow the remaining steps!

1. If using `poetry`, then install the dependencies which will also create a virtual environment automatically. (If you followed the recommended video, this step is already done.)

```bash
poetry install
```

Otherwise, create a virtual environment first and then install Pylenium in it:

```bash
pip install pyleniumio
```

2. Pylenium uses `pytest` as the Test Framework, but you need to setup your IDE to use pytest. (If you followed the recommended video, this step is already done.)

3. There is a branch for each video in the series. Within each branch, there is a commit with different pieces as I progress through the video. This is helpful since you can follow the progression of the code in the video. You can pause the video, checkout the commit we're currently working on, and copy + paste or try things yourself!

> I've included the links to each commit below for convenience :)

**_Video 1 - Introduction and Setup_**

- No code yet at this point

**_Video 2 - Write UI Tests_**

- [Write the first test](https://github.com/ElSnoMan/LambdaTest-with-python/commit/1304dab5bc7cdacb63e6b9cb45f265b2e553769f)
- [Write the second test](https://github.com/ElSnoMan/LambdaTest-with-python/commit/8ba654fb2b0299fb0a3de5aac5800b7156d5c976)
- [Refactor logic to TodoPage and page fixture](https://github.com/ElSnoMan/LambdaTest-with-python/commit/5521c6d9b4ee3000864d4f04ea12b0fcb0b85fc2)
- [Write a new test and cleanup our existing tests](https://github.com/ElSnoMan/LambdaTest-with-python/commit/4b994065c8fb06a1edbe9e3f05bb6bed46555058)
- [Design decision: move .get('input') to our class methods?](https://github.com/ElSnoMan/LambdaTest-with-python/commit/726da7cd5c08e141c6a7d21955622e04eb835c74)
- [Write the final test](https://github.com/ElSnoMan/LambdaTest-with-python/commit/26c7b0ef32c4f64db62ed7166eda9651a3e619d8)

**_Video 3 - Run Tests in Parallel_**

- [Tests with a shared driver](https://github.com/ElSnoMan/LambdaTest-with-python/commit/83f4f9f1da7ba71a9aa273c98701ac4265b4a057)

**_Video 4 - Cross Browser Testing with LambdaTest_**

- [LambdaTest fixture example with Selenium](https://github.com/ElSnoMan/LambdaTest-with-python/commit/e942fd35a1def236e436816e70d6fa141d627847)
- [Connect to LambdaTest with Pylenium](https://github.com/ElSnoMan/LambdaTest-with-python/commit/58f20c50b82930e7341f19db50334d4587ede3d5)
- [Change config to target Edge on MacOS Sierra](https://github.com/ElSnoMan/LambdaTest-with-python/commit/272a079f4ee3c51836bc19b81b9afc6f583dd54e)
- [Different tests with different browsers](https://github.com/ElSnoMan/LambdaTest-with-python/commit/c0502f4785837e6f2839f4902ac87c6e028cc4ea)
- [One test against multiple browsers](https://github.com/ElSnoMan/LambdaTest-with-python/commit/e261a4857b9967ab0936ec1f5d4b5b0de369d067)
