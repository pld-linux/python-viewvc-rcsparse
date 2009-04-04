%bcond_without	tests
#
%define		snap	20080616
%define		module	rcsparse
Summary:	Module for parsing RCS files
Summary(pl.UTF-8):	Moduł do analizy plików RCS
Name:		python-viewvc-%{module}
Version:	0.1
Release:	0.%{snap}.1
License:	GPL
Group:		Libraries/Python
# http://guest@http://viewvc.tigris.org/svn/viewvc/trunk/lib/vclib/ccvs/rcsparse/
Source0:	%{module}-%{snap}.tar.bz2
# Source0-md5:	b0fce6886163f58a6ba3816b9dc25e69
URL:		http://www.viewvc.org/
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

%build
%{?with_tests:%{__python} run-tests.py}

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
