%include	/usr/lib/rpm/macros.python
%define		snap	20030925
%define		module	rcsparse
Summary:	Module for parsing RCS files
Name:		python-%{module}
Version:	0.1
Release:	0.%{snap}.1
License:	GPL
Group:		Libraries/Python
# http://cvs.sourceforge.net/viewcvs.py/viewcvs/viewcvs/lib/vclib/ccvs/rcsparse/
Source0:	%{module}-%{snap}.tar.gz
# Source0-md5:	7cabbe1b8f387a22bbfe7948c2cd95e9
URL:		http://viewcvs.sourceforge.net/
BuildRequires:	python-modules
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rcsparse.py is a Python module parsing RCS files.

%prep
%setup -q -n %{module}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}/%{module}

install *.py	$RPM_BUILD_ROOT%{py_sitedir}/%{module}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
