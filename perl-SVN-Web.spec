#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SVN
%define		pnam	Web
Summary:	Subversion repository web frontend
Summary(pl):	Frontend WWW dla repozytoriów subversion
Name:		perl-%{pdir}-%{pnam}
Version:	0.41
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae343e3dcd1f220cc1740e9ad44c59fa
URL:		http://search.cpan.org/~nikc/SVN-Web/
BuildRequires:	perl-Locale-Maketext-Lexicon
BuildRequires:  perl-Locale-Maketext-Simple
BuildRequires:	perl-Template-Plugin-Number-Format
BuildRequires:	perl-Template-Toolkit
BuildRequires:  perl-Text-Diff
BuildRequires:	perl-Text-Diff-HTML
BuildRequires:  perl-URI
BuildRequires:  perl-XML-RSS
BuildRequires:  perl-YAML
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-subversion >= 1.0.4
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
#BuildRequires:	perl-Test-WWW-Mechanize ?
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subversion repository web frontend.

%description -l pl
Frontend WWW dla repozytoriów subversion.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/SVN/Web
%{perl_vendorlib}/SVN/Web.pm
%{perl_vendorlib}/SVN/*.pod
%{_mandir}/man3/*
