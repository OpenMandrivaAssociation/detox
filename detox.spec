Name:		detox
Summary:	A console utility to clean up filenames
Version:	1.2.0
Release:	3
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
export CC=gcc
export CXX=g++
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install
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



%changelog
* Mon May 18 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 1.2.0-2mdv2010.0
+ Revision: 376817
- add a patch to fix str fmt

* Wed Oct 01 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.0-1mdv2009.0
+ Revision: 290280
- minor spec cleanups
- new version 1.2.0 (fixes large file support, #44313)

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-6mdv2009.0
+ Revision: 240602
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Apr 25 2007 Eskild Hustvedt <eskild@mandriva.org> 1.1.1-4mdv2008.0
+ Revision: 18184
- Fix buildrequires and yearly rebuild


* Fri Nov 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.1.1-3mdk
- Fix BuildRequires

* Sat Apr 02 2005 Eskild Hustvedt <eskild@mandrake.org> 1.1.1-2mdk
- %%mkrel

* Sun Mar 13 2005 Eskild Hustvedt <eskild@mandrake.org> 1.1.1-1mdk
- Initial Mandrakelinux package

