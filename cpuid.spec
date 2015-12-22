#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cpuid
Version  : 20151017
Release  : 1
URL      : http://www.etallen.com/cpuid/cpuid-20151017.src.tar.gz
Source0  : http://www.etallen.com/cpuid/cpuid-20151017.src.tar.gz
Summary  : dumps CPUID information about the CPU(s)
Group    : Development/Tools
License  : GPL-2.0
Requires: cpuid-bin
Requires: cpuid-doc

%description
cpuid dumps detailed information about the CPU(s) gathered from the CPUID 
instruction, and also determines the exact model of CPU(s).

%package bin
Summary: bin components for the cpuid package.
Group: Binaries

%description bin
bin components for the cpuid package.


%package doc
Summary: doc components for the cpuid package.
Group: Documentation

%description doc
doc components for the cpuid package.


%prep
%setup -q -n cpuid-20151017

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cpuid

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
