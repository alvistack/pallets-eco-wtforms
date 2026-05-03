# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-wtforms
Epoch: 100
Version: 3.2.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Form validation and rendering for Python web development
License: BSD-3-Clause
URL: https://github.com/pallets-eco/wtforms/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
WTForms is a flexible forms validation and rendering library for Python 
web development. It can work with whatever web framework and template
engine you choose. It supports data validation, CSRF protection,
internationalization (I18N), and more. There are various community
libraries that provide closer integration with popular frameworks.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} >= 1500
%package -n python%{python3_version_nodots}-wtforms
Summary: Form validation and rendering for Python web development
Requires: python3
Requires: python3-MarkupSafe >= 1.1.1
Provides: python3-wtforms = %{epoch}:%{version}-%{release}
Provides: python3dist(wtforms) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wtforms = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wtforms) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wtforms = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wtforms) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-wtforms
WTForms is a flexible forms validation and rendering library for Python 
web development. It can work with whatever web framework and template
engine you choose. It supports data validation, CSRF protection,
internationalization (I18N), and more. There are various community
libraries that provide closer integration with popular frameworks.

%files -n python%{python3_version_nodots}-wtforms
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} >= 1500)
%package -n python3-wtforms
Summary: Form validation and rendering for Python web development
Requires: python3
Requires: python3-markupsafe >= 1.1.1
Provides: python3-wtforms = %{epoch}:%{version}-%{release}
Provides: python3dist(wtforms) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wtforms = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wtforms) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wtforms = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wtforms) = %{epoch}:%{version}-%{release}

%description -n python3-wtforms
WTForms is a flexible forms validation and rendering library for Python
web development. It can work with whatever web framework and template
engine you choose. It supports data validation, CSRF protection,
internationalization (I18N), and more. There are various community
libraries that provide closer integration with popular frameworks.

%files -n python3-wtforms
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%changelog
