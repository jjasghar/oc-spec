# oc-spec

## Scope

This repository holds the [oc.spec](oc.spec) to build the [OpenShift][openshift]
client for Fedora (`.rpm`).

## Usage

To create a builder machine:
```bash
dnf install fedora-packager @development-tools git
```

On prepared builder machine:
```bash
git clone https://github.com/jjasghar/oc-spec
cd oc-spec
rpmbuild -ba oc.spec
```

## License & Authors

If you would like to see the detailed LICENSE click [here](./LICENSE).

- Author: JJ Asghar <awesome@ibm.com>

```text
Copyright:: 2020- IBM, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
