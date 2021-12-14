#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : resolvelib
Version  : 0.8.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/ac/20/9541749d77aebf66dd92e2b803f38a50e3a5c76e7876f45eb2b37e758d82/resolvelib-0.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/20/9541749d77aebf66dd92e2b803f38a50e3a5c76e7876f45eb2b37e758d82/resolvelib-0.8.1.tar.gz
Summary  : Resolve abstract dependencies into concrete ones
Group    : Development/Tools
License  : ISC
Requires: resolvelib-license = %{version}-%{release}
Requires: resolvelib-python = %{version}-%{release}
Requires: resolvelib-python3 = %{version}-%{release}
Requires: black
Requires: build
Requires: flake8
Requires: html5lib
Requires: isort
Requires: mypy
Requires: packaging
Requires: requests
Requires: twine
BuildRequires : black
BuildRequires : build
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : html5lib
BuildRequires : isort
BuildRequires : mypy
BuildRequires : packaging
BuildRequires : requests
BuildRequires : twine

%description
==========
ResolveLib
==========
ResolveLib at the highest level provides a ``Resolver`` class that includes
dependency resolution logic. You give it some things, and a little information
on how it should interact with them, and it will spit out a resolution result.

%package license
Summary: license components for the resolvelib package.
Group: Default

%description license
license components for the resolvelib package.


%package python
Summary: python components for the resolvelib package.
Group: Default
Requires: resolvelib-python3 = %{version}-%{release}

%description python
python components for the resolvelib package.


%package python3
Summary: python3 components for the resolvelib package.
Group: Default
Requires: python3-core
Provides: pypi(resolvelib)

%description python3
python3 components for the resolvelib package.


%prep
%setup -q -n resolvelib-0.8.1
cd %{_builddir}/resolvelib-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636415328
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/resolvelib
cp %{_builddir}/resolvelib-0.8.1/LICENSE %{buildroot}/usr/share/package-licenses/resolvelib/e8f006df7200afbbdd3a2e7a85e487338dc75073
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/resolvelib/e8f006df7200afbbdd3a2e7a85e487338dc75073

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
