%define	name	detox
%define	version	1.1.1
%define	release	%mkrel 4
%define summary A console utility to clean up filenames
%define group	File tools

Name:		%{name} 
Summary:	%{summary}
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://detox.sourceforge.net
Group:		%{group}
License:	BSD-like

Buildrequires: bison flex

%description
The detox utility renames files to make them easier to work with. It
removes spaces and other such annoyances. It'll also translate or
cleanup Latin-1 (ISO 8859-1) characters encoded in 8-bit ASCII, Unicode
characters encoded in UTF-8, and CGI escaped characters.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# Make sure our config is not +x
chmod a-x $RPM_BUILD_ROOT%{_sysconfdir}/*

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc CHANGES README
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_mandir}/man?/*
%config(noreplace) %_sysconfdir/*

