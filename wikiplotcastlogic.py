import wikipedia as w

new = w.page("2006_in_film")
linkset = set(new.links)
print("Links retrieved", len(linkset))
movieset = []
for s in linkset:
    try:
        contentinfo = w.page(s).content
        print("Searching: ", s)
        if "== Plot ==" in contentinfo:
            movieset.append(s)
            contentinfo = contentinfo.split('== Plot ==')[1]
            try:
                plot = contentinfo.split('== Cast ==')[0]
                plot = plot.encode('utf8')
                with open(str(len(movieset)) + ' plot', 'wb') as f:
                    f.write(plot)
                cast = contentinfo.split('== Cast ==')[1].split('==')[0]
                cast = cast.encode('utf8')
                with open(str(len(movieset)) + ' cast', 'wb') as f1:
                    f1.write(cast)
            except Exception:
                pass
            print("Movie added: ", s, len(movieset))
    except Exception:
        pass
with open(new.title, 'w') as f2:
    f2.write("\n".join(movieset))
