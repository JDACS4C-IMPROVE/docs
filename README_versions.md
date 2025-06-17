## Changing the versions switcher

**Note:** The versions switcher will not build locally. On a local build you should see the box, but it won't populate with the versions. This currently only works on the GitHub Actions workflow run.

1) Make a new branch that will contain the static version. This will probably be the main as is, name it with 'static' and the version number like 'static-vX.X.X'.

2) Edit the top of the index.rst file with a warning similar to this:

```
.. warning::

   This documentation is for the most recent release of IMPROVE (v0.1.0). You can see the latest version of IMPROVE `here <https://jdacs4c-improve.github.io/docs/>`_.
```

3) Commit to this new branch with the static version but DO NOT MERGE TO MAIN.

4) Go to the previous version and change the warning in index.rst to similar to below. Commit but do not merge to main.

```
.. warning::

   This documentation is for a previous release of IMPROVE (v0.0.3-beta). You can see the latest release of IMPROVE `here <https://jdacs4c-improve.github.io/docs/v0.1.0/>`_ and the latest version of IMPROVE `here <https://jdacs4c-improve.github.io/docs/>`_. 
```

5) Make a patch branch from main (because main is protected).

6) Edit `versions.yaml` in the patch branch, placing the new version at the top of the file (so it shows first in the list):

```
"<VERSION_TO_DISPLAY>":
  tag: '<BRANCH_NAME>' 
```

7) Change the warning in index.rst in the patch branch to reflect the link to the latest release version.


8) PR this patch branch to main. Delete the patch branch so it doesn't clutter the branches.


9) Go to `Actions` (at the top), `versions-natasha` (at the left side), `Run workflow` (on the right), `Run workflow`. You should see a new workflow appear with the name versions-natasha with a yellow spinning circle. When this turns green you can check the documentation site. It should take about a minute. Double check that the versions and banners are showing as expected.


**Note:** If you made changes to conf.py (referencing new CSS sheets, etc), it seems like these changes need to be carried over to all version branches or the versions do not show correctly.


To Do:
- Have the banner show on all pages (probably using prolog).
