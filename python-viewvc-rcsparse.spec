%define		snap	20031026
%define		module	rcsparse
Summary:	Module for parsing RCS files
Summary(pl.UTF-8):	Moduł do analizy plików RCS
Name:		python-%{module}
Version:	0.1
Release:	0.%{snap}.4
License:	GPL
Group:		Libraries/Python
# http://cvs.sourceforge.net/viewcvs.py/viewcvs/viewcvs/lib/vclib/ccvs/rcsparse/
Source0:	%{module}-%{snap}.tar.gz
# Source0-md5:	dbf7cf8f43c4941d95834a0caf0dff86
URL:		http://viewcvs.sourceforge.net/
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rcsparse.py is a Python module parsing RCS files.

%description -l pl.UTF-8
rcsparse.py to moduł Pythona do analizy plików RCS.

%prep
%setup -q -n %{module}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}

install *.py	$RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/rcsparse
%{py_sitescriptdir}/rcsparse/*.py[co]
