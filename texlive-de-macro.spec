%global tl_name de-macro
%global tl_revision 66746

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.1
Release:	%{tl_revision}.1
Summary:	Expand private macros in a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/de-macro
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/de-macro.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/de-macro.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(de-macro.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
De-macro is a Python script that helps authors who like to use private
LaTeX macros (for example, as abbreviations). A technical editor or a
cooperating author may balk at such a manuscript; you can avoid
manuscript rejection misery by running de-macro on it. De-macro will
expand macros defined in \(re)newcommand or \(re)newenvironment
commands, within the document, or in the document's "private" package
file.

