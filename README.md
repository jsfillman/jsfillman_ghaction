# KBase SDK Build Action
This is a demo of building and testing KBase Apps using :octocat: Actions.

## Current Status

| Branch  | Build                                                              | Coverage                                                                         | LGTM Alerts                                                     |
| ------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| master  | [![Run SDK Tests](https://github.com/jsfillman/jsfillman_ghaction/workflows/Run%20SDK%20Tests/badge.svg)](https://github.com/jsfillman/jsfillman_ghaction/actions?query=workflow%3A%22Run+SDK+Tests%22)  | Coming Soon | [![Total alerts](https://img.shields.io/lgtm/alerts/g/jsfillman/jsfillman_ghaction.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/jsfillman/jsfillman_ghaction/alerts/)  |


## Details 
You will need to have the SDK installed to use this module. [Learn more about the SDK and how to use it](https://kbase.github.io/kb_sdk_docs/).

You can also learn more about the apps implemented in this module from its [catalog page](https://narrative.kbase.us/#catalog/modules/jsfillman_ghaction) or its [spec file]($module_name.spec).

### Setup and test

Add your KBase developer token to `test_local/test.cfg` and run the following:

```bash
$ make
$ kb-sdk test
```

After making any additional changes to this repo, run `kb-sdk test` again to verify that everything still works.

### Installation from another module

To use this code in another SDK module, call `kb-sdk install jsfillman_ghaction` in the other module's root directory.

### Help

You may find the answers to your questions in our [FAQ](https://kbase.github.io/kb_sdk_docs/references/questions_and_answers.html) or [Troubleshooting Guide](https://kbase.github.io/kb_sdk_docs/references/troubleshooting.html).
