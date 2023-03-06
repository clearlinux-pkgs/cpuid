#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cpuid
Version  : 20230306
Release  : 33
URL      : https://www.etallen.com/cpuid/cpuid-20230306.src.tar.gz
Source0  : https://www.etallen.com/cpuid/cpuid-20230306.src.tar.gz
Summary  : dumps CPUID information about the CPU(s)
Group    : Development/Tools
License  : GPL-2.0
Requires: cpuid-bin = %{version}-%{release}
Requires: cpuid-license = %{version}-%{release}
Requires: cpuid-man = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
cpuid dumps detailed information about the CPU(s) gathered from the CPUID 
instruction, and also determines the exact model of CPU(s).

%package bin
Summary: bin components for the cpuid package.
Group: Binaries
Requires: cpuid-license = %{version}-%{release}

%description bin
bin components for the cpuid package.


%package license
Summary: license components for the cpuid package.
Group: Default

%description license
license components for the cpuid package.


%package man
Summary: man components for the cpuid package.
Group: Default

%description man
man components for the cpuid package.


%prep
%setup -q -n cpuid-20230306
cd %{_builddir}/cpuid-20230306

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678115665
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1678115665
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cpuid
cp %{_builddir}/cpuid-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/cpuid/4cc77b90af91e615a64ae04893fdffa7939db84c || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cpuid
/usr/bin/cpuinfo2cpuid

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cpuid/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cpuid.1.gz
/usr/share/man/man1/cpuinfo2cpuid.1.gz
