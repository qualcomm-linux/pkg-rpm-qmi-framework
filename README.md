<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# Package branch — CentOS 10 Stream (`c10s`)

**This is the branch you work on.** It holds your package's spec file and
`sources` pointer, plus the CI workflows that build and publish them.

Following the Fedora/CentOS **dist-git** convention, each distro stream gets its
own branch, and the packaging files live at the branch root:

| Branch | Stream | Contents |
|---|---|---|
| `main` | — | Template docs, onboarding guide, community files. Nothing is built here. |
| **`c10s`** | CentOS 10 Stream | **This branch.** Your spec + `sources` + workflows. |

Full onboarding guide, configuration reference, and troubleshooting live on
[`main`](../../tree/main) — see its `README.md` and `docs/workflows.md`.

---

## Layout

```
qmi-framework.spec      # qmi-framework RPM spec
sources                 # dist-git checksum file
.github/workflows/       # build-on-pr.yml, pkg-release.yml
```

The template's starter files used a `.example` suffix on purpose. The build
expects **exactly one** `*.spec` at the root, so that suffix kept the skeleton
invisible to CI until it was renamed — otherwise a fresh repo's first PR would
fail with `Multiple spec files`.

---

## Getting started

### 1. Rename the starter files

```bash
git mv mypackage.spec.example qmi-framework.spec
git mv sources.example sources
```

### 2. Edit the spec

Set `Name:`, `Version:`, `Summary:`, `License:`, the build/install sections, and
`%files`. `Source0:` must be a real, fetchable URL whose **filename matches the
`sources` entry**:

```
Source0: https://github.com/qualcomm/qmi-framework/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
```

### 3. Record the tarball checksum

**The tarball is never committed to git.** Only its checksum is:

```bash
sha512sum --tag qmi-framework-0.1.4.tar.gz > sources
```

which yields a line like:

```
SHA512 (qmi-framework-0.1.4.tar.gz) = 8dd6ddec078b08aa969761b8c40cc09b2a975cc8de6d992e073e192f0e133929366f7ae19da4fd92f86eea9dd8d967a704936ded1f525c9b6e6194d201715822
```

### 4. Package output

This repository builds the following RPMs:

- `qmi-framework`
- `libqcci1`
- `libqcsi1`
- `libqencdec1`
- `libqmi-common1`
- `qmi-framework-devel`
- `qmi-framework-utils`

### 5. Open a PR against this branch

`build-on-pr` fetches the tarball (from the lookaside cache, or from the spec's
`Source` URL on a cache miss), verifies the checksum, and builds the RPM(s).
Download them from the run's **Artifacts**.


### 6. Release

**Actions → Release → Run workflow**, selecting this branch. A reviewer approves
the `pkg-release-approval` gate, then the RPM(s) publish to Artifactory.

---

## Updating the version

Two edits, every time:

1. Bump `Version:` in the spec (and the `Source0:` URL if its path changed).
2. Recompute the checksum:
   ```bash
   sha512sum --tag qmi-framework-<newversion>.tar.gz > sources
   ```

Commit both, open a PR, merge, then run **Release**. The first release fetches
the new upstream tarball, verifies it, and caches it back automatically.
