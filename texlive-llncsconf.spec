Name:		texlive-llncsconf
Version:	63136
Release:	2
Summary:	LaTeX package extending Springer's llncs class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/llncsconf
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/llncsconf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/llncsconf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends Springer's llncs class for adding
additional notes describing the status of the paper (submitted,
accepted) as well as for creating author-archived versions that
include the references to the official version hosted by
Springer (as requested by the copyright transfer agreement for
Springer's LNCS series).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/llncsconf
%doc %{_texmfdistdir}/doc/latex/llncsconf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
