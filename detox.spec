Name:		detox
Summary:	A console utility to clean up filenames
Version:	1.2.0
Release:	%{mkrel 2} 
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.2.0-fix-str-fmt.patch
URL:		http://detox.sourceforge.net
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	BSD-like
Buildrequires:	bison
Buildrequires:	flex

%description
The detox utility renames files to make them easier to work with. It
removes spaces and other such annoyances. It'll also translate or
cleanup Latin-1 (ISO 8859-1) characters encoded in 8-bit ASCII, Unicode
characters encoded in UTF-8, and CGI escaped characters.

%prep
%setup -q
%patch0 -p1 -b .strfmt

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall
# Make sure our config is not +x
chmod a-x %{buildroot}%{_sysconfdir}/*

%clean 
rm -rf %{buildroot} 

%files 
%defattr(-,root,root)
%doc CHANGES README
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/inline-%{name}
%{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*

